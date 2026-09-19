# Assembly Minute

The meeting is temporary. The record should not be.

Assembly Minute is a GenLayer primitive for publishing a motion outcome without erasing reservations, owners, or the right to object.

## Record lifecycle

| Phase | Authorized actor | Invariant |
|---|---|---|
| `OPEN` | secretary | motion and independent reviewer are frozen |
| `ADOPTED` | secretary | outcome, reservations, and action owner are explicit |
| `PUBLISHED` | secretary + validator consensus | public minute faithfully reflects every frozen field |
| `OBJECTED` | any participant | evidence URL lands within five days of publication |
| `RECONCILED` | assigned reviewer | corrected record is attributable |
| `FINAL` | anyone | possible only after an unobjectionable publication window |

Notice where the clock begins: `published_at`. A slow secretary cannot consume the community's objection time before the minute is visible.

## Audit the primitive

- `contracts/contract.py` — state machine and nondeterministic fidelity check
- `tests/direct/` — role separation and repair path
- `evidence/` — a minute and a distinct objection record
- `docs/` — circular chamber and chronological tape
- `deployment.json` — exact StudioNet address and transaction receipts

Run `pytest -q` and `ruff check contracts tests`. The UI is intentionally a chamber/tape composition and never acts as an alternate source of truth.
