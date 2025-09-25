#!/bin/bash

# Deploy contracts to Polygon Mumbai
echo "🚀 Deploying BDIAE contracts to Polygon Mumbai..."

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create one with:"
    echo "RPC_URL=https://rpc-mumbai.maticvigil.com"
    echo "PRIVATE_KEY=your_private_key_here"
    echo "CHAIN_ID=80001"
    exit 1
fi

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Check if required vars are set
if [ -z "$RPC_URL" ] || [ -z "$PRIVATE_KEY" ]; then
    echo "❌ RPC_URL and PRIVATE_KEY must be set in .env"
    exit 1
fi

# Install Hardhat dependencies
echo "📦 Installing Hardhat dependencies..."
cd contracts
npm install

# Compile contracts
echo "🔨 Compiling contracts..."
npx hardhat compile

# Deploy contracts
echo "🚀 Deploying to Mumbai..."
npx hardhat run scripts/deploy.js --network mumbai

echo "✅ Deployment complete!"
echo "📝 Update your backend/.env with the contract addresses shown above"
