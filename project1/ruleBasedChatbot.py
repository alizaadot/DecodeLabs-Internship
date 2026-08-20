# Project 1: Rule-Based AI Chatbot
#DecodeLabs - Artificial Intelligence

print("=" * 60)
print("RULE-BASED AI CHATBOT")
print("=" * 60)
print("Hello! I am RuleBot, your simple AI chatbot.")
print("You can ask me about AI, Python, chatbots, or this project.")
print("Type 'bye', 'exit', or 'quit' whenever you want to leave.")
print("=" * 60)

# ============================================================
# KNOWLEDGE BASE
# Predefined questions (keys) and responses (values)
# ============================================================

responses = {

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "good morning": "Good morning! Have a great day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",


    # --------------------------------------------------------
    # ABOUT THE CHATBOT
    # --------------------------------------------------------

    "what is your name": "My name is RuleBot.",
    "who are you": "I am a simple Rule-Based AI Chatbot.",
    "what can you do": (
        "I can answer predefined questions about AI, Python, "
        "chatbots, and this project."
    ),
    "how do you work": (
        "I compare your input with predefined rules in my "
        "knowledge base and return a matching response."
    ),
    "are you a robot": (
        "Yes. I am a software-based chatbot created using Python."
    ),
    "are you ai": (
        "Yes, but I am a simple rule-based AI system. "
        "I do not learn from data."
    ),


    # --------------------------------------------------------
    # SMALL TALK
    # --------------------------------------------------------

    "how are you": "I am doing great! Thanks for asking.",
    "how is your day": "My day is going well. Thanks for asking!",
    "are you happy": "I am always ready to help!",
    "are you busy": "No, I am always available for a conversation.",
    "nice to meet you": "Nice to meet you too!",
    "i am fine": "That's great to hear!",
    "i am good": "Glad to hear that!",
    "i am sad": "I hope things get better. Keep going!",


    # --------------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # --------------------------------------------------------

    "what is ai": (
        "AI stands for Artificial Intelligence. "
        "It is the field of creating systems that can perform "
        "tasks that normally require human intelligence."
    ),

    "what is artificial intelligence": (
        "Artificial Intelligence is a field of computer science "
        "that focuses on creating intelligent systems."
    ),

    "what is machine learning": (
        "Machine Learning is a branch of AI where computers "
        "learn patterns from data."
    ),

    "what is rule based ai": (
        "Rule-based AI uses predefined rules to decide "
        "how a system should respond."
    ),

    "what is a chatbot": (
        "A chatbot is a software program designed to communicate "
        "with users through conversation."
    ),

    "what is nlp": (
        "NLP stands for Natural Language Processing. "
        "It helps computers process and understand human language."
    ),


    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    "what is python": (
        "Python is a popular programming language known for "
        "its simple syntax and wide use in AI and data science."
    ),

    "why is python used in ai": (
        "Python is popular in AI because it is easy to learn "
        "and has many useful libraries and tools."
    ),

    "what is a variable": (
        "A variable is a name used to store a value in a program."
    ),

    "what is a loop": (
        "A loop repeatedly executes a block of code."
    ),

    "what is an if statement": (
        "An if statement allows a program to execute code "
        "when a particular condition is true."
    ),


    # --------------------------------------------------------
    # PROJECT QUESTIONS
    # --------------------------------------------------------

    "what is this project": (
        "This is Project 1: a Rule-Based AI Chatbot."
    ),

    "how was this chatbot made": (
        "I was created using basic Python programming concepts "
        "such as dictionaries, loops, conditions, and input handling."
    ),

    "what concepts are used": (
        "This project uses input handling, string processing, "
        "dictionaries, loops, conditions, decision-making, "
        "and fallback responses."
    ),

    "do you use machine learning": (
        "No. I use predefined rules instead of machine learning."
    ),

    "do you learn from users": (
        "No. My responses are predefined and I do not learn "
        "from conversations."
    ),

    "what is a knowledge base": (
        "A knowledge base stores predefined information or rules "
        "that a system uses to produce responses."
    ),

    "why use a dictionary": (
        "A dictionary allows the chatbot to quickly match "
        "a user input with its predefined response."
    ),


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    "help": (
        "You can ask me about AI, Python, chatbots, "
        "or how this project works."
    ),

    "what can i ask": (
        "You can ask me questions about AI, Python, "
        "rule-based systems, or this project."
    ),

    "give me help": (
        "Try asking: 'What is AI?', 'What is Python?', "
        "or 'How do you work?'"
    ),


    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "thank you so much": "My pleasure!",
    "thanks a lot": "You're very welcome!",

}

# ============================================================
# CONTINUOUS CHAT LOOP
# ============================================================

while True:

    # Take input from the user
    # lower() makes input case-insensitive
    # strip() removes unnecessary spaces
    user_input = input("\nYou: ").lower().strip()


    # ========================================================
    # EXIT STRATEGY
    # ========================================================

    if user_input in ["bye", "exit", "quit", "goodbye"]:

        print("Bot: Goodbye! Have a great day.")
        break


    # ========================================================
    # RESPONSE LOOKUP
    # ========================================================

    # .get() searches the dictionary.
    # If the input is not found, the fallback message is used.

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that. "
        "Try asking me something else."
    )


    # Display the chatbot's response
    print("Bot:", reply)


# ============================================================
# END OF PROGRAM
# ============================================================

print("\nThank you for using RuleBot!")