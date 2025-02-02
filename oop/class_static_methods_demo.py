# Define the Calculator class
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    # Static method - does not access class or instance data
    @staticmethod
    def add(a, b):
        return a + b
    
    # Class method - accesses class-level data
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
