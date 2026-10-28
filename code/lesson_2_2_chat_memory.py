"""Lesson 2.2 - Tutor with bounded chat memory.

The tutor remembers the conversation by sending the running `messages`
list to the model on every turn. To stop the cost from growing forever,
only the system message plus the last 8 messages are kept.

Commands:
    bye     exit the program
    /reset  clear memory but keep the system message
    /count  print how many messages are in memory

After every answer the number of input tokens sent to the model is printed.
"""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

MODEL_NAME = "llama3.2" #
MAX_HISTORY = 8          

llm = ChatOllama(model=MODEL_NAME)

SYSTEM_PROMPT = (
    "You are a friendly tutor at a learning centre. "
    "Keep every answer to 2-3 short sentences."
)

 
messages = [SystemMessage(content=SYSTEM_PROMPT)]

# Stretch: only the user's questions, kept separately from the trimmed memory.
questions = []


def trim(history):
    """Keep the system message plus the last MAX_HISTORY messages."""
    
    return [history[0]] + history[1:][-MAX_HISTORY:]


print("Tutor: Ask me anything. Commands: /reset, /count, bye")

while True:
    user_text = input("You: ").strip()
    if not user_text:
        continue

    if user_text.lower() == "bye":
        print("Tutor: Goodbye!")
        break

    if user_text == "/reset":
        
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
        continue

    if user_text == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue

    # Why: the model is stateless. It only "remembers" what we send it, so
    # the user message must be in the list before we call invoke().
    messages.append(HumanMessage(content=user_text))
    questions.append(user_text)
    messages = trim(messages)

    reply = llm.invoke(messages)
    messages.append(AIMessage(content=reply.content))
    messages = trim(messages)

    print(f"Tutor: {reply.content}")
    print(f"       (tokens sent: {reply.usage_metadata['input_tokens']})")

# Stretch: session summary of the questions asked.
if questions:
    print(f"\nQuestions asked: {len(questions)}")
    print(f"First question: {questions[0]}")
    print(f"Last question: {questions[-1]}")