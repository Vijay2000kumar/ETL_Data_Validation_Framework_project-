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

def test_data_types(db_connection):
    # Test data types for columns 'ProductKey', 'ProductName', 'ProductCategory'
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT DATA_TYPE 
        FROM information_schema.columns 
        WHERE table_schema = %s 
        AND table_name = 'DimProduct'
        AND column_name IN ('ProductKey', 'ProductName', 'ProductCategory')
    """, ('etldb',))
    expected_data_types = ['int', 'varchar', 'varchar']  # Assuming data types for each column
    actual_data_types = [row[0] for row in cursor.fetchall()]
    print("Actual Data Types:", actual_data_types)  # Print the actual data types
    assert actual_data_types == expected_data_types
