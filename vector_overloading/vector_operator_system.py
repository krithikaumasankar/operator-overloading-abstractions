class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Vector Addition
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # Vector Subtraction
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # Scalar Multiplication
    def __mul__(self, scalar):
        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    # Equality Check
    def __eq__(self, other):
        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )

    # Dot Product
    def dot_product(self, other):
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    # Cross Product
    def cross_product(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # Display Vector
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Input from user
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
z1 = int(input("Enter z1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
z2 = int(input("Enter z2: "))

scalar = int(input("Enter scalar value: "))

# Creating vectors
v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

# Operations
print("\nVector 1 =", v1)
print("Vector 2 =", v2)

print("\nAddition =", v1 + v2)
print("Subtraction =", v1 - v2)
print("Scalar Multiplication for v1=", v1 * scalar)
print("Vectors Equal =", v1 == v2)
print("Dot Product =", v1.dot_product(v2))
print("Cross Product =", v1.cross_product(v2))
