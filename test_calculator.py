import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add_1(self):
        self.assertEqual(self.calc.add(2, 4), 6)
    
    def test_add_2(self):
        self.assertEqual(self.calc.add(-2, -4), -6)
    
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(2, 4), -2)
    
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    
    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
    
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
    
    def test_divide_2(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(2, 1), 0)
    
    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
    
    


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()