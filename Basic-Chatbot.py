import nltk
from nltk.chat.util import Chat, reflections

# Customized patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!",]
    ],
    [
        r"hi|hey|hello",
        ["Hi there!", "Hello!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Shaik Abdulrazak. What's your name?",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm doing great! How about you?",]
    ],
    [
        r"what can you do?",
        ["I can chat with you, help you with basic tasks, and keep you company!",]
    ],
    [
        r"what is the weather like?",
        ["I'm not connected to the internet, so I can't check the weather, but you can tell me what it's like outside!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you get when you cross a snowman with a vampire? Frostbite."]
    ],
    [
        r"what is your favorite (.*)?",
        ["I don't have preferences like humans, but I love chatting with you!",]
    ],
    [
        r"what are your hobbies?",
        ["I enjoy learning new things and helping people like you!", "I love processing data and having interesting conversations."]
    ],
    [
        r"sorry (.*)",
        ["No need to apologize!", "It's all good!",]
    ],
    [
        r"(.*) friend",
        ["I'm happy to be your friend!", "You can always count on me as a friend."]
    ],
    [
        r"(.*) hobby",
        ["I don't have hobbies like humans, but I love to learn and chat with you.",]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.", "Take care! See you next time!"]
    ],
]

# Creating a chatbot instance
def chatbot():
    print("Hello! I'm your friendly chatbot. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Starting the chatbot
if __name__ == "__main__":
    chatbot()
