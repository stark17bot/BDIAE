#!/usr/bin/env python3
"""
Test script to verify contract deployment and connection
"""
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_contract_deployment():
    # Get configuration from .env
    rpc_url = os.getenv("RPC_URL")
    inr_token_address = os.getenv("INR_TOKEN_ADDRESS")
    auction_escrow_address = os.getenv("AUCTION_ESCROW_ADDRESS")
    
    print("🔍 Testing Contract Deployment...")
    print(f"RPC URL: {rpc_url}")
    print(f"INR Token Address: {inr_token_address}")
    print(f"Auction Escrow Address: {auction_escrow_address}")
    
    if not rpc_url or not inr_token_address:
        print("❌ Missing required environment variables!")
        return False
    
    try:
        # Connect to Polygon Mumbai
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not w3.is_connected():
            print("❌ Failed to connect to Polygon Mumbai!")
            return False
        
        print("✅ Connected to Polygon Mumbai!")
        
        # Get latest block
        latest_block = w3.eth.block_number
        print(f"📦 Latest block: {latest_block}")
        
        # Check if INR Token contract exists
        if inr_token_address and inr_token_address != "":
            try:
                code = w3.eth.get_code(inr_token_address)
                if code == b'':
                    print("❌ INR Token contract not found at address!")
                else:
                    print("✅ INR Token contract found!")
            except Exception as e:
                print(f"❌ Error checking INR Token: {e}")
        
        # Check if Auction Escrow contract exists
        if auction_escrow_address and auction_escrow_address != "":
            try:
                code = w3.eth.get_code(auction_escrow_address)
                if code == b'':
                    print("❌ Auction Escrow contract not found at address!")
                else:
                    print("✅ Auction Escrow contract found!")
            except Exception as e:
                print(f"❌ Error checking Auction Escrow: {e}")
        else:
            print("⚠️  Auction Escrow address not set in .env")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_contract_deployment()
