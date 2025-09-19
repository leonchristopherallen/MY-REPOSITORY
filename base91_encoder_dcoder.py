import base91

# ANSI escape code for green text
GREEN = '\033[92m'
RESET = '\033[0m'

def main():
    # Print simple green title
    print(f"{GREEN}Base91 Encoder & Decoder{RESET}\n")

    while True:
        print("Choose an option:")
        print("1. Encode to Base91")
        print("2. Decode from Base91")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            text = input("Enter text to encode: ")
            encoded = base91.encode(text.encode('utf-8'))
            result = f'"{encoded}"'
            print("Encoded Base91:", result)
            
        elif choice == '2':
            code = input("Enter Base91 code to decode: ")
            try:
                decoded = base91.decode(code).decode('utf-8')
                result = f'"{decoded}"'
                print("Decoded text:", result)
            except Exception as e:
                print("Error decoding:", e)
        
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()