"""
Model profile card with a per-chat cost estimate.

A client asks: "Which AI model should we use, and what will it cost per chat?"
This script stores one model's profile using the four basic Python types
(str, int, float, bool), prints each value with its type, then asks how many
tokens a typical chat uses and estimates the cost in PKR.
"""


# --- Model profile (one value for each of the 4 types) ---
model_name = "gemma 3:1b"          # str
context_window_tokens = 128000       # int
price_per_1k_tokens_pkr = 2.75       # float (example price, not a real quote)
runs_locally = True                  # bool


# --- Profile card ---
print("=== MODEL PROFILE CARD ===")
print(f"Model name:        {model_name} | type: {type(model_name)}")
print(f"Context window:    {context_window_tokens} tokens | type: {type(context_window_tokens)}")
print(f"Price per 1K tok:  PKR {price_per_1k_tokens_pkr} | type: {type(price_per_1k_tokens_pkr)}")
print(f"Runs locally:      {runs_locally} | type: {type(runs_locally)}")

# --- Cost estimate ---
tokens_per_chat = int(input("\nHow many tokens does one chat use? "))

# Divide by 1000 because the price is quoted per 1K tokens, not per single token.
estimated_cost_pkr = round((tokens_per_chat / 1000) * price_per_1k_tokens_pkr, 2)

print(f"\nEstimated cost per chat: PKR {estimated_cost_pkr}")

