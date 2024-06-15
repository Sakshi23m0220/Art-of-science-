def caesar_cipher(text, key, mode):
    result = ""
    if mode == 'd':
        key = -key

    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

print('*** CAESAR CIPHER PROGRAM ***')
print()

while True:
    user_input = input('Do you want to encrypt or decrypt? (e/d): ').strip().lower()
    if user_input in ['e', 'd']:
        break
    else:
        print("Invalid choice, please enter 'e' for encryption or 'd' for decryption.")
print()

key = int(input("Enter key (1 through 26): ").strip())
text = input("Enter text: ").strip()

result = caesar_cipher(text, key, user_input)
print("Resulting text:", result)
print("Length of the resulting text:", len(result))




