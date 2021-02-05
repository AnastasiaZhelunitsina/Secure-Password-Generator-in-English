from random import *

def generate_password(the_length_of_a_password, chars):
    password = []
    for _ in range(the_length_of_a_password):
        password.append(choice(chars))
    shuffle(password)
    password = ''.join(password)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O'
chars = ''
again = input('If you need to generate a password or multiple passwords, enter "yes", if you want to exit, enter " no": ')

while again == 'y' or again == 'yes' or again == 'yep' or again == 'ype' or again == 'yse':
    print('Great!')
    print('Creating a password must be handled responsibly, regardless of the type and importance of the resource where it will be used. When creating a complex password, you should follow the following rules: \n'
          '- The password must contain at least 8 characters, or better – 10 or more. \n'
          '- The presence of numbers and letters in upper and lower case. \n'
          '- The presence of special characters – «@», «$», «&» и т.д. (if their presence is acceptable).')
    print()

    chars = ''
    number_of_passwords = int(input('How many passwords do I need to generate? Enter a number: '))
    the_length_of_a_password = int(input('How long should the password be? Enter the required number of characters:'))
    numbers_in_the_password = input('Should the password contain numbers (0123...)? Enter - "yes" if needed and " no " if numbers are not required: ').strip()
    uppercase_in_the_password = input('Should the password contain uppercase letters (ABCD...)? Enter - "yes" if needed and "no" if uppercase letters are not required: ').strip()
    lowercase_in_the_password = input('Should the password contain lowercase letters (abcd...)? Enter - "yes" if needed and "no" if lowercase letters are not required: ').strip()
    punctuation_in_the_password = input('Should the password contain punctuation characters (!#$%&*+-=?@^_)? Enter - "yes" if needed and " no " if punctuation characters are not required: ').strip()
    exceptions_in_the_password = input('Whether to exclude ambiguous characters (il1Lo0O) in the password? Enter - "yes" if you want to exclude these characters from the password, and "no" if you want to add ambiguous characters to the password: ').strip()
    print()

    if numbers_in_the_password == 'y' or numbers_in_the_password == 'yes' or numbers_in_the_password == 'yep' or numbers_in_the_password == 'ype' or numbers_in_the_password == 'yse':
        chars += digits
    if lowercase_in_the_password == 'y' or lowercase_in_the_password == 'yes' or lowercase_in_the_password == 'yep' or lowercase_in_the_password == 'ype' or lowercase_in_the_password == 'yse':
        chars += lowercase_letters
    if uppercase_in_the_password == 'y' or uppercase_in_the_password == 'yes' or uppercase_in_the_password == 'yep' or uppercase_in_the_password == 'ype' or uppercase_in_the_password == 'yse':
        chars += uppercase_letters
    if punctuation_in_the_password == 'y' or punctuation_in_the_password == 'yes' or punctuation_in_the_password == 'yep' or punctuation_in_the_password == 'ype' or punctuation_in_the_password == 'yse':
        chars += punctuation
    if exceptions_in_the_password == 'n' or exceptions_in_the_password == 'no' or exceptions_in_the_password == 'on' or exceptions_in_the_password == 'nope':
        chars += exceptions
    if exceptions_in_the_password == 'y' or exceptions_in_the_password == 'yes' or exceptions_in_the_password == 'yep' or exceptions_in_the_password == 'ype' or exceptions_in_the_password == 'yse':
        for c in chars:
            if c == 'i' or c == 'l' or c == '1' or c == 'L' or c == 'o' or c == '0' or c == 'O':
                chars = chars.replace(c, '')

    passwords = []

    for _ in range(number_of_passwords):
        passwords.append(generate_password(the_length_of_a_password, chars))

    print(*passwords, sep='\n')
    print()
    again = input('If you need to generate a password or multiple passwords, enter "yes", if you want to exit, enter " no": ')
else:
    print('Come back if you need to generate a strong password!')
    exit()





