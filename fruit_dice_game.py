import random

def fruit_dice_game():
    print("Welcome to the Multiplayer Fruit Dice Challenge!🍒🍌🎲\n")

    number_of_playeres = 2 # oyuncuların sayısı
    players = [] # oyuncuların bilgilerini tutmak için

    # her oyuncunun ismini al ve paşlangıç puanlarını 0 yap
    for i in range(number_of_playeres):
        name = input(f"Enter name for the player {i+1}: ")
        players.append({"name": name, "point": []})

    # oyun 3 turdan oluşuyor
    for round in range(1,4):
        print(f"\n--- Round {round} ---")
        print("-" * 40)

        # her turda her oyuncu sırasıyla oynar
        for player in players:

            fruits = ['Cherry', 'Banana', 'apple']
            fruit = random.choice(fruits)
            dice = random.choice([1, 2, 3, 4, 5, 6])

            # oyuncunun ne atığını yazdır
            print(f"{player['name']} rolled a {dice} and got a {fruit}")

            # meyve göre puan ver
            if fruit == 'Banana':
                earned_points = dice + 6
                print("Banana bonus! +6 points\n")
            elif fruit == 'Cherry' and dice == 6 :
                earned_points =dice +10
                print("Cherry bonus! +10 points\n")
            else:
                earned_points = dice
                print(f"Dice bonus! {dice} points\n")

            player['point'].append(earned_points)
            print(f"points of the player {player['name']} at the round {round} is {earned_points}\n")

    print("-- Game over --")
    print("Final Scores: ")

    for player in players:
        total = sum(player['point'])
        print(f"{player['name']}: {total} points")
        player['total'] = total # karşılaştırmak için saklıyoruz

    if players[0]['total'] > players[1]['total']:
        print(f"\n{players[0]['name']} wins!🎉")
    elif players[1]['total'] > players[0]['total']:
        print(f"\n{players[1]['name']} wins!🎉")
    else:
        print("The  game ends in a draw!")
fruit_dice_game()