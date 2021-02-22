for value in range(1,5):
    print(value)

numbers = list(range(1,5))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares2 = [value**2 for value in range(1,11)]
print(squares2)

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
#['charles', 'martina', 'michael']
print(players[-3:])
#['michael', 'florence', 'eli']