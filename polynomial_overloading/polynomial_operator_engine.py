class Polynomial:
    def __init__(self, coeffs):
        # coeffs are stored in decreasing order of powers
        self.coeffs = coeffs

    def __mul__(self, other):
        # Resultant polynomial size
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        # Polynomial multiplication
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result)

    def display(self):
        n = len(self.coeffs)
        terms = []

        for i in range(n):
            coeff = self.coeffs[i]
            power = n - i - 1

            if coeff != 0:
                if power > 1:
                    terms.append(f"{coeff}x^{power}")
                elif power == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}")

        print(" + ".join(terms))


# Input for first polynomial
n1 = int(input("Enter number of coefficients for first polynomial: "))
p1 = []

print("Enter coefficients:")
for i in range(n1):
    p1.append(int(input()))

# Input for second polynomial
n2 = int(input("\nEnter number of coefficients for second polynomial: "))
p2 = []

print("Enter coefficients:")
for i in range(n2):
    p2.append(int(input()))

# Create objects
poly1 = Polynomial(p1)
poly2 = Polynomial(p2)

# Multiply using operator overloading
result = poly1 * poly2

# Display polynomials
print("\nFirst Polynomial:")
poly1.display()

print("\nSecond Polynomial:")
poly2.display()

print("\nMultiplication Result:")
result.display()
