# Domain Language Format

The canonical glossary is `specs/domain-language.md`.

Use this structure:

```markdown
# Domain Language

Project-specific canonical terms used in specs, code, tests, and docs.

## <Optional Domain Area>

**Order**: A confirmed request from a customer for one or more products.
_Avoid_: Purchase, transaction

**Customer**: A person or organization that places orders.
_Avoid_: Client, account
```

## Rules

- Pick one canonical term when several words refer to the same concept.
- Keep definitions to one or two sentences.
- Define what the concept is, including distinctions that prevent misuse.
- Include only project-specific domain language.
- Exclude general programming and methodology terms.
- Group terms only when grouping improves navigation.
- Use `_Avoid_` for misleading or deprecated synonyms.
- Do not add a term until the developer confirms it.
- Keep terminology aligned across specs, planning notes, tests, code, and docs.
