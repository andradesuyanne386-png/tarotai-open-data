# TarotAI Open Tarot Kit

78 English tarot card keyword summaries and 10 reflection spreads, maintained by [TarotAI](https://tarotai.art/).

[Visit the TarotAI website](https://tarotai.art/)

## Dataset mirrors

[Browse the dataset on Hugging Face](https://huggingface.co/datasets/HenryZheng99/tarotai-open-tarot-kit).

[Browse the dataset on Kaggle](https://www.kaggle.com/datasets/henryzheng99/tarotai-open-tarot-kit).

## Files

- `data/cards.json`: canonical card records (22 Major / 56 Minor Arcana).
- `data/cards.jsonl`: one card per line for dataset loaders.
- `data/cards.csv`: tabular mirror; keyword arrays are JSON encoded.
- `data/spreads.json`: 10 reflection layouts with numbered positions and journal prompts.

## Quick start

Requires Python 3.9+; no third-party dependencies.

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 examples/search.py beginnings
```

## Fields

`card_id`: stable slug; `name`: English name; `arcana`: major/minor; `suit`: null for majors, suit for minors; `number`: source numbering when provided; `locale`: en; `upright` / `reversed`: concise keyword summaries; `keywords_upright` / `keywords_reversed`: corresponding arrays; `source_url`: publisher homepage; `version`: dataset version.

Spread records contain `spread_id`, `name`, ordered `positions` (one-based index and name), `reflection_question`, `source_url`, and `version`. These are reflection layouts, not predictions.

## Provenance and methodology

Version 1.0.0, 2026-11-05. Card summaries were exported from TarotAI's existing English card configuration (`src/config/tarot-cards.ts`), without copying Tarotoo's dataset. Keywords are split on commas; no new long-form card interpretations were generated. Existing content reflects a Rider–Waite–Smith-oriented editorial tradition, not a universal or scientifically validated interpretation. The source configuration references an editorial calibration document which was not present in the checkout; independent source-by-source verification is therefore not claimed.

The 10 reflection layouts and questions were prepared with AI assistance for this release. No independent expert review is claimed. Automated checks cover record counts, required fields, unique identifiers, suit distribution and export consistency, not interpretive accuracy. No artwork, user questions, reading history, private prompts or application credentials are included.

All `source_url` fields identify the publisher homepage; they are not card-specific reference pages.

## Explore TarotAI

[TarotAI](https://tarotai.art/) offers AI tarot readings, custom card creation and journaling. Visit the homepage to explore the product behind this open dataset.

## Uses and limitations

Suitable for lookup tools, teaching prototypes, journaling and retrieval examples. Not a model-training benchmark or evidence that divination predicts events. Not medical, legal or financial advice. Interpretations vary across traditions.

## License and attribution

Data and documentation: CC BY 4.0 (see LICENSE-DATA.md). Scripts: MIT (see LICENSE). Credit [TarotAI](https://tarotai.art/), link to this repository, and indicate modifications. Artwork and the TarotAI brand are excluded.

Suggested citation: TarotAI (2026), TarotAI Open Tarot Kit, version 1.0.0, https://github.com/andradesuyanne386-png/tarotai-open-data. No DOI has been assigned.

## Contributing

Report errors with card ID, proposed correction and rationale. Edit canonical JSON, rebuild exports and run validation. Keep stable IDs. Do not submit personal reading histories or unlicensed artwork.
