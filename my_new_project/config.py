# Global configuration settings
# This file contains application-wide configurations

import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

# Other settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
