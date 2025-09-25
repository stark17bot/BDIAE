@echo off
echo 🚀 Deploying BDIAE contracts to Polygon Mumbai...

REM Check if .env exists
if not exist ".env" (
    echo ❌ .env file not found. Please create one with:
    echo RPC_URL=https://rpc-mumbai.maticvigil.com
    echo PRIVATE_KEY=your_private_key_here
    echo CHAIN_ID=80001
    exit /b 1
)

REM Install Hardhat dependencies
echo 📦 Installing Hardhat dependencies...
cd contracts
call npm install

REM Compile contracts
echo 🔨 Compiling contracts...
call npx hardhat compile

REM Deploy contracts
echo 🚀 Deploying to Mumbai...
call npx hardhat run scripts/deploy.js --network mumbai

echo ✅ Deployment complete!
echo 📝 Update your backend/.env with the contract addresses shown above
