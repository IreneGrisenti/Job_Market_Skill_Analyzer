# Swedish Data Job Market Analyzer

An analysis of the Swedish job market for data roles, using open data from Arbetsförmedlingen's JobSearch API to identify the most in-demand skills across data science, analytics, engineering and AI positions.

## What this project does

Collects active job listings from Platsbanken, cleans the raw text descriptions and applies TF-IDF to extract and rank the skills employers ask for most.

## Data source

Data is collected via the [JobSearch API](https://jobsearch.api.jobtechdev.se) provided by Arbetsförmedlingen (the Swedish Public Employment Service). The API is open, free to use and requires no authentication.

Search terms include both English and Swedish equivalents across roles such as data scientist, data analyst, data engineer, machine learning engineer and business intelligence analyst.

## Limitations

- **Snapshot in time** - the API only returns currently active listings. Results reflect the market at the time of collection (24/03/2026) and will differ if rerun.
- **Mixed languages** - Swedish and English appear in the same dataset, which adds noise to the text analysis.
- **Unstructured skills** - most listings do not use the API's structured skills fields, so skill extraction relies on free text analysis.

## Potential next steps

- Use the [Historical Job Ads API](https://data.arbetsformedlingen.se) to analyse skill trends over time.
- Compare skill demand across Swedish regions (Stockholm, Malmö, Göteborg).