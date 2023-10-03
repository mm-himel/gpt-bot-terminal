import openai

openai.api_key = "API KEY"

# Initialize an empty list for store conversation
conversation = []

#loop for continuing conversation
while True:
    user_input = input("Himel: ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    # Generate a response from the model
    compleation = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":user_input}]
    )

    # Extract and print the reply
    reply = compleation.choices[0].message.content
    print ("AI: " + reply)

    conversation.append ({"role":"user","content":reply})