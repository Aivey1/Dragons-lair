# AI Chatbot Program
# This is a simple chatbot that responds to basic questions from the user.

# Define the chatbot's name
chatbot_name = "AlBot"

def chatbot_response(user_input):
    """
    This function takes user input as a parameter and returns an appropriate response based on keywords in the input.
    """
   
    # Convert the input to lowercase to make it case-insensitive
    user_input = user_input.lower()
   
    # Responses based on specific keywords
    if "name" in user_input:
        return f"My name is {chatbot_name}! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but thanks for asking! How can I help you today?"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! It was nice talking to you."
    else:
        return "I'm sorry, I didn't understand that. Could you ask something else?"

# Main loop to keep the conversation going
print(f"Hello! I am {chatbot_name}. Feel free to ask me anything, or type 'bye' to exit.")
while True:
    # Get user input
    user_input = input("You: ")
   
    # Get the chatbot's response
    response = chatbot_response(user_input)
   
    # Print the chatbot's response
    print(f"{chatbot_name}: {response}")
   
    # Break the loop if the user says "bye" or "exit"
    if "bye" in user_input or "exit" in user_input:
        break