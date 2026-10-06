# nova-gig-kit

A complete, field-validated Fiverr gig kit for selling AI automation to
vacation-rental hosts: profile bio, gig title, tags, three priced packages,
description, FAQ, and buyer requirements.

```bash
python kit.py
# ALL FIELDS VALID ✅  (or it names the field that overflows)
```

Every string is validated against Fiverr's real field limits (title 80,
description 1200, tags 5×20, bio 600, FAQ 70/300) — nothing gets silently
truncated on paste. Currently live and selling.

Maintained in Nova by `n8n_agent` (delivers the automation orders this gig
sells). Extracted from the Nova monorepo as a portfolio piece.
