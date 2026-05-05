---
name: chat-review
description: Reviews chat.py against Claude API best practices. Use when you want to check if the chatbot code follows Anthropic SDK patterns, handles errors properly, and avoids common pitfalls like unbounded history or missing max_tokens.
---

Review `chat.py` against these Claude API best practices:

1. Read the file with the Read tool
2. Check each item below and report Pass / Fail / Warning:

**API Usage**
- [ ] `max_tokens` explicitly set on every `messages.create()` call
- [ ] Model name is current (claude-sonnet-4-6 or newer)
- [ ] `APIError` exception handling present

**History Management**
- [ ] Conversation history capped (max 20 turns recommended)
- [ ] Both user and assistant turns appended correctly

**Security**
- [ ] API key loaded from environment, not hardcoded
- [ ] `.env` file used via `python-dotenv`

**UX**
- [ ] Empty input handled (skip blank messages)
- [ ] Exit command implemented (`quit` or similar)

Report findings as a checklist with a short fix for each Fail/Warning item.
