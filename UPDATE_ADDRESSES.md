# 📝 Update Contract Addresses

After deploying via Remix, update these files with your deployed addresses:

## Step 1: Update Frontend Web3 Service

**File:** `bdiae-ui/src/lib/web3.ts`

**Find these lines:**
```typescript
public static readonly INR_TOKEN_ADDRESS = "0x0000000000000000000000000000000000000000";
public static readonly AUCTION_ESCROW_ADDRESS = "0x0000000000000000000000000000000000000000";
```

**Replace with your deployed addresses:**
```typescript
public static readonly INR_TOKEN_ADDRESS = "0x_YOUR_INR_TOKEN_ADDRESS_HERE_";
public static readonly AUCTION_ESCROW_ADDRESS = "0x_YOUR_AUCTION_ESCROW_ADDRESS_HERE_";
```

## Step 2: Update Backend Configuration

**File:** `backend/.env`

**Add these lines:**
```env
INR_TOKEN_ADDRESS=0x_YOUR_INR_TOKEN_ADDRESS_HERE_
AUCTION_ESCROW_ADDRESS=0x_YOUR_AUCTION_ESCROW_ADDRESS_HERE_
```

## Step 3: Update Backend Config (Alternative)

**File:** `backend/core/config.py`

**Find these lines:**
```python
INR_TOKEN_ADDRESS: str = Field(default="0x0000000000000000000000000000000000000000")
AUCTION_ESCROW_ADDRESS: str = Field(default="0x0000000000000000000000000000000000000000")
```

**Replace with:**
```python
INR_TOKEN_ADDRESS: str = Field(default="0x_YOUR_INR_TOKEN_ADDRESS_HERE_")
AUCTION_ESCROW_ADDRESS: str = Field(default="0x_YOUR_AUCTION_ESCROW_ADDRESS_HERE_")
```

## Step 4: Verify Addresses

**Check on Mumbai Polygonscan:**
1. Go to https://mumbai.polygonscan.com/
2. Search your contract addresses
3. Verify they show up as "Contract" (not "Address")
4. Check the contract code matches your deployment

## Example:
```typescript
// Example addresses (replace with yours)
public static readonly INR_TOKEN_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678";
public static readonly AUCTION_ESCROW_ADDRESS = "0xabcdef1234567890abcdef1234567890abcdef12";
```
