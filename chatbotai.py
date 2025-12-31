import google.generativeai as genai

genai.configure(api_key="AIzaSyCjJ1r432k3FCHGwsWpsVExsDFUrteJtpc")

apple = genai.GenerativeModel("gemini-2.5-flash")

chat = apple.start_chat(history=[])

print("hi !! i'am Apple the chat-bot")

while True:
    user_input = input("user:")

    if user_input.lower() == "bye":
        break

    response = chat.send_message(user_input)
    print("Apple:",response.text)
