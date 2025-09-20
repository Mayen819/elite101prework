def chatbot():
    print(" Welcome to the PreWork Chatbot!")

    name = input("What is your name? ")
    age = input("How old are you? ")

    print(f"Nice to meet you, {name}! You are {age} years old.")

    print("\nHow can I help you today?")

    while True:
        print("\nPlease choose an option:")
        print("1. Store hours")
        print("2. Store location")
        print("3. Available products")
        print("4. Prices")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("Our store hours are 9 AM - 9 PM.")
        elif choice == "2":
            print("We are located at 123 Main Street.")
        elif choice == "3":
            print("We currently offer clothing, shoes, and accessories.")
        elif choice == "4":
            print("Prices deppends on the product. Please check in-store or online.")
        elif choice == "5":
            print(f"Goodbye, {name}! Thanks for chatting. ")
            break
        else:
            print("Sorry, I didn’t understand that. Please try again.")

chatbot()
