class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Operator Overloading for Addition
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    # Operator Overloading for Subtraction
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    # String Representation
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

# Input for First Complex Number
print("Enter First Complex Number")
real1 = int(input("Enter Real Part: "))
imag1 = int(input("Enter Imaginary Part: "))

# Input for Second Complex Number
print("\nEnter Second Complex Number")
real2 = int(input("Enter Real Part: "))
imag2 = int(input("Enter Imaginary Part: "))

# Creating Objects
c1 = ComplexNumber(real1, imag1)
c2 = ComplexNumber(real2, imag2)

# Operations
addition = c1 + c2
subtraction = c1 - c2

# Display Results
print("\nFirst Complex Number :", c1)
print("Second Complex Number:", c2)

print("\nAddition Result      :", addition)
print("Subtraction Result   :", subtraction)
