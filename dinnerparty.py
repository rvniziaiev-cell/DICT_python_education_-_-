import random


def main():
    try:
        num_friends = int(input("Enter the number of friends joining (including you):\n> "))
    except ValueError:
        print("No one is joining for the party")
        return

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0

    try:
        total_amount = float(input("Enter the total amount:\n> "))
    except ValueError:
        return

    split_amount = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = split_amount

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')

    if lucky_choice.strip().lower() == "yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        if num_friends > 1:
            new_split = round(total_amount / (num_friends - 1), 2)
            for name in friends:
                if name == lucky_one:
                    friends[name] = 0
                else:
                    friends[name] = new_split
    else:
        print("No one is going to be lucky")

    print(friends)


if __name__ == "__main__":
    main()