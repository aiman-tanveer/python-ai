"""
Lesson 06: clean, measure and safely size a customer question.

Customers type messy questions with extra spaces and random capitals.
Before anything goes to an AI, this script cleans the name and question,
counts characters, estimates tokens, checks for the word "python",
hides a bad word, and builds a multi-line prompt for the AI.
"""

# Example price only, not a real quote. Used for the stretch cost estimate.
price_per_1k_tokens_pkr = 2.75
bad_word = "stupid"


# --- Ask the user ---
raw_name = input("Your name: ")
raw_question = input("Your question: ")


# --- Clean the input ---
clean_name = raw_name.strip().title()
cleaned_question = raw_question.strip().capitalize()

character_count = len(cleaned_question)
estimated_tokens = round(character_count / 4)
mentions_python = "python" in cleaned_question.lower()
safe_question = cleaned_question.lower().replace(bad_word, "***").capitalize()
estimated_cost_pkr = (estimated_tokens / 1000) * price_per_1k_tokens_pkr


# --- Report ---
print("=" * 40)
print(f"Cleaned question: {cleaned_question}")
print(f"Characters: {character_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: PKR {estimated_cost_pkr:.2f} (example price)")
print("=" * 40)


# --- Build the prompt ---
prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {safe_question[:150]}"""


print(prompt)
