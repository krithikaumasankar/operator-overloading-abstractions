class Word:
    def __init__(self, text):
        self.text = text

    # Operator Overloading for Concatenation
    def __add__(self, other):
        return Word(self.text + other.text)

    # Operator Overloading for Equality Check
    def __eq__(self, other):
        return self.text == other.text

    # String Representation
    def __str__(self):
        return self.text

# Input from User
word1 = input("Enter First Word : ")
word2 = input("Enter Second Word: ")

# Creating Objects
w1 = Word(word1)
w2 = Word(word2)

# Concatenation
concatenated_word = w1 + w2

# Equality Check
is_equal = w1 == w2

# Display Results
print("\nFirst Word :", w1)
print("Second Word:", w2)

print("\nConcatenated Word:", concatenated_word)

if is_equal:
    print("Both words are Equal")
else:
    print("Both words are Not Equal")
