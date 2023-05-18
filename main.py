username = input('Enter your username:\n ')
password = input('Enter your password:\n')
length = len(password)
hidden = '*' * length
print(f'{username}, your password {hidden} is {length} characters long.')

