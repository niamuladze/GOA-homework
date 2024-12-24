#1 work

name = input("enter name: ")
print("Hello, " + name )

age = input("enter age: ")
print("you are " + age)

#3 work

me =int(input("my age is: "))
brother =int(input("my brother age is: "))
mom = int(input("my mom age is: "))
dad = int(input("my dad age is: "))

print(me + 10, brother + 10, mom + 10, dad + 10)

#4 work

num1 = str(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = str(input("შეიყვანეთ მეორე რიცხვი (num2): "))

print(f"{num1 + num2}")
print(f"{num1 - num2}")
print(f"{num1 * num2}")
print(f"{num1 / num2}")


#5 work

num1 = str(input("შეიყვანეთ num1: "))
num2 = str(input("შეიყვანეთ num2: "))
num3 = str(input("შეიყვანეთ num3: "))
num4 = str(input("შეიყვანეთ num4: "))
num5 = str(input("შეიყვანეთ num5: "))


print((num1 + num2) / num3 - num4 * num5 + num1**num3 % num2)


#boss level

name = input("შეიყვანეთ სახელი: ")
surname = input("შეიყვანეთ გვარი: ")
age = input("შეიყვანეთ ასაკი: ")
email = input("შეიყვანეთ ელფოსტა: ")
birth_year = input("შეიყვანეთ დაბადების წელი: ")
birthday = input("შეიყვანეთ დაბადების თარიღი (დღე/თვე): ")

print("\nშეყვანილი მონაცემები:")
print(f"სახელი: {name}")
print(f"გვარი: {surname}")
print(f"ასაკი: {age}")
print(f"ელფოსტა: {email}")
print(f"დაბადების წელი: {birth_year}")
print(f"დაბადების თარიღი: {birthday}")