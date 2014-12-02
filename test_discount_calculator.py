import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def testExampleDiscount(self):
        discount = calculate_discount(200, 10, 30)
        expected_outcome = 150
        self.assertEqual(discount, expected_outcome)

    def testNegativeCost(self):
        with self.assertRaises(ValueError):
            discount = calculate_discount(-200, 10, 30)

    def testNegativePercent(self):
        with self.assertRaises(ValueError):
            discount = calculate_discount(200, -10, 30)

    def testNegativeAbsolute(self):
        with self.assertRaises(ValueError):
            discount = calculate_discount(200, 10, -30)

    def testZeroRelative(self):
        discount = calculate_discount(200, 0, 30)
        expected_outcome = 170
        self.assertEqual(discount, expected_outcome)

    def testZeroAbsolute(self):
        """Zero absolute discount is allowed """
        discount = calculate_discount(200, 10, 0)
        expected_outcome = 180
        self.assertEqual(discount, expected_outcome)

    def testNotZero(self):
        """Discounts should return lowest_cost not 0 """
        discount = calculate_discount(20, 10, 18)
        self.assertNotEqual(discount, 0.0)

    def testNotBelowZero(self):
        """Discounts should return lowest_cost when discount is over 90% """
        discount = calculate_discount(20, 10, 20)
        lowest_cost = 2
        self.assertEqual(discount, lowest_cost)


if __name__ == "__main__":
    unittest.main()
