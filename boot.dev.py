def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

# don't touch above this line

# max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

# print(f"max_health is: {max_health}")

# ============================================

# player_level = 4

# def calculate_health(modifier):
#     return player_level * modifier


# def calculate_primary_stats(armor_bonus, modifier):
#     return armor_bonus + modifier + player_level


# print(f"Character has {calculate_health(10)} max health.")

# print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

# ========================================================================

# def main():
#     calculate_dps(8_000_000, 45)
#     calculate_dps(10_000_000, 49)


# # Don't edit below this line


# def calculate_dps(damage, time):
#     dps = damage / time
#     print(f"Damage per second: {dps}")
#     print("=====================================")


# main()


# =========================================================================

# def print_status(player_health):
#     if player_health == 0:
#         print("You are dead.")

#     print("status checked completed.")


# # Don't edit below this line


# def test(health):
#     print(f"Player Health: {health}")
#     print("Checking status...")
#     print_status(health)
#     print("=====================================")


# def main():
#     test(0)
#     test(5)
#     test(3)


# main()

# =========================================================================

# def do_looping(end):
#     for i in range(0, end):
#         print(i)

# do_looping(5)
# do_looping(10)
# do_looping(16)
# do_looping(20)

# =========================================================================

# num = 0
# while num < 3:
#     num += 1
#     print(num)

# =========================================================================

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i, char in enumerate(old_character_levels):
        if char < new_character_levels[i]:
            print(i)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()

negative_infinity = float("-inf")
positive_infinity = float("inf")

print(negative_infinity)
print(positive_infinity)
