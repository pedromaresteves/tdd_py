import unittest
import into_roman

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

    def test_0(self):
        result = into_roman.convert_to_roman(0)
        self.assertFalse(result)
    def test_1(self):
        result = into_roman.convert_to_roman(1)
        self.assertEqual(result, "I")
    def test_2(self):
        result = into_roman.convert_to_roman(2)
        self.assertEqual(result, "II")
    def test_3(self):
        result = into_roman.convert_to_roman(3)
        self.assertEqual(result, "III")
    def test_4(self):
        result = into_roman.convert_to_roman(4)
        self.assertEqual(result, "IV")
    def test_5(self):
        result = into_roman.convert_to_roman(5)
        self.assertEqual(result, "V")
    def test_6(self):
        result = into_roman.convert_to_roman(6)
        self.assertEqual(result, "VI")
    def test_7(self):
        result = into_roman.convert_to_roman(7)
        self.assertEqual(result, "VII")
    def test_8(self):
        result = into_roman.convert_to_roman(8)
        self.assertEqual(result, "VIII")
    def test_9(self):
        result = into_roman.convert_to_roman(9)
        self.assertEqual(result, "IX")
    def test_10(self):
        result = into_roman.convert_to_roman(10)
        self.assertEqual(result, "X")
    def test_11(self):
        result = into_roman.convert_to_roman(11)
        self.assertEqual(result, "XI")
    def test_12(self):
        result = into_roman.convert_to_roman(12)
        self.assertEqual(result, "XII")
    def test_13(self):
        result = into_roman.convert_to_roman(13)
        self.assertEqual(result, "XIII")
    def test_14(self):
        result = into_roman.convert_to_roman(14)
        self.assertEqual(result, "XIV")
    def test_15(self):
        result = into_roman.convert_to_roman(15)
        self.assertEqual(result, "XV")
    def test_16(self):
        result = into_roman.convert_to_roman(16)
        self.assertEqual(result, "XVI")
    def test_17(self):
        result = into_roman.convert_to_roman(17)
        self.assertEqual(result, "XVII")
    def test_18(self):
        result = into_roman.convert_to_roman(18)
        self.assertEqual(result, "XVIII")
    def test_19(self):
        result = into_roman.convert_to_roman(19)
        self.assertEqual(result, "XIX")
    def test_20(self):
        result = into_roman.convert_to_roman(20)
        self.assertEqual(result, "XX")
    def test_30(self):
        result = into_roman.convert_to_roman(30)
        self.assertEqual(result, "XXX")
    def test_40(self):
        result = into_roman.convert_to_roman(40)
        self.assertEqual(result, "XL")
    def test_50(self):
        result = into_roman.convert_to_roman(50)
        self.assertEqual(result, "L")
    def test_60(self):
        result = into_roman.convert_to_roman(60)
        self.assertEqual(result, "LX")
    def test_70(self):
        result = into_roman.convert_to_roman(70)
        self.assertEqual(result, "LXX")
    def test_80(self):
        result = into_roman.convert_to_roman(80)
        self.assertEqual(result, "LXXX")
    def test_90(self):
        result = into_roman.convert_to_roman(90)
        self.assertEqual(result, "XC")
    def test_100(self):
        result = into_roman.convert_to_roman(100)
        self.assertEqual(result, "C")
    def test_200(self):
        result = into_roman.convert_to_roman(200)
        self.assertEqual(result, "CC")
    def test_300(self):
        result = into_roman.convert_to_roman(300)
        self.assertEqual(result, "CCC")
    def test_400(self):
        result = into_roman.convert_to_roman(400)
        self.assertEqual(result, "CD")
    def test_500(self):
        result = into_roman.convert_to_roman(500)
        self.assertEqual(result, "D")
    def test_600(self):
        result = into_roman.convert_to_roman(600)
        self.assertEqual(result, "DC")
    def test_700(self):
        result = into_roman.convert_to_roman(700)
        self.assertEqual(result, "DCC")
    def test_800(self):
        result = into_roman.convert_to_roman(800)
        self.assertEqual(result, "DCCC")
    def test_900(self):
        result = into_roman.convert_to_roman(900)
        self.assertEqual(result, "CM")
    def test_1000(self):
        result = into_roman.convert_to_roman(1000)
        self.assertEqual(result, "M")
    def test_2000(self):
        result = into_roman.convert_to_roman(2000)
        self.assertEqual(result, "MM")
    def test_1111(self):
        result = into_roman.convert_to_roman(1111)
        self.assertEqual(result, "MCXI")
    def test_4444(self):
        result = into_roman.convert_to_roman(4444)
        self.assertEqual(result, "MMMMCDXLIV")
    def test_9999(self):
        result = into_roman.convert_to_roman(9999)
        self.assertEqual(result, "MMMMMMMMMCMXCIX")
    def test_1984(self):
        result = into_roman.convert_to_roman(1984)
        self.assertEqual(result, "MCMLXXXIV")



# With the below function we can run the tests with 'python test_guess_number.py'
# Without this function we would have to do 'python -m unittest test_guess_number.py'
if __name__ == '__main__':
    unittest.main()
