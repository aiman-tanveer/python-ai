"""
Lesson 08: Mini chatbot for Glow Salon

Client story: a salon answers the same questions all day. This bot
handles the common ones (timings, prices, location, appointments),
passes complaints to the manager, and counts the questions it could
not answer, so the owner can see what still needs help.
"""

BOT = "Glow Bot"
BUSINESS = "Glow Salon"

print(f"{BOT}: Hi! Ask about timings, prices, location or appointments. Type 'bye' to exit.")

# Why: ask the name once, before the loop, so we do not repeat the question
# on every message. .title() turns "sara malik" into "Sara Malik".
name = input(f"{BOT}: What is your name?  ").strip().title()
if name == "":
    name = "Guest"

total = 0       
unanswered = 0  

while True:
    # Why: clean every message once, so "  TIMINGS " and "timings" match
    message = input(f"{name}: ").strip().lower()

    # Why: an empty message is not a real question, so skip it
    # without counting it
    if message == "":
        print(f"{BOT}: Please type your question.")
        continue

    total += 1

    # Why: the complaint rule comes first. An upset customer who writes
    # "my appointment was late" must reach a human, not get a timing reply
    # just because the message also contains "appointment".
    if "late" in message or "bad" in message or "rude" in message or "complaint" in message or "refund" in message:
        print(f"{BOT}: Sorry about that. The salon manager will call you today.")
    elif message == "bye":
        print(f"{BOT}: Take care, {name}!")
        break  # leaves the while loop
    # Why: short words like "hi" must use == or .startswith(). With "in",
    # "hi" would match inside "which" or "this" and give a wrong reply.
    elif message == "hi" or message.startswith("hello") or message.startswith("salam"):
        print(f"{BOT}: Hello {name}! How can I help you?")
    elif "time" in message or "open" in message or "close" in message or "hours" in message:
        print(f"{BOT}: We are open 11 am to 9 pm, Monday to Saturday.")
    elif "price" in message or "cost" in message or "how much" in message or "rate" in message:
        print(f"{BOT}: Haircut is 1,500 PKR and facial is 3,000 PKR.")
    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: Shop 12, Main Market, Gulberg, Lahore.")
    elif "appointment" in message or "book" in message:
        print(f"{BOT}: Call or WhatsApp 0300-1234567 to book your slot.")
    else:
        # Why: count what the bot cannot answer. This list tells the
        # owner which new intents to add next.
        unanswered += 1
        print(
            f"{BOT}: I am not sure yet. In Module 2, an AI will answer: "
            f"You are the friendly assistant of {BUSINESS}. "
            f"Answer in 2 lines: {message}"
        )

print("=" * 40)
print(f"Chat summary: {total} messages, {unanswered} unanswered.")