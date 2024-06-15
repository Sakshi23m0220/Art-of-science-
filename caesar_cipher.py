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

def main():
    # Take user input for file name
    file_name = input("Enter the file name (with extension): ").strip()

    try:
        # Open and read the text file
        with open('C:\\Users\\rahul\\PycharmProjects\\week1\\Sample.txt') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please ensure the file exists and try again.")
        return

    # Ensure the text is of sufficient length
    word_count = len(text.split())
    if word_count < 1800 or word_count > 1900:
        print("The text must be between 1800 and 1900 words.")
        return

    # Prompt the user for a key
    while True:
        try:
            key = int(input("Enter the key (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Prompt the user for their choice of encryption or decryption
    mode = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    while mode not in ['e', 'd']:
        mode = input("Invalid input. Enter 'e' for encryption or 'd' for decryption: ").lower()

    # Perform the encryption or decryption
    result = caesar_cipher(text, key, mode)

    # Store the resulting text in a file named "output.txt"
    with open('output.txt', 'w') as output_file:
        output_file.write(result)

    # Print the result to the console
    print("The result has been saved in 'output.txt'.")
    print("Here is the resulting text:\n")
    print(result)

if __name__ == "__main__":
    main()
