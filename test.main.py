from main import *

# run_cases = [
#     (1, 200, 300),
#     (2, 50, 250),
# ]

# submit_cases = run_cases + [
#     (0, 0, 0),
#     (0, 200, 200),
#     (176, 350, 17950),
#     (250, 100, 25100),
# ]

# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}")
#     print(f"Expecting: {expected_output}")
#     result = total_xp(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# =======================================================


# run_cases = [
#     (100, 5, 2, 20, 65),
#     (200, 10, 1, 25, 185),
# ]

# submit_cases = run_cases + [
#     (0, 0, 0, 0, 0),
#     (1, 1, 1, 1, 1),
#     (100, 2, 3, 1, 99),
#     (2500, 3, 2, 2, 2499),
# ]


# def test(input1, input2, input3, input4, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
#     print(f"Expecting: {expected_output}")
#     result = take_magic_damage(input1, input2, input3, input4)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ==================================================





# run_cases = [
#     (100, 20, "Speedster", (120, "Achievement Unlocked: Speedster")),
#     (200, 50, "Killer", (250, "Achievement Unlocked: Killer")),
# ]

# submit_cases = run_cases + [
#     (100, 50, "Unstoppable", (150, "Achievement Unlocked: Unstoppable")),
#     (400, 75, "Gnarly", (475, "Achievement Unlocked: Gnarly")),
# ]


# def test(input1, input2, input3, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}, {input3}")
#     print(f"Expecting: {expected_output}")
#     result = unlock_achievement(input1, input2, input3)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ==========================================================================


# run_cases = [
#     (1, 2, 3, "You have 1 strength, 2 wisdom, and 3 dexterity for a total of 6 stats."),
#     (2, 4, 2, "You have 2 strength, 4 wisdom, and 2 dexterity for a total of 8 stats."),
# ]

# submit_cases = run_cases + [
#     (
#         10,
#         50,
#         100,
#         "You have 10 strength, 50 wisdom, and 100 dexterity for a total of 160 stats.",
#     ),
#     (0, 0, 0, "You have 0 strength, 0 wisdom, and 0 dexterity for a total of 0 stats."),
#     (1, 1, 1, "You have 1 strength, 1 wisdom, and 1 dexterity for a total of 3 stats."),
# ]


# def test(input1, input2, input3, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}, {input3}")
#     print(f"Expecting: {expected_output}")
#     result = create_stats_message(input1, input2, input3)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


# run_cases = [
#     (3, 5, 2, 1, 4, (15, 3.0)),
#     (5, 5, 5, 5, 5, (25, 5.0)),
# ]

# submit_cases = run_cases + [
#     (1, 2, 3, 4, 5, (15, 3.0)),
#     (0, 0, 0, 0, 10, (10, 2.0)),
#     (0, 0, 0, 0, 0, (0, 0.0)),
#     (10, 20, 30, 40, 50, (150, 30.0)),
#     (2, 2, 2, 2, 2, (10, 2.0)),
#     (1, 1, 1, 1, 1, (5, 1.0)),
# ]


# def test(sword, arrow, spear, dagger, fireball, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {sword}, {arrow}, {spear}, {dagger}, {fireball}")
#     print(f"Expecting: {expected_output}")
#     result = calculate_damage(sword, arrow, spear, dagger, fireball)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


# run_cases = [
#     (0, 100, 100),
#     (100, 200, 300),
# ]

# submit_cases = run_cases + [
#     (300, 300, 600),
#     (600, 50, 650),
#     (0, 0, 0),
#     (1, 1, 2),
#     (100, -50, 50),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}")
#     print(f"Expecting: {expected_output}")
#     result = update_player_score(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


# run_cases = [
#     (1000, 100, 900),
#     (900, 60, 840),
# ]

# submit_cases = run_cases + [
#     (840, 10, 830),
#     (830, 3, 827),
#     (0, 0, 0),
#     (1, 1, 0),
#     (100, 2, 98),
#     (2500, 3, 2497),
# ]


# def test(current_health, damage, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {current_health}, {damage}")
#     print(f"Expecting: {expected_output}")
#     result = get_hurt(current_health, damage)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


# run_cases = [
#     (1.024e18, 1.024e19, 1.024e20),
# ]

# submit_cases = run_cases


# def test(expected1, expected2, expected3):
#     print("---------------------------------")
#     print(f"Expecting: {(expected1, expected2, expected3)}")
#     result = max_players_on_server()
#     print(f"Actual: {result}")
#     if result == (expected1, expected2, expected3):
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


# run_cases = [
#     (0b0110, False, True, True, False),
#     (0b1111, True, True, True, True),
#     (0b0000, False, False, False, False),
# ]

# submit_cases = run_cases + [
#     (0b1001, True, False, False, True),
#     (0b1000, True, False, False, False),
#     (0b0100, False, True, False, False),
#     (0b0010, False, False, True, False),
#     (0b0001, False, False, False, True),
# ]


# def test(
#     input1, expected_output1, expected_output2, expected_output3, expected_output4
# ):
#     print("---------------------------------")
#     print(f"Inputs: {input1:04b}")
#     print(f"Expecting can_create: {expected_output1}")
#     print(f"Expecting can_review: {expected_output2}")
#     print(f"Expecting can_delete: {expected_output3}")
#     print(f"Expecting can_edit: {expected_output4}")

