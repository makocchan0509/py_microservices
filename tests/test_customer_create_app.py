from unittest import TestCase
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.customer import customer_create_app

class testCustomerCreateApp(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normal_case(self):
        mock = MagicMock()
        mock.return_value = 

if __name__ == "__main__":
