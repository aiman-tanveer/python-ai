"""Lesson 2.4 - Batch menu description writer.

Takes a price list and asks the AI for a one-sentence description of each
product in a single run. Items with price 0 are skipped (no AI call).
At the end it prints a numbered menu and a summary of the total tokens
used and the total seconds spent.
"""

import time

from langchain_ollama import ChatOllama

# Replace with your own Module 1 business.
products = {
    "Chocolate Cake": 1500,
    "Cupcake": 250,
    "Brownie": 300,
    "Donut": 200,
    "Cheesecake Slice": 450,
    "old stock": 0,  # price 0 = not for sale, must be skipped
}

# Why: the model is created once, before the loop. Creating it inside the
# loop would reconnect for every item and waste time.
llm = ChatOllama(model="llama3.2", temperature=0.7)  # your pulled model

results = []        
total_tokens = 0    
total_seconds = 0.0  

for name, price in products.items():
    if price == 0:
        
        print(f"Skipping {name} (no price)")
        continue

    prompt = (
        f"Write one short, tasty sentence (max 20 words) describing "
        f"'{name}' for a bakery menu. Do not mention the price."
    )

    start = time.time()
    reply = llm.invoke(prompt)
    total_seconds += time.time() - start
    total_tokens += reply.usage_metadata["total_tokens"]

    results.append({"item": name, "price": price, "text": reply.content.strip()})

print("=" * 50)
for number, entry in enumerate(results, start=1):
    print(f"{number}. {entry['item']} ({entry['price']} PKR)")
    print(f"   {entry['text']}")
print("=" * 50)
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")