# BDIAE Deployment Guide

## 🚀 Deploy Contracts to Polygon Mumbai

### Prerequisites
1. **MetaMask Wallet** with Mumbai testnet configured
2. **Mumbai MATIC** for gas fees (get from [faucet](https://faucet.polygon.technology/))
3. **Node.js** and npm installed

### Step 1: Setup Environment

Create `backend/.env` file:
```bash
# Blockchain Configuration
RPC_URL=https://rpc-mumbai.maticvigil.com
PRIVATE_KEY=your_private_key_here
PUBLIC_ADDRESS=your_wallet_address_here
CHAIN_ID=80001

# Contract Addresses (will be filled after deployment)
INR_TOKEN_ADDRESS=
AUCTION_ESCROW_ADDRESS=

# Backend Configuration
JWT_SECRET=your_super_secret_jwt_key
JWT_ALGORITHM=HS256
DATABASE_URL=sqlite:///./dev.db
```

### Step 2: Deploy Contracts

**Windows:**
```bash
cd backend
deploy-contracts.bat
```

**Linux/Mac:**
```bash
cd backend
chmod +x deploy-contracts.sh
./deploy-contracts.sh
```

**Manual Deployment:**
```bash
cd backend/contracts
npm install
npx hardhat compile
npx hardhat run scripts/deploy.js --network mumbai
```

### Step 3: Update Environment

After deployment, copy the contract addresses to your `.env`:
```bash
INR_TOKEN_ADDRESS=0x1234...
AUCTION_ESCROW_ADDRESS=0x5678...
```

### Step 4: Start Backend

```bash
cd backend
python -m venv .venv311
.venv311\Scripts\Activate.ps1  # Windows
# source .venv311/bin/activate  # Linux/Mac

pip install -r requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 5: Start Frontend

```bash
cd bdiae-ui
npm install
npm run dev
```

## 🔧 Testing the Integration

### 1. Register Users
- Visit http://localhost:3000/register?role=contractor
- Register with email/password
- Repeat for auctioneer and admin roles

### 2. Create Auction
- Login as auctioneer
- Visit http://localhost:3000/create
- Create auction with title, type, reserve price

### 3. Place Bids
- Login as contractor
- Visit http://localhost:3000/auctions/1
- Place bids (requires INR token balance)

### 4. Finalize Auction
- Login as admin
- Call POST /auction/finalize API
- Winner selected automatically

### 5. Confirm Delivery
- Login as auctioneer
- Call POST /auction/confirm API
- Funds released to winner

## 📊 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token

### Auctions
- `POST /auction/create` - Create auction (auctioneer only)
- `POST /auction/bid` - Place bid (contractor only)
- `POST /auction/finalize` - Finalize auction (admin only)
- `POST /auction/confirm` - Confirm delivery (auctioneer only)
- `GET /auction/status` - Get auction status
- `GET /auction/bids` - Get current bids
- `GET /auction/auction` - Get current auction

### Wallet
- `GET /wallet/balance` - Get INR token balance
- `GET /wallet/transactions` - Get transaction history

## 🔐 Security Notes

1. **Never commit private keys** to version control
2. **Use environment variables** for all sensitive data
3. **Enable HTTPS** in production
4. **Validate all inputs** on both frontend and backend
5. **Use rate limiting** to prevent abuse

## 🐛 Troubleshooting

### Common Issues

**"RPC_URL not configured"**
- Ensure `.env` file exists with correct RPC_URL

**"Insufficient funds"**
- Get Mumbai MATIC from faucet
- Ensure wallet has enough gas

**"Contract not deployed"**
- Check contract addresses in `.env`
- Redeploy contracts if needed

**"Import errors"**
- Ensure virtual environment is activated
- Install all requirements: `pip install -r requirements.txt`

### Getting Help

1. Check API docs: http://localhost:8000/docs
2. View backend logs for detailed errors
3. Check browser console for frontend issues
4. Verify contract deployment on [Mumbai Explorer](https://mumbai.polygonscan.com/)

## 🚀 Production Deployment

### Backend (Render/Heroku)
1. Set environment variables in dashboard
2. Deploy from GitHub repository
3. Update frontend API URL

### Frontend (Vercel/Netlify)
1. Set `NEXT_PUBLIC_API_URL` environment variable
2. Deploy from GitHub repository
3. Update CORS settings in backend

### Database
- Use PostgreSQL in production
- Set `DATABASE_URL` to production database
- Run migrations: `alembic upgrade head`
