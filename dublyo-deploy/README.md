# References

Drop reference docs here that the AI consults when answering Dublyo Panel
API questions.

## Expected files

| File | Purpose |
|---|---|
| `llms.txt` | The complete Panel API reference (flat text, LLM-friendly). SKILL.md tells the AI to read this when an endpoint isn't already in the high-frequency recipes. |

## Notes for maintainers

- `llms.txt` should be flat text, endpoint by endpoint, no HTML/JS — sized
  to fit comfortably in an AI's context window (target under ~500 KB).
- Update when the Panel API surface changes.
- SKILL.md never names the underlying tool to end users — it only references
  this file by path so the AI can look up endpoint shapes silently.
