import pytest
#from ..src.db_connection import connect_to_db, close_connection
#from etl_auto_framwork.db_conn import connect_to_db, close_connection
import sys
sys.path.append('C:\\Users\\Techment\\PycharmProjects\\ETL_Project03')  # Replace '/path/to/rootfile' with the actual path
from etl_auto_framwork.utilities.db_conn import connect_to_db, close_connection
@pytest.fixture(scope="module")
def db_connection():
    # Establishing a connection to the database
    conn = connect_to_db()
    yield conn
    # Closing the connection after all tests are done
    close_connection(conn)

def test_accuracy(db_connection):
    # Test for accuracy: Check if ProductName column has accurate values
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM etldb.DimProduct
        WHERE ProductName IN ('Product A', 'Product B', 'Product C')
    """)
    result = cursor.fetchone()
    assert result[0] == 3