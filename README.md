# SEProject-Team4-The-Popularity-Paradigm

Research on How Software Development Metrics Influence Project Fame

> Requirements

Install all the required libraries

```shell
pip install -r requirements.txt
```

> Pre-process the data - `preprocessing.ipynb`

- Scraped repository data:
  - Graduated and retired repositories:
    - Successfully scraped: `repo_data.json` (193 repositories)
    - Failed to scrape: `failed_repos.json` (100 repositories)
  - Incubating repositories:
    - Successfully scraped: `repo_data_incubating.json` (16 repositories)
    - Failed to scrape: `failed_repos_incubating.json` (21 repositories)

- Handled failed data:
  - Retried failed scrapes for incubating repositories, remaining failed: `0`
  - Retried failed scrapes for graduated and retired repositories, remaining failed: `0`

- `repo_data.json` contains:
  - Successfully scraped graduated and retired repositories
  - Previously failed but now successfully scraped repositories
  - Successfully scraped incubating repositories

- `repo_data_incubating.json` contains successfully scraped incubating repositories

- Merged both datasets, calculated **popularity score**, normalized it, found popularity and stored the final dataset in `final-dataset.csv`
