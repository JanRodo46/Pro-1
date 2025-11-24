# Zad 1
number = 1 + 2 * 3 / 4.0
print(number)
# Zad 2
remainder = 11 % 3
print(remainder)
# Zad 3
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
# Zad 4
helloworld = "hello" + " " + "world"
print(helloworld)
# Zad 5
lotsofhellos = "hello" * 10
print(lotsofhellos)
# Zad 6
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
# Zad 7
print([1, 2, 3] * 3)
# Zad 8
x = object()
y = object()
x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if len(x_list) == 10 and len(y_list) == 10:
    print("Almost there...")
if len(big_list) == 20:
    print("Great!")
