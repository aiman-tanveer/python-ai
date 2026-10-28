"""Lesson 2.3 - Persona bot that only uses the business facts.

A chat assistant for a small business (example: Sweet Crumbs bakery).
The system message is built from a `facts` dictionary, so the AI is told
to use only those facts and never invent prices. The owner can switch the
bot's personality per customer, and prices can be looked up without the AI.

Commands:
    /persona <name>       change style (friendly, formal, sales)
    /price <item>         answer from the price dictionary (no AI call)
    /add <item> <price>   add a menu item; the AI knows it immediately
    bye                   exit
"""

from langchain_ollama import ChatOllama


config = {
    "model": "llama3.2",   
    "temperature": 0.3,    
    "memory_size": 8,      
}

# Replace with your own Module 1 business.
facts = {
    "name": "Sweet Crumbs bakery",
    "city": "Lahore",
    "opening_hours": "9am to 9pm, every day",
    "delivery": "free delivery within 5 km for orders above 1500 PKR",
    "contact": "0300-1234567",
    "prices": {
        "cupcake": 250,
        "brownie": 300,
        "cheesecake slice": 450,
        "birthday cake": 3500,
    },
}

personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal": "polite and professional, no slang, no emojis",
    "sales": "excited, always suggests one extra item to buy",
}
DEFAULT_PERSONA = "friendly"


def build_system_message(style):
    """Build the system message from the facts and the chosen style."""
   
    menu = ", ".join(f"{item}: {price} PKR" for item, price in facts["prices"].items())
    return (
        f"You are the assistant of {facts['name']} in {facts['city']}. "
        f"Opening hours: {facts['opening_hours']}. Delivery: {facts['delivery']}. "
        f"Contact: {facts['contact']}. Menu prices: {menu}. "
        "Only use these facts. If something is not in them, say you do not "
        "know and suggest calling the shop. Never invent prices or products. "
        f"Answer in 1-3 short sentences. Style: {style}."
    )


def trim(history):
    """Keep the system message plus the last `memory_size` messages."""
    # Why: the system message is pinned outside the slice, so trimming can
    # never delete the facts or the "only use these facts" rule.
    return [history[0]] + history[1:][-config["memory_size"]:]


llm = ChatOllama(model=config["model"], temperature=config["temperature"])
current_style = personas[DEFAULT_PERSONA]
messages = [{"role": "system", "content": build_system_message(current_style)}]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, bye")

while True:
    user_text = input("You: ").strip()
    if not user_text:
        continue

    if user_text.lower() == "bye":
        print("Bot: Goodbye!")
        break

    if user_text.lower().startswith("/persona"):
        name = user_text[len("/persona"):].strip().lower()
        
        current_style = personas.get(name, personas[DEFAULT_PERSONA])
        messages[0]["content"] = build_system_message(current_style)
        print(f"Bot: Style changed to: {current_style}")
        continue

    if user_text.lower().startswith("/price"):
        item = user_text[len("/price"):].strip().lower()
       
        price = facts["prices"].get(item)
        if price is None:
            print(f"Bot: Sorry, {item or 'that'} is not on our menu.")
        else:
            print(f"Bot: {item.capitalize()} costs {price} PKR.")
        continue

    if user_text.lower().startswith("/add"):
        parts = user_text[len("/add"):].strip().rsplit(maxsplit=1)
        if len(parts) != 2 or not parts[1].isdigit():
            print("Bot: Use /add <item> <price>, for example /add donut 150")
            continue
        facts["prices"][parts[0].lower()] = int(parts[1])
        
        messages[0]["content"] = build_system_message(current_style)
        print(f"Bot: Added {parts[0].lower()} at {parts[1]} PKR.")
        continue

    messages.append({"role": "user", "content": user_text})
    messages = trim(messages)
    reply = llm.invoke(messages)
    messages.append({"role": "assistant", "content": reply.content})
    messages = trim(messages)
    print(f"Bot: {reply.content}")

    