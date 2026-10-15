"""
lesson_04_print_input.py

A tiny tool for a digital agency. The user enters their name, business type,
one problem the business faces, and a monthly budget in PKR. The tool prints
a welcome line and builds a ready-to-use AI prompt that can be pasted into
any AI chat (like Ollama).
"""

# Asking for three separate values lets us reuse each one in the welcome
# line and in the prompt without retyping anything.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# input() always returns text, so int() turns the budget into a real number.
budget = int(input("Monthly budget (PKR): "))

print(f"\nWelcome, {name}!")

# Using a template means the agency can reuse the same prompt shape
# for any client without rewriting it by hand each time.
prompt = (
    f"Suggest 3 AI solutions for a {business} that struggles with {problem}. "
    f"Budget: {budget} PKR per month."
)

print("--- Your AI Prompt ---")
print(prompt)

