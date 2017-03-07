import pytest
from tax_caculator import TaxCaculator

def test_1():
    tax = TaxCaculator()
    tax.set_income(3000000)
    result = tax.calculate_income_2()
    assert result == 150000

def test_1_boundary():
    tax = TaxCaculator()
    tax.set_income(5000000)
    result = tax.calculate_income_2()
    assert result == 250000

def test_2():
    tax = TaxCaculator()
    tax.set_income(7000000)
    result = tax.calculate_income_2()
    assert result == 450000

def test_2_boundary():
    tax = TaxCaculator()
    tax.set_income(10000000)
    result = tax.calculate_income_2()
    assert result == 750000

def test_3():
    tax = TaxCaculator()
    tax.set_income(12000000)
    result = tax.calculate_income_2()
    assert result == 1050000

def test_3_boundary():
    tax = TaxCaculator()
    tax.set_income(18000000)
    result = tax.calculate_income_2()
    assert result == 1950000

def test_4():
    tax = TaxCaculator()
    tax.set_income(19000000)
    result = tax.calculate_income_2()
    assert result == 2150000

def test_4_boundary():
    tax = TaxCaculator()
    tax.set_income(32000000)
    result = tax.calculate_income_2()
    assert result == 4750000

def test_5():
    tax = TaxCaculator()
    tax.set_income(35000000)
    result = tax.calculate_income_2()
    assert result == 5500000

def test_5_boundary():
    tax = TaxCaculator()
    tax.set_income( 52000000)
    result = tax.calculate_income_2()
    assert result == 9750000

def test_6():
    tax = TaxCaculator()
    tax.set_income(55000000)
    result = tax.calculate_income_2()
    assert result == 10650000

def test_6_boundary():
    tax = TaxCaculator()
    tax.set_income(80000000)
    result = tax.calculate_income_2()
    assert result == 18150000

def test_7():
    tax = TaxCaculator()
    tax.set_income(120000000)
    result = tax.calculate_income_2()
    assert result == 32150000
