import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thanks!']),
    (r'what is your name?', ['I am a Aditya.', 'My name is Aditya.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'i love you',['Thank you for your kind words! Im just a computer program, so I dont have feelings']),
    (r'i hate you',['i am really sorry for my mistakes']),
    (r'who are you',['i am a computer program to help you']),
]


chatbot = Chat(patterns, reflections)
def start_chat():
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("-----HELLOW ! FRIENDS || I AM ADITYA-----")
    print("-----------------------------------------")
    print("-----------------------------------------")
    chatbot.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    start_chat()