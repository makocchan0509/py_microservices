
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.customer import customer_cmd

class customerCmdTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_all_variable(self):
        name = "test"
        address = "sonohen"
        email = "xxx@xxx"
        result = customer_cmd.CustomerCommand(name,address,email)
        self.assertEqual(name,result.customer_name)
        self.assertEqual(address,result.address)
        self.assertEqual(email,result.email)

if __name__ == "__main__":
    unittest.main()