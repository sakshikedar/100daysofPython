import random
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']

print("Welcome to Pypassword Generator")
p_alphabets=int(input("How many alphabets you want?\n"))
p_numbers=int(input("How many numbers do you want?\n"))
p_symbols=int(input("How many symbols do you want?\n"))

#easy
password=""
for char in range(1, p_alphabets + 1):
    password+=random.choice(alphabets)
for char in range(1, p_numbers + 1):
    password+=random.choice(numbers)
for char in range(1, p_symbols +1):
    password+=random.choice(symbols)

print(password)

#hard
password_list=[]
for char in range(1, p_alphabets + 1):
    password_list.append(random.choice(alphabets))
for char in range(1, p_numbers + 1):
    password_list+=random.choice(numbers)
for char in range(1, p_symbols +1):
    password_list+=random.choice(symbols)

random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your password:{password}")