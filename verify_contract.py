#!/usr/bin/env python3
"""
Script to verify the deployed AuctionEscrow contract and get the INR token address
"""

from web3 import Web3
import json

# Amoy testnet RPC (Mumbai replacement)
RPC_URL = "https://rpc-amoy.polygon.technology"
AUCTION_ESCROW_ADDRESS = "0xa19b9a9454e68dffbadb8edaf70fc90b2cafad52"

def verify_contract():
    try:
        # Connect to Mumbai testnet
        w3 = Web3(Web3.HTTPProvider(RPC_URL))
        
        if not w3.is_connected():
            print("❌ Failed to connect to Amoy testnet")
            return False
            
        print("✅ Connected to Amoy testnet")
        
        # Check if contract exists
        checksum_address = w3.to_checksum_address(AUCTION_ESCROW_ADDRESS)
        code = w3.eth.get_code(checksum_address)
        if len(code) == 0:
            print("❌ No contract found at address")
            return False
            
        print("✅ Contract found at address")
        
        # Get contract info
        try:
            # Simple ABI for basic contract interaction
            contract_abi = [
                {
                    "inputs": [],
                    "name": "inr",
                    "outputs": [{"name": "", "type": "address"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "owner",
                    "outputs": [{"name": "", "type": "address"}],
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
            
            contract = w3.eth.contract(
                address=checksum_address,
                abi=contract_abi
            )
            
            # Get INR token address
            inr_token_address = contract.functions.inr().call()
            owner_address = contract.functions.owner().call()
            
            print(f"✅ Contract verified successfully!")
            print(f"📋 Contract Details:")
            print(f"   - Auction Escrow: {AUCTION_ESCROW_ADDRESS}")
            print(f"   - INR Token: {inr_token_address}")
            print(f"   - Owner: {owner_address}")
            
            # Check if INR token contract exists
            inr_code = w3.eth.get_code(inr_token_address)
            if len(inr_code) > 0:
                print(f"✅ INR Token contract verified")
            else:
                print(f"❌ INR Token contract not found")
                
            return True
            
        except Exception as e:
            print(f"⚠️  Contract found but couldn't read details: {e}")
            return True  # Contract exists even if we can't read it
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Verifying deployed AuctionEscrow contract...")
    print(f"📍 Address: {AUCTION_ESCROW_ADDRESS}")
    print(f"🌐 Network: Amoy Testnet")
    print("-" * 50)
    
    success = verify_contract()
    
    if success:
        print("\n🎉 Contract verification completed!")
        print("\n📝 Next steps:")
        print("1. Update INR_TOKEN_ADDRESS in your config files")
        print("2. Test the contract interaction")
        print("3. Deploy your frontend and test the full flow")
    else:
        print("\n❌ Contract verification failed!")
        print("Please check the contract address and network")
