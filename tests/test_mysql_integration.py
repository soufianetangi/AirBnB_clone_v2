import unittest
import MySQLdb

class TestMySQLIntegration(unittest.TestCase):

    def setUp(self):
        # Connect to MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test",
                                  passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close connection
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        # Get initial count of states
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        # Execute command to create a new state (simulated)
        # Example: subprocess.run(['echo', 'create State name="California" | ./console.py'])
        # Or call a function that executes this command

        # Get count of states after creation
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        final_count = self.cursor.fetchone()[0]

        # Assert that one state was added
        self.assertEqual(final_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()
