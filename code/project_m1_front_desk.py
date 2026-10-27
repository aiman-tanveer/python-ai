"""Sweet Crumbs Desk: AI front desk for Sweet Crumbs bakery (Lahore).

Answers common questions with free rules, gives exact price quotes
(bulk discount + delivery fee), and turns every other question into a
cost-checked AI prompt. Private questions go to a local model.
Ends with a session report for the owner.

Module 1 tools only: no lists, dictionaries, for loops or functions.
"""

# Constants in UPPER_CASE: the owner can change a price rule in one place
BOT_NAME = "Sweet Crumbs Desk"
BUSINESS = "Sweet Crumbs bakery"
DELIVERY_FEE = 200           
FREE_DELIVERY_LIMIT = 3000    
BULK_MIN_QTY = 10
BULK_DISCOUNT = 0.10         
CLOUD_PRICE_PER_1K = 0.1      
LOCAL_MODEL = "llama3.2"
MAX_QUESTION_CHARS = 150

print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

# Ask the name once, before the loop, so we do not ask on every message
name = input(f"{BOT_NAME}: What is your name? ").strip().title()
if name == "":
    name = "Customer"

# Counters start before the loop; inside it they would reset every message
messages = 0
answered = 0
unanswered = 0
quotes = 0
quoted_value = 0
ai_cost = 0.0

while True:
    text = input(f"{name}: ").strip().lower()

    if text == "":
        print(f"{BOT_NAME}: Please type a question, /quote, or bye.")

   
    elif "refund" in text or "complaint" in text or " late" in " " + text:
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")

    elif text == "bye":
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Goodbye, {name}!")
        break

    elif text == "/quote":
        messages += 1
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        qty_text = input(f"{BOT_NAME}: How many? ").strip()

        # Price 0 means "not on the menu"
        price = 0
        if item == "cupcake":
            price = 250
        elif item == "brownie":
            price = 300
        elif item == "chocolate cake":
            price = 1500

        if price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
        elif not qty_text.isdigit():
            
            print(f"{BOT_NAME}: Please type the quantity as a whole number.")
        else:
            quantity = int(qty_text)
            if quantity == 0:
                print(f"{BOT_NAME}: The quantity must be at least 1.")
            else:
                subtotal = price * quantity

                discount = 0
                if quantity >= BULK_MIN_QTY:
                    discount = round(subtotal * BULK_DISCOUNT)

                
                after_discount = subtotal - discount
                if after_discount >= FREE_DELIVERY_LIMIT:
                    delivery = 0
                    delivery_text = "FREE"
                else:
                    delivery = DELIVERY_FEE
                    delivery_text = f"{delivery:,} PKR"

                total = after_discount + delivery
                quotes += 1
                quoted_value += total
                print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
                print(f"     Discount: -{discount:,} PKR | Delivery: {delivery_text}")
                print(f"     Total: {total:,} PKR")

    
    elif (text == "hi" or text.startswith("hi ") or text.startswith("hello")
          or text.startswith("salam") or text.startswith("assalam")):
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Hello, {name}! How can we help you today?")

    elif "hour" in text or "open" in text or "close" in text:
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")

    elif "location" in text or "located" in text or "where are you" in text:
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Visit us at our Lahore shop, or order for delivery.")

    elif "deliver" in text:
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Delivery costs {DELIVERY_FEE:,} PKR, free for orders "
              f"from {FREE_DELIVERY_LIMIT:,} PKR.")

    elif "price" in text or "menu" in text or "how much" in text:
        messages += 1
        answered += 1
        print(f"{BOT_NAME}: Cupcake 250, brownie 300, chocolate cake 1,500 PKR. "
              "Type /quote for an exact price.")

    else:
        
        messages += 1
        unanswered += 1

        question = text.capitalize()[:MAX_QUESTION_CHARS]
       
        tokens = round(len(question) / 4)

        
        if "phone" in text or "cnic" in text or "my address" in text:
            model = f"{LOCAL_MODEL} (local, private)"
            cost = 0
        else:
            model = "small cloud model (cheap)"
            cost = tokens / 1000 * CLOUD_PRICE_PER_1K
        ai_cost += cost

        prompt = f"""You are the assistant of {BUSINESS}.
Answer {name} in 2 short lines. Do not invent prices or timings.
Question: {question}"""

        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{tokens} tokens)")
        print(f"     Prompt: {prompt}")

print("=" * 50)
print("Session report")
print(f"Messages: {messages} | Answered by rules: {answered} | Unanswered: {unanswered}")
print(f"Quotes: {quotes} | Quoted value: {quoted_value:,} PKR")
print(f"Estimated AI cost for unanswered questions: {ai_cost:.4f} PKR")
print("=" * 50)