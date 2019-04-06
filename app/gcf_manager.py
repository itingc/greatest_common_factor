from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.base import Base
from app.gcf_input import GcfInput


class GcfManager:
    def __init__(self, db_filename):