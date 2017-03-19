import pytest
import csv
from tax_caculator import TaxCaculator



# get data from csv to test on dataset
@pytest.fixture
def get_test_data():
    csvfile = open('Data.csv', 'rb')
    reader = csv.reader(csvfile)
    r = []
    for row in reader:
        test_input = int(row[0])
        test_output = int(row[1])
        r.append((test_input, test_output))
    return r


class TestUsingData:
    @pytest.mark.parametrize("test_input, test_expected", get_test_data())
    def testTaxCalculatorWayOne(self, test_input, test_expected):
        tax = TaxCaculator()
        tax.set_income(test_input)
        result = tax.calculate_income_1()
        assert result == test_expected


    @pytest.mark.parametrize("test_input, test_expected", get_test_data())
    def testTaxCalculatorWayTwo(self, test_input, test_expected):
        tax = TaxCaculator()
        tax.set_income(test_input)
        result = tax.calculate_income_2()
        assert result == test_expected