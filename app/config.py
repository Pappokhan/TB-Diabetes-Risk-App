import os

class Config:
    SECRET_KEY = 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///predictions.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
