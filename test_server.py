#!/usr/bin/env python3
"""
Test script to verify the FastAPI server works
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("Starting FastAPI server...")
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    except Exception as e:
        print(f"Error starting server: {e}")
        import traceback
        traceback.print_exc()
