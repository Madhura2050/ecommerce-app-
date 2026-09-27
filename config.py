import os

class Config:
    SECRET_KEY = 'super-secret-key-12345'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SESSION_TYPE = 'filesystem'