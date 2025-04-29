class Config:
    """Base configuration."""
    SECRET_KEY = "supersecretkey"  # Change this for production
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = "sqlite:///development.db"  # Exemple


class ProductionConfig(Config):
    """Production configuration."""
    DATABASE_URI = "sqlite:///production.db"  # Exemple


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DATABASE_URI = "sqlite:///test.db"  # Exemple
