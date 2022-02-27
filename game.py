import random


# get scores from already existing scorecard text file
def get_rating():
    name = input("Enter your name: ")
    print(f"Hello, {name}")

    with open('rating.txt') as rating_file:
        for line in rating_file:
            name_in_file, rating = line.rstrip('\n').split()
            if name_in_file == name:
                return int(rating.rstrip('\n'))
    return 0


def get_options():
    options = input().split(',')
    if options[0] != '':
        return options
    return ['rock', 'paper', 'scissors']


def play(player_rating, game_options):
    while True:
        user = input()
        if user == '!exit':
            print('Bye!')
            quit()
        elif user == '!rating':
            print(f'Your rating: {player_rating}')
            continue
        elif user not in game_options:
            print('Invalid input')
            continue

        comp = random.choice(game_options)

        user_index = game_options.index(user)
        # making a list from which it will be easy to read who won
        # 1. we move all available options after the users option to the front
        # 2. if the computers move is in the first half of the new list then the computer won
        # 3. if it is in the second half then the user won
        relative_options = game_options[user_index + 1:] + game_options[:user_index]

        if user == comp:
            print("There is a draw (" + user + ")")
            player_rating += 50
        elif comp in relative_options[:len(relative_options) // 2]:
            print("Sorry, but the computer chose", comp)
        else:
            print("Well done. The computer chose", comp, "and failed")
            player_rating += 100


def main():
    rating = get_rating()
    options = get_options()

    print("Okay, let's start")
    play(rating, options)


if __name__ == "__main__":
    main()
