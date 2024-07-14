import sqlalchemy
from sqlalchemy.sql import text
from pytest import fixture


@fixture
def database_connection():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    connection = engine.connect()
    yield connection
    connection.close()

def test_database_connection(database_connection):
    result = database_connection.execute(text('SELECT 1'))
    assert result.fetchone()[0] == 1