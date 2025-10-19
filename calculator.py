class Operation:
    def execute(self, a, b):
        raise NotImplementedError()

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b

class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.execute(a, b)

if __name__ == "__main__":
    a, b = 10, 5
    calc = Calculator(Add())
    print(f"{a} + {b} = {calc.calculate(a, b)}")
    calc.operation = Subtract()
    print(f"{a} - {b} = {calc.calculate(a, b)}")
    calc.operation = Multiply()
    print(f"{a} * {b} = {calc.calculate(a, b)}")
    calc.operation = Divide()
    print(f"{a} / {b} = {calc.calculate(a, b)}")
