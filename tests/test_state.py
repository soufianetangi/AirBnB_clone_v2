import unittest
import MySQLdb
import os
from models.state import State
from models import storage

class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            cls.db = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            cls.db.close()

    def setUp(self):
        """Set up each test"""
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Clean up after each test"""
        storage.delete(self.state)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not relevant for file storage")
    def test_create_state(self):
        """Test creating a new state"""
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        new_state = State(name="Nevada")
        new_state.save()

        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        self.assertEqual(new_count, initial_count + 1)

if __name__ == "__main__":
    unittest.main()
