class TaxCaculator:
    def __init__(self):
        self.percentage = [5, 10, 15, 20, 25, 30, 35]
        self.w1_const1 = [0, 0.25, 0.75, 1.95, 4.75, 9.75, 18.15]
        self.w1_const2 = [0, 5, 10, 18, 32, 52, 80]
        self.w2_const = [0, 0.25, 0.75, 1.65, 3.25, 5.85, 9.85]
        self.state = 0
        self.income = 0

    def set_income(self, income):
        assert type(income) == int
        assert income > 0
        income = float(income)/1000000
        self.income = income
        if income <= 5:
            self.state = 1
        elif income > 5 and income <= 10:
            self.state = 2
        elif income > 10 and income <= 18:
            self.state = 3
        elif income > 18 and income <= 32:
            self.state = 4
        elif income > 32 and income <= 52:
            self.state = 5
        elif income > 52 and income <= 80:
            self.state = 6
        elif income > 80:
            self.state = 7
        assert self.state != 0

    def calculate_income_1(self):
        tax = 0
        income = self.income
        tax+= self.w1_const1[self.state-1]
        income-= self.w1_const2[self.state - 1]
        if (income < 0):
            income = 0
        tax += income*(float(self.percentage[self.state-1])/100)
        assert tax > 0
        return int(tax*1000000)

    def calculate_income_2(self):
        tax = 0
        income = self.income
        tax += income*(float(self.percentage[self.state-1])/100)
        tax -= self.w2_const[self.state-1]
        assert tax > 0
        return int(tax*1000000)

