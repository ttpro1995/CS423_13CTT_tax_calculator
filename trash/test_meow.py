import pytest
import csv

@pytest.fixture
def get_test_data():
    csvfile = open('Data.csv', 'rb')
    reader = csv.reader(csvfile)
    r = []
    for row in reader:
        test_input = row[0]
        test_output = row[1]
        r.append((test_input, test_output))
    return r

@pytest.fixture
def data():
    return ["meow", "woof"]
class TestMeow:
    @pytest.mark.parametrize("test_input", get_test_data())
    def test_print(self, test_input):
        print (test_input, "meow")