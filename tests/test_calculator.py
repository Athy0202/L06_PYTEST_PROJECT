from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
        
    def test_subtract(self):
        # Arrange
        a = 10
        b = 5
        expected_result = 5

        # Act
        result = self.calc.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_result)
        
    def test_multiply(self):
        # Arrange
        a = 10
        b = 5
        expected_result = 50

        # Act
        result = self.calc.multiply(a, b)

        # Assert
        self.assertEqual(result, expected_result)
        
    def test_divide(self):
        # Arrange
        a = 10
        b = 5
        expected_result = 2

        # Act
        result = self.calc.divide(a, b)

        # Assert
        self.assertEqual(result, expected_result)
