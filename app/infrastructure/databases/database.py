from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def create_session(self):
        return self.Session()

    def add(self, entity):
        session = self.create_session()
        session.add(entity)
        session.close()

    def commit(self):
        session = self.create_session()
        session.commit()
        session.close()

    def delete(self, entity):
        session = self.create_session()
        session.delete(entity)
        session.close()

    def query(self, entity_class):
        session = self.create_session()
        query = session.query(entity_class)
        session.close()
        return query


def get_session():
    database = Database("sqlite:///sqlite3.db")
    return database.create_session()
