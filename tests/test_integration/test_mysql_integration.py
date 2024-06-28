# tests/test_integration/test_mysql_integration.py

import unittest
import MySQLdb

# Replace with actual credentials for your MySQL database
DB_USER = 'hbnb_test'
DB_PASSWORD = 'hbnb_test_pwd'
DB_HOST = 'localhost'
DB_NAME = 'hbnb_test_db'

class TestMySQLIntegration(unittest.TestCase):
    def setUp(self):
        # Initialize MySQL connection and cursor
        self.connection = MySQLdb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        self.cursor = self.connection.cursor()

        # Ensure states table is empty before each test
        self.cursor.execute("DELETE FROM states")
        self.connection.commit()

    def tearDown(self):
        # Close cursor and connection after each test
        self.cursor.close()
        self.connection.close()

    def test_create_state(self):
        initial_count = self.get_states_count()

        # Execute command to create a new state
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()

        updated_count = self.get_states_count()
        self.assertEqual(updated_count, initial_count + 1)

    def get_states_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()
