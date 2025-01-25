import string

str_letters = "abc"
array_shifts = [[0,1,0],[1,2,1],[0,2,1]]

def shiftingLetters(letters, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        alphabets = string.ascii_lowercase

        print(letters)
        print(shifts)

        for item in shifts:
                start = item[0]
                end = item[1]
                direction = item[2]
                
                for i in range(start, (end + 1)):
                        change = letters[i]
                        print(f'Character to Stransform: ===> {change}')
                        if direction == 1:
                                print('Forward')
                                position = alphabets.index(change)
                                if position + 1 == 26:
                                        copy1 = letters[:i]
                                        copy2 = letters[(i + 1):]
                                        new_char = alphabets[0]

                                        letters = f'{copy1}{new_char}{copy2}'
                                        print(f"New Str Forward first block: {letters}")
                                elif position + 1 == 1:
                                            copy1 = letters[:i]
                                            copy2 = letters[(i + 1):]
                                            new_char = alphabets[(position + 1)]

                                            letters = f'{copy1}{new_char}{copy2}'

                                            print(f"New Str Forward second block: {letters}")
                                        
                                else:
                                        copy1 = letters[:i]
                                        copy2 = letters[(i + 1):]
                                        new_char = alphabets[(position + 1)]
                                        letters = f'{copy1}{new_char}{copy2}'

                                        print(f"New Str Forward last block: {letters}")
                        elif direction == 0:
                                print('Backward')
                                position = alphabets.index(change)
                                if position + 1 == 26:
                                        copy1 = letters[:i]
                                        copy2 = letters[(i + 1):]
                                        new_char = alphabets[(position - 1)]
                                        letters = f'{copy1}{new_char}{copy2}'

                                        print(f"New Str Backward First Block: {letters}")
                                elif position + 1 == 1:
                                            copy1 = letters[:i]
                                            copy2 = letters[(i + 1):]
                                            new_char = alphabets[25]

                                            letters = f'{copy1}{new_char}{copy2}'
                                            print(f"New Str Backward Second Block: {letters}")
                                else:
                                        copy1 = letters[:i]
                                        copy2 = letters[(i + 1):]
                                        new_char = alphabets[(position - 1)]

                                        letters = f'{copy1}{new_char}{copy2}'

                                        print(f"New Str Backward Last Block: {letters}")
        return letters


print(shiftingLetters(str_letters, array_shifts))