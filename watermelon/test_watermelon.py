import unittest
import watermelon

#IMPORTANT:
#All test functions must start with test_
#unittest Assertion Methods: https://docs.python.org/3/library/unittest.html#assert-methods


class TestWatermelon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Use setUpClass to run code at the beginning of the test Suite
        pass
  
    @classmethod
    def tearDownClass(cls):
        #Use tearDownClass to run code at the end of the test Suite
        pass

    def setUp(self):
        #Use setUp function to run code before each test case
        pass
  
    def tearDown(self):
        #Use setUp function to run code after each test case
        pass

    def test_one(self):
        result = watermelon.divide(1)
        self.assertEqual(result, True, 'Result should be True')

#With the below function we can run the tests with 'python test_watermelon.py'
#Without this function we would have to do 'python -m unittest test_watermelon.py'
if __name__ == '__main__':
    unittest.main()