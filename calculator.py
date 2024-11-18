class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return -b + a

    def multiply(self, a, b):
        result = 0
        if(b < 0):
            for i in range(-b):
                result = self.add(result, -a)
        else:
            for i in range(b):
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        neg_result_divide = (a < 0) ^ (b < 0)
        if(a < 0):
            a = -a
        if(b < 0):
            b = -b
        while a >= b:
            a -= b 
            result += 1
        if(neg_result_divide):
            return -result
        else:
            return result
    
    def modulo(self, a, b):
        neg_result_modulo = (a < 0) ^ (b < 0)
        if(a < 0):
            a = -a
        if(b < 0):
            b = -b
        while a >= b:
            a = a-b
        if(neg_result_modulo):
            return -a
        else:
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))