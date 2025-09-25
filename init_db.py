#!/usr/bin/env python3
"""
Database initialization script for BDIAE backend
"""

from db.database import engine, Base
from db.models import User, Auction, Bid, TxLog, Dispute, AuditLog, Notification
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    """Create all database tables"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully!")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

if __name__ == "__main__":
    init_db()
