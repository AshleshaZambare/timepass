# @pytest.mark.smoke
# @pytest.mark.xfail
# @pytest.mark.skip
import pytest


def test_sum_two_numbers(setup1):
    a = 3
    b = 4
    print("sum = ", a+b)

@pytest.mark.usefixtures("setup1")
class Test_test_two:
    def test_sample(self):
        print("In method sample")

    def test_sample2(self):
        print("In method sample2")

    def test_sample3(self):
        print("In sample3")

