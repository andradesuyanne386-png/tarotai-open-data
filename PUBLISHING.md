# Mirror publishing

GitHub is the canonical source. Publish the same version on both mirrors.

## Hugging Face
Create a public dataset repository in your account. Upload `data/cards.jsonl` at its root and `huggingface/README.md` as the root README.md. Upload `data/spreads.json` under `extras/`. Confirm the viewer has 78 records and the source links work. Update the root README with the actual dataset URL after publishing.

## Kaggle
Create a public dataset with cards.json, cards.csv and spreads.json from data/. Copy the root README description and select CC BY 4.0. The metadata template requires your actual account handle. Create a Notebook from validation-and-lookup.ipynb and attach the published dataset. Run all cells before publishing. Add the actual dataset and Notebook URLs to the root README.

## Website
The accompanying application patch adds /open-data and downloadable copies. Deploy through the existing TarotAI website deployment workflow. Do not advertise the page as live before deployment succeeds.

## Website links

Use https://tarotai.art/ for all publisher and product links, including platform website fields, introductions, examples and attribution. Do not substitute inner-page URLs.
