import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app/data/taskmanagerapi.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False