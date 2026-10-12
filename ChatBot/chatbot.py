bot_name = "DICT_Bot"
birth_year = "2020"

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

print("Please, remind me your name.")
your_name = input()
print(f"What a great name you have, {your_name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")