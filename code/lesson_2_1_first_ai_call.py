"""Tuition tutor: explains a topic at the student's level and shows its token cost.

Asks for a topic and a level (beginner or expert), sends them to a chat model
through LangChain's init_chat_model, then prints the answer, the total tokens
used and the time taken in seconds.
"""

from langchain.chat_models import init_chat_model

# Why: .strip() removes stray spaces so " beginner " still matches the level we expect
topic = input("Topic:   ").strip()
level = input("Level (beginner or expert): ").strip()

# The system message sets the role, uses the level, and limits the length
system_message = (
    "You are a friendly tutor at a tuition centre. "
    f"Explain the topic for a {level} student. "
    "Answer in at most 3 short sentences."
)

model = init_chat_model("llama3.2", 
model_provider="ollama",
temperature=0.2
)

response = model.invoke(
    [
        {"role": "system", "content": system_message},
        {"role": "user", "content": topic},
    ]
)

# Why: Ollama reports total_duration in nanoseconds, so divide by 1e9 for seconds
seconds = response.response_metadata["total_duration"] / 1e9
tokens = response.usage_metadata["total_tokens"]

print("=" * 40)
print(response.text)
print("=" * 40)
print(f"{tokens} tokens in {seconds:.1f} seconds")

