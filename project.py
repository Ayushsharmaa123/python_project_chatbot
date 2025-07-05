def chatbot():
    print("Chatbot: Hello! I'm yout friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can i help you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple python chatbot")
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you! ")
        elif "help" in user_input:
            print("Chatbot: Sure, I'm here to help. Ask me anything ")
        elif "tell me something" in user_input:
            print("Chatbot: I'm a simple python based chatbot, i'm here to solve your problems and feel free to ask me anything.")
        elif "who is the prime minister of india" in user_input:
            print("Chatbot: Narendra modi is the prime minister of india")
        elif "who is the president of india" in user_input:
            print("Chatbot: Miss Droupadi Murmu is the president of india")
        
        else: 
            print("Chatbot: Sorry, I didn't understand that.")
            
chatbot()
