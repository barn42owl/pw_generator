import random

letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P","Q", "R", "S","T","U","V", "W","X","Y","Z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
symbols=["!", "#", "$", "%", "&", "(", ")", "*", "+"]



print("Welcome to the PyPassword Generator!")
int_letters=int(input("How many letters would you like in your password?\n"))
int_symbols=int(input("How many symbols would you like in your password?\n"))
int_numbers=int(input("How many numbers would you like in your password?\n"))

p=[]
for value in range(0, int_letters, 1):
    letters_list= random.choice(letters)
    p.append(letters_list)

for repeat in range(0, int_symbols, 1):
    symbols_list= random.choice(symbols)
    p.append(symbols_list)

for repeat in range(0, int_numbers, 1):
    numbers_list= random.choice(numbers)
    p.append(numbers_list)


random.shuffle(p)
p_str= "".join(p)

print(f"Here is your password: {p_str}")
