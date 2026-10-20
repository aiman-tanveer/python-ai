# python-ai learning

**Name:** Aiman Tanveer
**Course:** AI For Everyone

## My AI Goal
I want to become an AI Developer who builds AI tools that help local businesses save time.

## How to Run
uv run lesson_04_print_input.py

## Lessons Done So Far
- [x] Lesson 1: Python variables and f-strings (name, dream AI role, business problem, city)
- [x] Lesson 2: Dev toolkit setup and versions (`lesson_02_toolkit.py`)
- [x] Ollama first chat with `gemma3:1b` (`docs/ollama-first-chat.md`)
- [x] Lesson 4: `lesson_04_print_input.py` with input(), f-string prompt builder and monthly budget with `int()`
- [x] Prompt test with Ollama (`docs/prompt-test.md`)
- [x] MCQs answers is put in (`docs/my-answers-module-1.md`)
- [x] Project M1: `code/project_m1_prompt_kit.py` AI Prompt Kit with 5 inputs and 3 prompts

# AI Course Practice

Small Python practice projects, one section per lesson.

- [Lesson 07: Model router](#lesson-07-model-router)
- [Lesson 08: Glow Salon mini chatbot](#lesson-08-glow-salon-mini-chatbot)

---

## Lesson 07: Model router

File: `code/lesson_07_conditions.py`

**Client story:** A company pays too much for AI. This router sends private
data to a local model, code questions to a strong model, and everything else
to a cheap one, then estimates the cost.

### Routing table

Prices are example numbers in PKR per 1K tokens.

| Task type | Model | Price per 1K tokens |
|-----------|-------|---------------------|
| `code` | claude (cloud, strong at code) | 0.80 |
| `private` | llama3.2 (local, Ollama) | 0 (runs on our own machine) |
| anything else (`chat`) | haiku (cloud, cheap) | 0.10 |

Cost formula: `cost = tokens / 1000 * price`

If tokens are over 4000, the program prints a warning. Otherwise it prints
`Length is fine.`

### How to run

```
python code/lesson_07_conditions.py
```

### Example runs

```
Task (code / private / chat): Code
Estimated tokens: 5000
Warning: long request, consider shortening it.
Chosen model: claude (cloud, strong at code)
Estimated cost: 4.00 PKR
```

```
Task (code / private / chat): private
Estimated tokens: 800
Length is fine.
Chosen model: llama3.2 (local, Ollama)
Estimated cost: 0.00 PKR
```

### Notes

- The task type is cleaned with `.strip().lower()`, so `" Code "` still works.
- Tokens are converted with `int()` because `input()` always returns text.
- `if / elif / else` covers all three task types. The `else` branch also
  catches unexpected input, so the cheap model is the safe default.
- The cost is printed with `:.2f` (2 decimals).

---

## Lesson 08: Glow Salon mini chatbot

File: `code/lesson_08_mini_chatbot.py`

A small rule-based chatbot for a local salon. It answers common questions,
sends complaints to the manager, and counts the questions it cannot answer.

### Design table

Rules are checked from top to bottom, so the complaint rule is first.

| # | Intent (what the user wants) | Keywords to look for | Reply |
|---|------------------------------|----------------------|-------|
| 1 | Complaint / human help | `late`, `bad`, `rude`, `complaint`, `refund` | Sorry about that. The salon manager will call you today. |
| 2 | Greeting | `hi` (exact), starts with `hello` or `salam` | Hello {name}! How can I help you? |
| 3 | Timings | `time`, `open`, `close`, `hours` | We are open 11 am to 9 pm, Monday to Saturday. |
| 4 | Prices | `price`, `cost`, `how much`, `rate` | Haircut is 1,500 PKR and facial is 3,000 PKR. |
| 5 | Location | `where`, `location`, `address` | Shop 12, Main Market, Gulberg, Lahore. |
| 6 | Appointment | `appointment`, `book` | Call or WhatsApp 0300-1234567 to book your slot. |
| 7 | Exit | `bye` (exact) | Take care, {name}! |
| 8 | Fallback | anything else | Counts as unanswered and prints the AI prompt for Module 2. |

### How to run

```
python code/lesson_08_mini_chatbot.py
```

### Notes

- Every message is cleaned with `.strip().lower()`.
- Short words like `hi` use `==` or `.startswith()`, not `in`, so "which" does not match.
- The summary at the end shows the message count and the unanswered count.