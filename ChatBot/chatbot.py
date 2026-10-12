def main():
    bot_name = "DICT_Bot"
    birth_year = "2020"

    # Stage 1: Приветствие
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

    # Stage 2: Знакомство
    print("Please, remind me your name.")
    your_name = input()
    print(f"What a great name you have, {your_name}!")

    # Stage 3: Угадывание возраста
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {your_age}; that's a good time to start programming!")

    # Stage 4: Подсчет
    print("Now I will prove to you that I can count to any number you want.")
    count_to = int(input())

    for i in range(count_to + 1):
        print(f"{i} !")

    # Stage 5: Тест по программированию
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    while True:
        answer = input()
        if answer == "2":
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")

    print("Congratulations, have a nice day!")


if __name__ == "__main__":
    main()