# Module 1 Project: Design (Sweet Crumbs Desk)

**Business:** Sweet Crumbs bakery, Lahore
**Problem:** Staff answer the same questions all day and make mistakes on price quotes.

## 1. Intents

Rules are checked from top to bottom, and the first match wins.

| # | Intent | Keywords | Reply |
|---|---|---|---|
| 1 | Complaint | refund, complaint, late (checked as `" late"` so it does not match "chocolate") | Sorry about that. A manager will call you within 1 hour. |
| 2 | Goodbye | `bye` (exact match) | Goodbye, name! Then the session report prints. |
| 3 | Quote | `/quote` (exact match) | Ask item and quantity, then print the price calculation |
| 4 | Greeting | `hi`, starts with `hi `, `hello`, `salam`, `assalam` (checked with `==` / `.startswith()`, not `in`) | Hello, name! How can we help you today? |
| 5 | Hours | hour, open, close | We are open 9 am to 10 pm, every day. |
| 6 | Location | location, located, where are you | Visit us at our Lahore shop, or order for delivery. |
| 7 | Delivery | deliver | Delivery costs 200 PKR, free for orders from 3,000 PKR. |
| 8 | Prices | price, menu, how much | Cupcake 250, brownie 300, chocolate cake 1,500 PKR. Type /quote for an exact price. |
| 9 | Fallback | anything else | Cleaned question, token estimate, routed to a model, AI-ready prompt |

## 2. Business Rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250 PKR, brownie 300 PKR, chocolate cake 1,500 PKR |
| Unknown item | "Sorry, (item) is not on our menu." |
| Bulk discount | 10% off the subtotal for 10 or more items |
| Delivery | 200 PKR, free when the price after discount is 3,000 PKR or more |
| Rule order | Discount first, then delivery is judged on the discounted amount |
| Private words | phone, cnic, my address |
| Private routing | Local model (llama3.2), cost 0 PKR |
| Other routing | Small cloud model, estimated at 0.1 PKR per 1K tokens |
| Question limit | Cut to 150 characters |
| Token estimate | characters / 4, rounded |

## 3. Rule Tests

Run every row and fill in the "Pass?" column honestly.

| You type | Expected | Pass? |
|---|---|---|
| `  WHAT are your hours  ` | Hours (capitals and spaces handled) | |
| `which cake is best?` | Fallback, **not** a greeting ("hi" hides in "which") | |
| `do you have chocolate cake?` | Fallback, **not** a complaint ("late" hides in "chocolate") | |
| `my order is late` | Manager reply (complaint rule first) | |
| `/quote`, 1 chocolate cake | Delivery fee charged (1,500 + 200 = 1,700 PKR) | |
| `/quote`, 3 chocolate cakes | Delivery free (4,500 PKR, no discount) | |
| `/quote`, 12 cupcakes | Discount applied: 3,000 - 300, delivery still charged, total 2,900 PKR | |
| `/quote`, pizza | "Not on our menu", no crash | |
| `/quote`, brownie, quantity `abc` | Polite message, no crash | |
| `can I change my phone number on the order?` | Routed to local model, cost 0 | |
| Press Enter with no text | Asks again, not counted as a message | |
| `BYE` | Goodbye + session report | |