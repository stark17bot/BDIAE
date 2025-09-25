from db.database import SessionLocal
from db.models import User, UserRole, Auction, AuctionStatus, AuctionType
from auth.utils import hash_password

def create_test_users():
    db = SessionLocal()
    try:
        # Create test users
        test_users = [
            {'email': 'contractor@test.com', 'password': 'password123', 'role': UserRole.contractor},
            {'email': 'auctioneer@test.com', 'password': 'password123', 'role': UserRole.auctioneer},
            {'email': 'admin@test.com', 'password': 'password123', 'role': UserRole.admin}
        ]
        
        for user_data in test_users:
            existing = db.query(User).filter(User.email == user_data['email']).first()
            if not existing:
                user = User(
                    email=user_data['email'],
                    password_hash=hash_password(user_data['password']),
                    role=user_data['role']
                )
                db.add(user)
                print(f'Created user: {user_data["email"]} ({user_data["role"]})')
            else:
                print(f'User already exists: {user_data["email"]}')
        
        db.commit()

        # Create demo auctions for the auctioneer
        auctioneer = db.query(User).filter(User.email == 'auctioneer@test.com').first()
        if auctioneer:
            existing = db.query(Auction).filter(Auction.creator_id == auctioneer.id).count()
            if existing == 0:
                demo_auctions = [
                    Auction(
                        title='Sealed Bid - Radar Components',
                        description='Procurement of RAD-200 modules',
                        type=AuctionType.sealed,
                        reserve_price=1000,
                        creator_id=auctioneer.id,
                        status=AuctionStatus.upcoming,
                    ),
                    Auction(
                        title='Reverse - Armored Vehicle Parts',
                        description='Brake assemblies',
                        type=AuctionType.reverse,
                        reserve_price=500,
                        creator_id=auctioneer.id,
                        status=AuctionStatus.live,
                    ),
                ]
                for a in demo_auctions:
                    db.add(a)
                db.commit()
                print('Created demo auctions for auctioneer')

        print('Test users and demo data created successfully!')
    finally:
        db.close()

if __name__ == "__main__":
    create_test_users()


