# BDIAE Backend (FastAPI + Web3.py)

## Setup
1. Python 3.11+
2. Install deps:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Create `.env` in `backend/`:
   ```env
   RPC_URL="https://rpc-mumbai.maticvigil.com"
   PRIVATE_KEY="your-private-key"
   PUBLIC_ADDRESS="0xyouraddress"
   CHAIN_ID=80001
   INR_TOKEN_ADDRESS="0x..."
   AUCTION_ESCROW_ADDRESS="0x..."
   JWT_SECRET="supersecret"
   JWT_ALGORITHM="HS256"
   DATABASE_URL="sqlite:///./dev.db"
   ```

## Run
```bash
uvicorn backend.main:app --reload
```

## API
- Auth: `/auth/register`, `/auth/login`
- Auction: `/auction/create`, `/auction/bid`, `/auction/finalize`, `/auction/confirm`
- Wallet: `/wallet/balance`, `/wallet/transactions`

## Contracts
- `contracts/INRToken.sol` (ERC20 Mock with mint)
- `contracts/AuctionEscrow.sol` (auction + escrow)
- Compile with Hardhat/Foundry and place ABIs in `contracts/abis/` named `INRToken.json`, `AuctionEscrow.json`.

## Testing
```bash
pytest -q backend/tests
```

## Deploy
- Build container and deploy to Render/Heroku.
- Configure environment variables securely.

## Notes
- Service layer uses fallback ABIs until compiled ABIs are provided.
- Role-based access enforced via JWT claims.