#     result1 = get_create_bits(input1) == can_create_guild
#     result2 = get_review_bits(input1) == can_review_guild
#     result3 = get_delete_bits(input1) == can_delete_guild
#     result4 = get_edit_bits(input1) == can_edit_guild

#     print(f"Actual can_create: {result1}")
#     print(f"Actual can_review: {result2}")
#     print(f"Actual can_delete: {result3}")
#     print(f"Actual can_edit: {result4}")
#     if (
#         result1 == expected_output1
#         and result2 == expected_output2
#         and result3 == expected_output3
#         and result4 == expected_output4
#     ):
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
# ]

# submit_cases = run_cases + [
#     (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
#     (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
# ]


# def test(input1, input2, input3, input4, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
#     print(f"Expecting: {expected_output}")
#     result = calculate_guild_perms(input1, input2, input3, input4)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     ("1", "10", "1010", (1, 2, 10)),
#     ("101", "11", "10100", (5, 3, 20)),
#     ("111", "1011", "11010", (7, 11, 26)),
# ]

# submit_cases = run_cases + [
#     ("0", "0", "0", (0, 0, 0)),
#     ("1111", "1111", "1111", (15, 15, 15)),
#     ("101010", "110011", "101010", (42, 51, 42)),
# ]


# def test(input1, input2, input3, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}, {input3}")
#     print(f"Expecting: {expected_output}")
#     result = binary_string_to_int(input1, input2, input3)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     (5, 6, False),
#     (5, 5, False),
#     (7, 6, True),
# ]

# submit_cases = run_cases + [
#     (10, 3, True),
#     (2, 2, False),
#     (0, 0, False),
#     (10, 5, True),
#     (5, 10, False),
# ]


# def test(player_1_score, player_2_score, expected):
#     print("---------------------------------")
#     print(f"Inputs: {player_1_score}, {player_2_score}")
#     print(f"Expecting: {expected}")
#     result = player_1_wins(player_1_score, player_2_score)
#     print(f"Actual: {result}")
#     if result == expected:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     (5, 5, 7, 5, (True, True, False)),
#     (6, 6, 5, 5, (False, True, False)),
# ]

# submit_cases = run_cases + [
#     (4, 4, 4, 4, (True, True, True)),
#     (2, 2, 2, 2, (True, True, True)),
#     (8, 8, 8, 7, (False, True, True)),
#     (5, 7, 9, 11, (False, False, False)),
#     (11, 9, 7, 5, (False, False, False)),
# ]


# def test(elon, sara, jill, bob, expected):
#     print("---------------------------------")
#     print(f"Inputs: {elon}, {sara}, {jill}, {bob}")
#     print(f"Expecting: {expected}")
#     result = compare_heights(elon, sara, jill, bob)
#     print(f"Actual: {result}")
#     if result == expected:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     (0, "dead"),
#     (4, "injured"),
# ]

# submit_cases = run_cases + [
#     (6, "healthy"),
#     (5, "injured"),
#     (1, "injured"),
#     (10, "healthy"),
#     (-1, "dead"),
# ]


# def test(health, expected_status):
#     print("---------------------------------")
#     print(f"Health: {health}")
#     print(f"Expecting: {expected_status}")
#     result = player_status(health)
#     print(f"Result: {result}")
#     if result == expected_status:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [
#     (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
#     (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
# ]

# submit_cases = run_cases + [
#     ([], (0, 0, 0)),
#     (
#         [
#             "Potion",
#             "Leather Scraps",
#             "Bread",
#             "Iron Ore",
#             "Light Leather",
#             "Bread",
#             "Shortsword",
#             "Longsword",
#             "Ironwood Branch",
#             "Shortsword",
#             "Shortsword",
#         ],
#         (1, 2, 3),
#     ),
#     (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
#     (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
#     (["Potion"], (1, 0, 0)),
#     (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
# ]


# def test(input, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input}")
#     print(f"Expecting: {expected_output}")
#     result = get_item_counts(input)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

# submit_cases = run_cases + [
#     ([1, 20, 3, 4, 5], 20),
#     ([-1, 2, 3, 4, 5], 5),
#     ([1, 2, 3, 21, 18], 21),
#     ([], float("-inf")),
#     ([-1, -2, -3, -4, -5], -1),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}")
#     print(f"Expecting: {expected_output}")
#     result = find_max(input1)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================

# run_cases = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]

# submit_cases = run_cases + [
#     (0, []),
#     (1, []),
#     (2, [1]),
#     (300, [i for i in range(1, 300, 2)]),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}")
#     print(f"Expecting: {expected_output}")
#     result = get_odd_numbers(input1)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False

# ===========================================================================================


run_cases = [
    (
        [
            (
                "Glorfindel",
                2093,
                True,
            ),
            (
                "Gandalf",
                1054,
                False,
            ),
            (
                "Gimli",
                389,
                False,
            ),
            (
                "Aragorn",
                87,
                False,
            ),
        ]
    ),
]

submit_cases = run_cases


def test(expected_output):
    print("---------------------------------")
    passed = True
    result = get_heroes()
    for i, hero in enumerate(expected_output):
        print(f"Expected: {hero} at index {i}")
        if i >= len(result):
            print(f"Actual: None at index {i}")
            print("Fail")
            passed = False
            continue
        print(f"Actual: {result[i]} at index {i}")
        if hero != result[i]:
            print("Fail")
            passed = False
        else:
            print("Pass")
    return passed


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()