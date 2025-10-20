import psycopg
from data_provider import DataProvider
from db_logic.
class RawSQLProvider(DataProvider):
    connection = None

    @staticmethod
    def connect():
        if not RawSQLProvider.connection or RawSQLProvider.connection.closed:
            print("Creating new connection")
            RawSQLProvider.connection = psycopg.connect("dbname=console-app user=postgres password=postgres")
            return RawSQLProvider.connection

    @staticmethod
    def create_table():
        with RawSQLProvider.connection() as coon:

