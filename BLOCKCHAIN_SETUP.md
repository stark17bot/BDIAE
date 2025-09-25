# 🚀 Blockchain Integration Setup Guide

## ✅ **What's Implemented:**

### **Smart Contracts:**
- ✅ **INR Token** - ERC20 token with 10% platform fee
- ✅ **Auction Escrow** - Handles bidding, escrow, and automatic winner selection
- ✅ **Mumbai Testnet** - Configured for Polygon Mumbai

### **Frontend Integration:**
- ✅ **MetaMask Connection** - Connect/disconnect wallet
- ✅ **Web3 Service** - Handle blockchain transactions
- ✅ **Real Bidding** - Place bids directly on blockchain
- ✅ **Token Balance** - Display INR token balance

### **Backend Integration:**
- ✅ **Blockchain Services** - Real Web3 integration
- ✅ **JWT Verification** - Supabase authentication
- ✅ **Database Storage** - SQLite for auction data

---

## 🛠️ **Setup Instructions:**

### **Step 1: Install Contract Dependencies**
```bash
cd contracts
npm install
```

### **Step 2: Configure Environment**
Create `contracts/.env`:
```env
PRIVATE_KEY=your_metamask_private_key_here
POLYGONSCAN_API_KEY=your_polygonscan_api_key_here
```

### **Step 3: Deploy Contracts**
```bash
npm run deploy
```

This will deploy:
- INR Token contract
- Auction Escrow contract
- Mint 100,000 INR tokens to your address

### **Step 4: Update Contract Addresses**
After deployment, update these files:
- `bdiae-ui/src/lib/web3.ts` - Update contract addresses
- `backend/.env` - Add contract addresses

### **Step 5: Environment (Amoy)**

Create backend/.env (NitroLite / Yellow):
```
RPC_URL=https://rpc.nitrolite.yellow.org
CHAIN_ID=7824
PRIVATE_KEY=0x<nitro_private_key>
INR_TOKEN_ADDRESS=0x<deployed_INR>
AUCTION_ESCROW_ADDRESS=0x<deployed_EscrowManager>
FEE_TREASURY=0x<your_fee_treasury>
SETTLEMENT_SIGNER=0x<address_of_PRIVATE_KEY>
```

### **Step 6: Start the Application**

**Backend:**
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --host 127.0.0.1 --port 8000
```

**Frontend:**
```bash
cd bdiae-ui
npm run dev
```

---

## 🔧 **How It Works:**

### **Auction Creation:**
1. **Auctioneer connects MetaMask**
2. **Creates auction on blockchain** → Smart contract deployed
3. **Stores metadata in database** → SQLite for UI display

### **Bidding Process:**
1. **Contractor connects MetaMask**
2. **Places bid on blockchain** → Tokens escrowed in contract
3. **Previous bidder refunded** → Automatic token transfer
4. **Bid stored in database** → For tracking and display

### **Auction Finalization:**
1. **Auction ends** → Time-based automatic finalization
2. **Winner selected** → Highest bidder wins
3. **10% platform fee** → Automatically deducted
4. **90% to auctioneer** → Tokens transferred
5. **Transaction logged** → All details stored

---

## 💰 **Token Economics:**

- **INR Token** - ERC20 token for bidding
- **10% Platform Fee** - Automatically deducted from winning bid
- **Escrow System** - Tokens locked during auction
- **Automatic Refunds** - Previous bidders get refunded

---

## 🧪 **Testing:**

1. **Get Mumbai MATIC** - Use Mumbai faucet
2. **Connect MetaMask** - Switch to Mumbai testnet
3. **Create Auction** - Deploy auction contract
4. **Place Bids** - Test bidding with different accounts
5. **Finalize Auction** - Test automatic winner selection

---

## 📋 **Contract Addresses:**
*Update these after deployment:*

- **INR Token:** `0x...` (Update in web3.ts)
- **Auction Escrow:** `0x...` (Update in web3.ts)

---

## 🚨 **Important Notes:**

- **Mumbai Testnet Only** - No real money involved
- **MetaMask Required** - For all blockchain interactions
- **Gas Fees** - Paid in MATIC (testnet)
- **Private Keys** - Keep secure, use test accounts only

---

**Ready to deploy and test! 🚀**
