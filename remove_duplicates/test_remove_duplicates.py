import unittest
import remove_duplicates

# IMPORTANT:
# All test functions must start with test_
# unittest Assertion Methods: https://docs.python.org/3/library/unittest.html#assert-methods


class GuessNumber(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use setUpClass to run code at the beginning of the test Suite
        pass

    @classmethod
    def tearDownClass(cls):
        # Use tearDownClass to run code at the end of the test Suite
        pass

    def setUp(self):
        # Use setUp function to run code before each test case
        pass

    def tearDown(self):
        # Use setUp function to run code after each test case
        pass

    def test_if_duplicats_are_removed_part_1(self):
        given_arr = [1, 2, 3, 2, 3, 4, 5, 9, 9, 9, 9]
        solution_arr = [1, 2, 3, 4, 5, 9]
        handled_arr = remove_duplicates.clean2(given_arr)
        handled_arr.sort()
        self.assertEqual(solution_arr,
                         handled_arr)

    def test_if_duplicats_are_removed_part_2(self):
        given_arr = [9, 2, 1, 2, 3, 2, 3, 4, 5, 9, 9, 9, 9]
        solution_arr = [1, 2, 3, 4, 5, 9]
        handled_arr = remove_duplicates.clean2(given_arr)
        handled_arr.sort()
        self.assertEqual(solution_arr,
                         handled_arr)

    def test_if_duplicats_are_removed_part_3(self):
        given_arr = ["banana", "cherries", "tomato", "banana"]
        solution_arr = ["banana", "cherries", "tomato"]
        handled_arr = remove_duplicates.clean2(given_arr)
        handled_arr.sort()
        self.assertEqual(solution_arr,
                         handled_arr)

        # With the below function we can run the tests with 'python test_guess_number.py'
        # Without this function we would have to do 'python -m unittest test_guess_number.py'
if __name__ == '__main__':
    unittest.main()
