"""
Model profile card with per-chat and monthly cost estimates.

A client asks: "Which AI model should we use, and what will it cost per chat?"
This script stores one model's profile using the four basic Python types
(str, int, float, bool), prints each value with its type, then asks how many
tokens a chat uses and how many chats happen per day. It estimates the cost
per chat and for a 30-day month, in PKR.
"""

# --- Model profile (one value for each of the 4 types) ---
model_name = "gemma3:1b"             
context_window_tokens = 32768        
price_per_1k_tokens_pkr = 2.75       
runs_locally = True                  

days_per_month = 30                 

# --- Profile card ---
print("=== MODEL PROFILE CARD ===")
print(f"Model name:        {model_name} | type: {type(model_name)}")
print(f"Context window:    {context_window_tokens} tokens | type: {type(context_window_tokens)}")
print(f"Price per 1K tok:  PKR {price_per_1k_tokens_pkr} (example price) | type: {type(price_per_1k_tokens_pkr)}")
print(f"Runs locally:      {runs_locally} | type: {type(runs_locally)}")


# --- Questions for the client ---
tokens_per_chat = int(input("\nHow many tokens does one chat use? "))
chats_per_day = int(input("How many chats per day? "))


# --- Cost estimate ---
cost_per_chat_pkr = (tokens_per_chat / 1000) * price_per_1k_tokens_pkr


monthly_cost_pkr = cost_per_chat_pkr * chats_per_day * days_per_month

print(f"\nEstimated cost per chat:  PKR {round(cost_per_chat_pkr, 2)}")
print(f"Estimated monthly cost ({days_per_month} days, {chats_per_day} chats/day): PKR {round(monthly_cost_pkr, 2)}")
print("Note: prices are examples only, not a real quote.")

