from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.base import Base
from app.gcf import Gcf


class GcfManager:
    def __init__(self, db_filename):
        if db_filename is None or db_filename == "":
            raise ValueError("Invalid database file")
        engine = create_engine('sqlite:///' + db_filename)

        # Bind the engine to the metadata of the Base class so that the
        # declarative can be accessed through a DBSession instance
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)


    def add_gcf(self, gcf):
        """ Adds a new point"""
        if gcf is None or not isinstance(gcf, Gcf):
            raise ValueError("Invalid Gcf Object")
        print(f'haha {gcf.get_x()} type: {type(gcf.get_x())}')
        print(f'bbb {gcf.get_y() } type: {type(gcf.get_x())}')
        print(f'abc {gcf.calculate_gcf()} type: {type(gcf.get_x())}')
        session = self._db_session()
        session.add(gcf)
        session.commit()
        session.close()
