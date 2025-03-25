# wk_albet = "B"
# wk_albet_b = "b"

# print(ord(wk_albet))
# print(ord(wk_albet_b))

# print("." * 4)


# for i in range(8):
#     print(i)
# print("." * 8)
# if i % 2 == 0:
#     print(" " + "." * 8)
#     break
# else:
# print("." * 8)
# pass
# else:
#     print("Executed else block: ====>")
#     print(" " + "." * 8)

# total_even_number = 0

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#         total_even_number += 1

# print(f"We have {total_even_number} total even numbers.")

def fix_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print(fix_buzz(50))
