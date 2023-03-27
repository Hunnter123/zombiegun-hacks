level = 1
gun_level = 0
gun = "glock"
level_gun = 2
money = 0
while True:
    player_input = int(input())
    if player_input < level_gun:
        level_gun = level_gun + 1
        money = money + player_input
    else:
        print("You do not have a high enough level for this gun.")
    if level_gun >= 5:
        gun = "AK-47"
        gun_level = 1
    print("Your current gun is: " + gun + " at level " + str(gun_level) + " and you have $" + str(money))