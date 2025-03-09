import os
import shutil
import uuid
from typing import List
from dotenv import load_dotenv
from fastapi import Depends, APIRouter, File, UploadFile, HTTPException, Request
from itsdangerous import URLSafeTimedSerializer
from src.application.contracts.user_service import IUserService
from src.application.dependencies import get_user_service
from src.application.dtos.user.add_user_dto import AddUserRequest, AddUserResponse
from src.application.dtos.user.get_user_dto import GetUserRequest, GetUserResponse
from src.application.dtos.user.get_all_user_dto import GetAllUserResponse
from src.application.dtos.user.update_user_dto import UpdateUserRequest, UpdateUserResponse
from src.application.dtos.user.delete_user_dto import DeleteUserRequest, DeleteUserResponse
from src.application.dtos.user.get_by_username_dto import GetByUsernameRequest, GetByUsernameResponse
from src.application.dtos.user.get_profile_dto import GetProfileRequest, GetProfileResponse
from src.application.dtos.user.save_profile_picture_dto import SaveProfilePictureRequest

UPLOAD_DIR = "src/ui/static/assets/profile_pictures"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the directory exists
load_dotenv()


class UserController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/user", tags=["User"])
        self.router.post("/", response_model=AddUserResponse)(self.add)
        self.router.get("/{id}", response_model=GetUserResponse)(self.get)
        self.router.get("/", response_model=List[GetAllUserResponse])(self.get_all)
        self.router.put("/", response_model=UpdateUserResponse)(self.update)
        self.router.delete("/{id}")(self.delete)
        self.router.get("/get_by_username/{username}", response_model=GetByUsernameResponse)(self.get_by_username)
        self.router.post("/get_profile_picture", response_model=GetProfileResponse)(self.get_profile)
        self.router.post("/upload_profile_picture")(self.upload_profile_picture)

    @staticmethod
    async def add(request: AddUserRequest, service: IUserService = Depends(get_user_service)) -> AddUserResponse:
        return await service.add(request)

    @staticmethod
    async def get(user_id: int, service: IUserService = Depends(get_user_service)) -> GetUserResponse:
        return await service.get(GetUserRequest(id=user_id))

    @staticmethod
    async def get_all(service: IUserService = Depends(get_user_service)) -> List[GetAllUserResponse]:
        return await service.get_all()

    @staticmethod
    async def update(request: UpdateUserRequest,
                     service: IUserService = Depends(get_user_service)) -> UpdateUserResponse:
        return await service.update(request)

    @staticmethod
    async def delete(user_id: int, service: IUserService = Depends(get_user_service)) -> DeleteUserResponse:
        return await service.delete(DeleteUserRequest(id=user_id))

    @staticmethod
    async def get_by_username(username: str, user_service: IUserService = Depends(get_user_service)) -> AddUserResponse:
        return await user_service.get_by_username(GetByUsernameRequest(username=username))

    @staticmethod
    async def get_profile(request: Request, user_service: IUserService = Depends(get_user_service)) -> GetProfileResponse:
        serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
        session_id = request.cookies.get('session_id')
        if not session_id:
            raise HTTPException(status_code=400, detail="Login required")
        session = serializer.loads(session_id)

        get_profile_request = GetProfileRequest(
            user_id=session['user_id']
        )

        response = await user_service.get_profile(get_profile_request)

        return response

    @staticmethod
    async def upload_profile_picture(request: Request, image: UploadFile = File(...),
                                     user_service: IUserService = Depends(get_user_service)):
        try:
            unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(image.filename)[1]}"
            file_path = os.path.join(UPLOAD_DIR, unique_filename)

            serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
            session_id = request.cookies.get('session_id')
            if not session_id:
                raise HTTPException(status_code=400, detail="Login required")
            session = serializer.loads(session_id)

            profile_picture = SaveProfilePictureRequest(
                user_id=session['user_id'],
                profile_picture=unique_filename
            )

            success = await user_service.save_profile_picture(profile_picture)

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            if success:
                return unique_filename
            else:
                return None

        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Image processing error: {str(e)}")
