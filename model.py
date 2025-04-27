from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the pretrained model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

# Main chat loop
print("Chatbot is running! Type 'exit' to end the conversation.\n")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Update conversation history
    conversation_history.append(user_input)

    # Prepare the input for the model
    # Combine conversation history into one string
    history_string = " ".join(conversation_history)
    inputs = tokenizer(history_string, return_tensors="pt", truncation=True, max_length=512)

    # Generate a response from the model
    outputs = model.generate(inputs["input_ids"], max_length=100, num_beams=3, early_stopping=True)
    
    # Decode and print the model's response
    bot_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Chatbot: {bot_response}")

    # Add the bot's response to conversation history
    conversation_history.append(bot_response)
