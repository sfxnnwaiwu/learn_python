# def total_xp(level, xp_to_add):
#     old_xp = level * 100
#     new_xp = old_xp + xp_to_add
#     return new_xp

# =========================================================


# def take_magic_damage(health, resist, amp, spell_power):
#     damage = spell_power * amp
#     damage -= resist
#     health -= damage
#     return health

# ============================================================
    

# def unlock_achievement(before_xp, ach_xp, ach_name):
#     after_xp = before_xp + ach_xp
#     alert = "Achievement Unlocked: " + ach_name
#     return after_xp, alert

# ============================================================


# def create_stats_message(strength, wisdom, dexterity):
#     total = strength + wisdom + dexterity
#     msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
#     return msg

# ============================================================

# def calculate_damage(sword, arrow, spear, dagger, fireball):
#     total_damage = sword + arrow + spear + dagger + fireball
#     average_damage = total_damage / 5
#     return total_damage, average_damage

# ============================================================

# def update_player_score(current_score, increment):
#     return current_score + increment

# ============================================================

# def get_hurt(current_health, damage):
#     current_health -= damage
#     return current_health

# ============================================================

# def max_players_on_server():
#     small = 1.024e18
#     medium = 1.024e19
#     large = 1.024e20
#     return small, medium, large

# ============================================================

# can_create_guild = 0b1000
# can_review_guild = 0b0100
# can_delete_guild = 0b0010
# can_edit_guild = 0b0001


# def get_create_bits(user_permissions):
#     return can_create_guild & user_permissions


# def get_review_bits(user_permissions):
#     return can_review_guild & user_permissions


# def get_delete_bits(user_permissions):
#     return can_delete_guild & user_permissions


# def get_edit_bits(user_permissions):
#     return can_edit_guild & user_permissions

# ============================================================

# def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
#     return glorfindel | galadriel | elendil | elrond

# ============================================================

# def binary_string_to_int(num_servers, num_players, num_admins):
#     server = int(num_servers, 2)
#     players = int(num_players, 2)
#     admins = int(num_admins, 2)
#     return server, players, admins

# ============================================================

# def player_1_wins(player_1_score, player_2_score):
#     return player_1_score > player_2_score

# ============================================================

# def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
#     is_mustang_edward_same = mustang_height == edward_height
#     is_alphonse_edeward_same = alphonse_height == edward_height
#     is_winry_alphonse_same = winry_height == alphonse_height
#     return is_mustang_edward_same, is_alphonse_edeward_same, is_winry_alphonse_same

# ============================================================

# def player_status(health):
#     if health <= 0:
#         return "dead"
#     elif health <= 5:
#         return "injured"
#     else:
#         return "healthy"

# ============================================================


# def get_item_counts(items):
#     potion_count = 0
#     bread_count = 0
#     shortsword_count = 0

#     # don't touch above this line

#     for i in range(0, len(items)):
#         print(items[i])
#         if items[i] == "Potion":
#             potion_count += 1
#         elif items[i] == "Bread":
#             bread_count += 1
#         elif items[i] == "Shortsword":
#             shortsword_count += 1
#         else:
#             continue

#     # don't touch below this line

#     return potion_count, bread_count, shortsword_count

# ============================================================

# def find_max(nums):
#     max_so_far = float("-inf")
#     for num in nums:
#         if num > max_so_far:
#             max_so_far = num

#     return max_so_far

# ============================================================

# def get_odd_numbers(num):
#     odd_numbers = []

#     for i in range(0, num):
#         # don't touch above this line

#         # print(i)
#         if i % 2 != 0:
#             odd_numbers.append(i)
#         else:
#             continue

#     # don't touch below this line

#     return odd_numbers

# ============================================================

def get_heroes():
    heroes = [
        ("Glorfindel", 2093, True,),
        ("Gandalf", 1054, False,),
        ("Gimli", 389, False,),
        ("Aragorn", 87, False,),
    ]

    return heroes