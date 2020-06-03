import unittest
import guess_number

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

    def test_correct_number_returns_right_answer(self):
        correct_inserted_num = 5
        number_to_find = 5
        num_of_tries = 1
        intent = guess_number.check_number(
            correct_inserted_num, number_to_find, num_of_tries)
        self.assertTrue(intent["result"])
        self.assertEqual(intent["message"], guess_number.correct_answer_txt)

    def test_high_number_returns_wrong_answer(self):
        too_high_inserted_num = 6
        number_to_find = 5
        num_of_tries = 1
        intent = guess_number.check_number(
            too_high_inserted_num, number_to_find, num_of_tries)
        self.assertFalse(intent["result"])
        self.assertEqual(intent["message"],
                         guess_number.incorrect_answer_too_high_txt)

    def test_low_number_returns_wrong_answer(self):
        too_low_inserted_num = 4
        number_to_find = 5
        num_of_tries = 1
        intent = guess_number.check_number(
            too_low_inserted_num, number_to_find, num_of_tries)
        self.assertFalse(intent["result"])
        self.assertEqual(intent["message"],
                         guess_number.incorrect_answer_too_low_txt)

    def test_not_valid_input(self):
        non_valid_input = "This is not a valid number"
        input_check = guess_number.convert_user_input(non_valid_input)
        self.assertFalse(input_check)

    def test_valid_input(self):
        valid_input = 5
        input_check = guess_number.convert_user_input(valid_input)
        self.assertTrue(input_check)

    def test_exit_input(self):
        exit_input = "exit"
        exit_msg = guess_number.exit_msg
        with self.assertRaises(SystemExit) as cm:
            guess_number.convert_user_input(exit_input)
        self.assertEqual(cm.exception.code, exit_msg)


# With the below function we can run the tests with 'python test_guess_number.py'
# Without this function we would have to do 'python -m unittest test_guess_number.py'
if __name__ == '__main__':
    unittest.main()
