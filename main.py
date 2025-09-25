from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import router as auth_router
from auction.routes import router as auction_router
from wallet.routes import router as wallet_router
from yellow.routes import router as yellow_router
from chain.routes import router as chain_router
from settlement.routes import router as settlement_router
from public.routes import router as public_router
from contractor.routes import router as contractor_router
from auctioneer.routes import router as auctioneer_router
from admin.routes import router as admin_router

app = FastAPI(title="BDIAE Backend", version="0.1.0")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(auction_router, prefix="/auction", tags=["auction"])
app.include_router(wallet_router, prefix="/wallet", tags=["wallet"])
app.include_router(yellow_router, prefix="/yellow", tags=["yellow"])
app.include_router(chain_router, prefix="/chain", tags=["chain"])
app.include_router(settlement_router, prefix="/settlement", tags=["settlement"])
app.include_router(public_router, prefix="/public", tags=["public"])
app.include_router(contractor_router, prefix="/contractor", tags=["contractor"])
app.include_router(auctioneer_router, prefix="/auctioneer", tags=["auctioneer"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])


@app.get("/")
async def root():
	return {"ok": True, "service": "bdiae-backend"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
