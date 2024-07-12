even_squares = []
odd_squares = []
for number in range(51):
    square = number * number
    if number % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("\n even_squares")
for i in even_squares:
    print(i)
print("\n odd_squares")
for i in odd_squares:
    print(i)