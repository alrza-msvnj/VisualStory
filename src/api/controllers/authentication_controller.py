from fastapi import Depends, APIRouter, Response
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.dependencies import get_authentication_service
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest


class AuthenticationController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/authentication", tags=["Authentication"])
        self.router.post("/register", response_model=RegisterResponse)(self.register)
        self.router.post("/login")(self.login)
        self.router.get("/logout")(self.logout)

    @staticmethod
    async def register(request: RegisterRequest,
                       service: IAuthenticationService = Depends(get_authentication_service)) -> RegisterResponse:
        return await service.register(request)

    @staticmethod
    async def login(response: Response, request: LoginRequest,
                    service: IAuthenticationService = Depends(get_authentication_service)):
        login_response = await service.login(request)
        if not login_response.success:
            return {"success": False, "message": login_response.message}

        response.set_cookie(
            key="session_id",
            value=login_response.value,
            secure=True,  # Use True in production with HTTPS
            max_age=3600,  # Session expires in 1 hour
        )

        response.headers['X-Redirect-To'] = '/'
        return {"message": "Login successful"}

    @staticmethod
    async def logout(response: Response):
        response.delete_cookie("session_id")
        response.headers['X-Redirect-To'] = '/'
        return {"message": "Logged out successfully"}
