from src.infrastructure.repositories.user_repository import UserRepository


class SubmitBidUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def __call__(self, bid: Bid) -> None: ...
