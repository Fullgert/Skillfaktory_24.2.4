import pytest


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) != 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(2, 0)

    def test_multiply_success(self):
        assert self.calc.multiply(1, 2) == 2

    def test_multiply_unsoccess(self):
        assert self.calc.multiply(1, 1) != 3

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5

    def test_division_unsoccess(self):
        assert self.calc.division(12, 3) != 3


    def teardown(self):
        print("Выполнение метода Teardown")