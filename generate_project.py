import os

def create_project(base_path):
    # Create folders
    folders = [
        'app/api',
        'app/core',
        'app/model',
        'repositories',
        'schemas',
        'services'
    ]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Create and populate files with standard boilerplate content
    files = {
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

# Database URL - can be overridden by environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
''',
        'app/__init__.py': '''# App package initialization
''',
        'app/api/__init__.py': '''# API layer package
# This layer handles external interfaces (though not HTTP in this script)
''',
        'app/core/__init__.py': '''# Core package
# Contains core business logic and utilities
''',
        'app/model/__init__.py': '''# Models package
# Contains data models and database schemas
''',
        'repositories/__init__.py': '''# Repositories package
# Data access layer for interacting with data sources
''',
        'schemas/__init__.py': '''# Schemas package
# Contains data validation and serialization schemas
''',
        'services/__init__.py': '''# Services package
# Business logic layer
'''
    }

    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    project_name = input("Enter the name for your new project: ")
    base_path = os.path.join(os.getcwd(), project_name)
    create_project(base_path)
    print(f"Project '{project_name}' created successfully at {base_path}")
    print("Folders created: app/api, app/core, app/model, repositories, schemas, services")
    print("Files populated with standard boilerplate code.")