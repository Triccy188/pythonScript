FOLDERS = [
    'app/api',
    'app/core',
    'app/model',
    'repositories',
    'schemas',
    'services'
]

FILES = {
    'main.py': '''# Main entry point for the application
# This is the starting point of your Python script

def main():
    print("Application started successfully!")
    # Add your main logic here

if __name__ == "__main__":
    main()
''',
    'config.py': '''# Global configuration settings
# This file contains application-wide configurations

import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

# Other settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
''',
    'config/database.py': '''# Database configuration and connection setup
# This module handles database connections and settings

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
''',
    'app/__init__.py': '# App package initialization\n',
    'app/api/__init__.py': '# API layer package\n',
    'app/core/__init__.py': '# Core package\n',
    'app/model/__init__.py': '# Models package\n',
    'repositories/__init__.py': '# Repositories package\n',
    'schemas/__init__.py': '# Schemas package\n',
    'services/__init__.py': '# Services package\n',
}
