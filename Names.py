words = []

while True:
    user_input = input("Enter a word (or type 'quit' to stop): ").strip()

    if user_input.lower() == "quit":
        break
    else:
        words.append(user_input)
        
print("\nYou entered the following words:")
for w in words:
    print("-", w)

check = input("\nWould you like to check if a word exists in the list? (yes/no): ").strip().lower()

if check == "yes":
    search_word = input("Enter the word you want to search for: ").strip()
    if search_word in words:
        print(f"'{search_word}' is in the list.")
    else:
        print(f"'{search_word}' was not found on the list.")
else:
    print("Okay, no word search was needed.")
