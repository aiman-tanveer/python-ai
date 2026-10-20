"""
Lesson 07: Conditions - AI model router

Client story: a company pays too much for AI. This router sends
private data to a local model, code questions to a strong model,
and everything else to a cheap one, then estimates the cost.
"""

# Example prices in PKR per 1K tokens (made-up numbers for practice)
CLAUDE_PRICE = 0.80
CHAT_PRICE = 0.10

task = input("Task (code / private / chat): ").strip().lower()

# input() always gives a string, so int() is needed before doing maths
tokens = int(input("Estimated tokens: "))


if task == "code":
    model = "claude (cloud, strong at code)"
    price = CLAUDE_PRICE
elif task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0
else:
    model = "haiku (cloud, cheap)"
    price = CHAT_PRICE

# Cost = (tokens / 1000) * price per 1K tokens
cost = tokens / 1000 * price

if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")