from stega import embed_message, extract_message

def main():
    choice = input("Do you want to (e)mbed a message or (x)tract a message? ")

    if choice == 'e':
        source_image = input("Enter the path to the source image: ")
        message = input("Enter the message to hide: ")
        output_image = input("Enter the path for the steganographic image: ")

        embed_message(source_image, message, output_image)
        print(f"Message embedded in {output_image}!")

    elif choice == 'x':
        steg_image = input("Enter the path to the steganographic image: ")
        secret = extract_message(steg_image)
        print(f"Extracted message: {secret}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
