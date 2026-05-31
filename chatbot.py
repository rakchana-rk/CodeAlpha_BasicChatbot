def chatbot():
    print("=" * 40)
    print("      BASIC CHATBOT")
    print("=" * 40)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")
        elif user_input == "how are you":
            print("Bot: I'm doing well, thank you.")
        elif user_input == "what is your name":
            print("Bot: I am a Python ChatBot.")
        elif user_input == "help":
            print("Bot: You can say hello, ask my name, or ask how I am.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
