sentence = 'This is a common interview question'

char_frequency = {}
unpacked = [char for char in sentence if char and char != ' ']

print(unpacked)

for char in unpacked:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print(char_frequency)

max_frequency = max(char_frequency.values())
print(max_frequency)

sorted_char_frequency = sorted(
    char_frequency.items(), key=lambda x: x[1], reverse=True)
print(sorted_char_frequency)

for char, frequency in sorted_char_frequency:
    print(f'{char}: {frequency}')

print(sorted_char_frequency[0])

most_repeated_char = [
    (char, frequency) for char, frequency in char_frequency.items() if frequency == max_frequency]
print(most_repeated_char[0])
