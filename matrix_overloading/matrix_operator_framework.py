class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
        print(f"\nEnter elements for {rows}x{cols} matrix:")
        self.data = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = int(input(f"Enter element [{i}][{j}]: "))
                row.append(value)
            self.data.append(row)

    # Matrix Addition
    def __add__(self, other):
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return result

    # Matrix Subtraction
    def __sub__(self, other):
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return result

    # Matrix Multiplication
    def __mul__(self, other):
        result = []

        for i in range(self.rows):
            row = []

            for j in range(other.cols):
                total = 0

                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]

                row.append(total)

            result.append(row)

        return result

    # Display Matrix
    def display(self):
        for row in self.data:
            for value in row:
                print(value, end=" ")
            print()


# Main Program
r1 = int(input("Enter rows of Matrix 1: "))
c1 = int(input("Enter columns of Matrix 1: "))

m1 = Matrix(r1, c1)

r2 = int(input("\nEnter rows of Matrix 2: "))
c2 = int(input("Enter columns of Matrix 2: "))

m2 = Matrix(r2, c2)

print("\nMatrix 1:")
m1.display()

print("\nMatrix 2:")
m2.display()

# Addition
if r1 == r2 and c1 == c2:
    print("\nMatrix Addition:")
    add_result = m1 + m2

    for row in add_result:
        for value in row:
            print(value, end=" ")
        print()

    print("\nMatrix Subtraction:")
    sub_result = m1 - m2

    for row in sub_result:
        for value in row:
            print(value, end=" ")
        print()

else:
    print("\nAddition and Subtraction not possible")

# Multiplication
if c1 == r2:
    print("\nMatrix Multiplication:")
    mul_result = m1 * m2

    for row in mul_result:
        for value in row:
            print(value, end=" ")
        print()

else:
    print("\nMultiplication not possible")
