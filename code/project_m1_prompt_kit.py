"""
project_m1_prompt_kit.py

AI Prompt Kit: a small tool for local business owners and the digital agencies
that work with them. It asks a few questions about the business and then builds
three ready-to-use AI prompts (marketing, customer service, growth) that can be
pasted into any AI chat, like Ollama.
"""

# Five separate answers let us reuse each detail in several prompts,
# so the owner answers once and gets three tailored prompts.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
main_customers = input("Main customers: ")

# input() always returns text, so int() is needed to use the budget as a number.
budget = int(input("Monthly budget (PKR): "))


# Building the separator once avoids typing 45 "=" signs by hand
# and keeps every section visually consistent.
line = "=" * 41
print(line)
print(f"   AI Prompt Kit for {business_name}")
print(line)


# Each prompt gets its own variable so it can be printed, copied,
# or tested in Ollama separately.
prompt_marketing = (
    f"Write a social media post idea for {business_name}, a {business_type} in {city}. "
    f"The post should attract {main_customers} and feel friendly and local."
)

prompt_service = (
    f"Write a polite reply to an unhappy customer of {business_name}, "
    f"a {business_type} in {city}. "
    f"Apologize sincerely, offer a solution, and keep the tone respectful for {main_customers}."
)

prompt_growth = (
    f"Suggest 3 low-cost AI ideas for a {business_type} in {city} "
    f"whose main customers are {main_customers}. "
    f"Keep every idea within a budget of {budget} PKR per month."
)

print("\n--- Prompt 1: Marketing ---")
print(prompt_marketing)

print("\n--- Prompt 2: Customer Service ---")
print(prompt_service)

print("\n--- Prompt 3: Growth ---")
print(prompt_growth)

print()
print(line)