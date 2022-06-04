import unittest
import math
from dodatak_A import OperationsManager


class test_perform_division(unittest.TestCase):

    def test_integer_division1(self):
        ops_manager = OperationsManager(5, 2)
        self.assertEqual(ops_manager.perform_division(), 2.5)

    def test_integer_divison2(self):
        ops_manager = OperationsManager(6, 3)
        self.assertEqual(ops_manager.perform_division(), 2)
    
    def test_float_division1(self):
        ops_manager = OperationsManager(5.2, 2)
        self.assertEqual(ops_manager.perform_division(), 2.6)

    def test_zero_division(self):
        ops_manager = OperationsManager(5.2, 0)
        self.assertTrue(math.isnan(ops_manager.perform_division()))

    def test_value_error_division(self):
        ops_manager = OperationsManager("aa", 2)
        self.assertRaises(TypeError, lambda: ops_manager.perform_division())

    def test_type_error_division1(self):
        self.assertRaises(TypeError, lambda : OperationsManager())

    def test_type_error_division2(self):
        self.assertRaises(TypeError, lambda: OperationsManager(1))

    def test_type_error_division3(self):
        self.assertRaises(TypeError, lambda: OperationsManager(1,2,3))

    def test_correct_toFloat1(self):
        self.assertEqual(OperationsManager.toFloat("2"), 2)
    
    def test_correct_toFloat2(self):
        self.assertEqual(OperationsManager.toFloat("2.33"), 2.33)

    def test_correct_toFloat3(self):
        self.assertEqual(OperationsManager.toFloat("     2.33"), 2.33)

    def test_correct_toFloat4(self):
        self.assertEqual(OperationsManager.toFloat(True), 1)

    def test_correct_toFloat5(self):
        self.assertEqual(OperationsManager.toFloat(False), 0)

    def test_toFloat1(self):
        self.assertTrue(math.isnan(OperationsManager.toFloat("a2.33")))
    
    def test_toFloat2(self):
        self.assertTrue(math.isnan(OperationsManager.toFloat("adsd")))
    
    def test_toFloat3(self):
        self.assertTrue(math.isnan(OperationsManager.toFloat("")))

    def test_toFloat4(self):
        self.assertTrue(math.isnan(OperationsManager.toFloat(math.nan)))

    def test_toFloat5(self):
        self.assertTrue(math.isnan(OperationsManager.toFloat(None)))


if __name__ == '__main__':
    unittest.main()


