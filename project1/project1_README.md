# Project 1: Rule-Based AI Chatbot
**DecodeLabs | Artificial Intelligence — Industrial Training Kit | Batch 2026**

**File:** `ruleBasedChatbot.py`

---

## Goal
Create a simple rule-based chatbot that responds to predefined user inputs using explicit control flow logic.

## Key Requirements
- Handle greetings and exit commands
- Use decision-making logic for responses
- Run in a continuous loop

## Key Skills
Control flow, decision-making logic, basic AI concepts

## Technologies Used
- Python 3 (no external libraries required)

## How It Works
- Runs inside a continuous `while` loop that keeps the chatbot active until an exit command is given
- Sanitizes user input (`.lower().strip()`) to handle inconsistent casing/whitespace
- Uses a dictionary-based knowledge base (40+ predefined intents covering greetings, small talk, AI/Python concepts, and project-related questions) with `.get()` for fast lookup and a built-in fallback response for unrecognized input
- Cleanly exits the loop using a `break` statement on exit commands (`bye`, `exit`, `quit`, `goodbye`)

## How to Run
```bash
python ruleBasedChatbot.py
```

## Sample Output
```
============================================================
RULE-BASED AI CHATBOT
============================================================
Hello! I am RuleBot, your simple AI chatbot.
You can ask me about AI, Python, chatbots, or this project.
Type 'bye', 'exit', or 'quit' whenever you want to leave.
============================================================

You: hi
Bot: Hello! How can I help you?

You: what is ai
Bot: AI stands for Artificial Intelligence. It is the field of creating systems that can perform tasks that normally require human intelligence.

You: bye
Bot: Goodbye! Have a great day.

Thank you for using RuleBot!
```

---

## Author
**Aliza**
AI 473 — Deep Learning Coursework
DecodeLabs Industrial Training Kit, Batch 2026
