# Claude Learning Project

A CLI chatbot built with the Anthropic Python SDK — used to learn Claude Code features.

## Project Structure
- `chat.py` — main chatbot script
- `.claude/agents/` — custom subagents
- `.claude/skills/` — custom skills
- `.claude/settings.json` — hooks and permissions

## Code Standards
- Python 3.10+
- Use `python-dotenv` for all secrets — never hardcode API keys
- API key loaded via `os.environ["ANTHROPIC_API_KEY"]` from `.env`
- Model: `claude-sonnet-4-6` unless testing a specific model
- Always cap `history` to last 20 turns to avoid unbounded growth
- `max_tokens` should be set explicitly on every `client.messages.create()` call

## Anthropic SDK Patterns
- Use `client.messages.create()` for single-turn and multi-turn conversations
- Maintain conversation history as `[{"role": "user"|"assistant", "content": "..."}]`
- Handle `anthropic.APIError` for API failures
- Use `response.content[0].text` to extract reply text

## What NOT to do
- Do not commit `.env` files
- Do not log full conversation history to stdout
- Do not use raw `os.environ[]` without a fallback error message
