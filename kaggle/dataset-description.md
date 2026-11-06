## About this dataset
Published by [TarotAI](https://tarotai.art/): 78 English tarot card keyword summaries and 10 reflection spreads for lookup tools, educational prototypes and journaling.

## Contents
- cards.csv: 78 rows; keyword arrays are JSON encoded.
- cards.json: identical structured card records, preserving arrays.
- spreads.json: 10 reflection layouts with numbered positions and journal prompts.
- README.md: field guide, provenance and reuse terms.
- LICENSE-DATA.md: CC BY 4.0 data license.

## Fields
card_id is a stable slug; name is the English card name; arcana is major/minor; suit is blank/null for majors; number is source numbering where provided; locale is en; upright and reversed are concise keyword summaries; keywords_upright and keywords_reversed are arrays; source_url identifies the publisher homepage, not a card-specific citation; version is the dataset version.

## Provenance and quality
Card text was exported from TarotAI's existing English card configuration on November 5, 2026. The summaries reflect a Rider–Waite–Smith-oriented editorial tradition. The reflection layouts were prepared with AI assistance. No independent expert review is claimed. Automated checks cover 78 unique cards, the 22/56 arcana split, four 14-card suits, required fields, and consistency across formats. These checks do not establish interpretive accuracy. No artwork, private user questions or reading histories are included.

## Reuse and limitations
Data and documentation: CC BY 4.0. Credit [TarotAI](https://tarotai.art/), identify this dataset and indicate modifications. Intended for education, creativity and reflection; not evidence of predictive accuracy or a substitute for professional advice.

## Source and examples
[GitHub source and runnable Python examples](https://github.com/andradesuyanne386-png/tarotai-open-data).
[Hugging Face mirror](https://huggingface.co/datasets/HenryZheng99/tarotai-open-tarot-kit).

## Explore the publisher
[TarotAI](https://tarotai.art/) offers AI tarot readings, custom card creation and journaling.
