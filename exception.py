import os


# try:
# Create a new directory named 'my_directory'
#     os.makedirs('my_directory')
# except FileExistsError:
#     print("'my_directory' already exists")

# Change the current working directory to 'my_directory'
# os.chdir('my_directory')

# Create a new file named 'my_file.txt'
# try:
#     with open('my_file.txt', 'w') as file:
#         file.write('Hello, this is my file.')
# except FileExistsError:
#     print("'my_file.txt' already exists")
#     # Overwrite the existing file
#     with open('my_file.txt', 'w') as file:
#         file.write('Hello, this is my updated file.')

# List all files in the current directory
# print(os.listdir())


# Accept the command line arguments
# print(sys.argv)
# print(sys.argv[1])
# print(sys.argv[2])


# Read a file
# with open('my_file.txt', 'r') as file:
#     print(file.read())

# sys.exit()
# exit()
# name = input('Enter your name: ')

# Accept input from the user
try:
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    age = int(input('Enter your age: '))
    print(f'You are {age} years old.')
except ValueError:
    print('Invalid input. Please enter a number for age.')
except EOFError:
    print('No input provided.')
except KeyboardInterrupt:
    print('Interrupted by user.')
except Exception as e:
    print(f'An error occurred: {e}')
else:
    print('Program completed successfully.')
finally:
    print('Closing the program.')


# Remove the file
# os.remove('my_file.txt')

# raise Exception
# raise ValueError('Invalid value')
# raise ValueError from None
# raise ValueError('Invalid value') from None
# raise ValueError('Invalid value') from ValueError('Another error')
# raise ValueError('Invalid value') from ValueError('Another error') from None
