def chatbot():
    while True:
        user = input("You: ").lower()
        if user in ["hello", "hi"]:
            print("Bot: Hi there!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! How can I help?")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
