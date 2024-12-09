class SubmitBidUseCase:
    def __init__(self, auction_repository: AuctionRepository):
        self._auction_repository = auction_repository

    async def __call__(self, bid: Bid) -> None: ...