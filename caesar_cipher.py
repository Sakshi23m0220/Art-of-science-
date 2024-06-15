letter = ("abcdefghijklmnopqrstuvwxyz")


def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letter.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                    ciphertext += letter

                return ciphertext


print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

while True:
    user_input = input('Do you want to encrypt or decrypt? (e/d): ').strip().lower()
    if user_input in ['e', 'd']:
        break
    else:
        print("Invalid choice, please enter 'e' for encryption or 'd' for decryption.")
print()

if user_input == 'e':
    print('*** ENCRYPT ***')
    print()
    key = int(input("Enter key (1 through 26): ").strip())
    text = input("Enter text: ").strip()

elif user_input == 'd':
    print('*** DECRYPT ***')
print()
key = int(input("enter key: (1 through 26): "))
text = input("enter text: ")
