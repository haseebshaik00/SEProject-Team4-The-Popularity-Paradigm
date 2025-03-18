# SEProject-Team4-The-Popularity-Paradigm

Research on How Software Development Metrics Influence Project Fame

---

## Useful Links:

- [Adopted RQ#1 and RQ#2 dataset](https://zenodo.org/records/14499305) 🔗
- [Adopted RQ#3 dataset](https://incubator.apache.org/clutch/) 🔗
- [RQ#1 and RQ#2 Dataset](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/datasets/final-dataset.csv) 🔗
- [RQ#3 Dataset](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/datasets/final-rq3-dataset.csv) 🔗
- [Preprocessing (RQ#1 and RQ#2)](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/preprocessing.ipynb) 🔗
- [Preprocessing (RQ#3)](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/%23RQ3_preprocessing.ipynb) 🔗
- [RQ#1 Analysis](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/%23RQ1.ipynb) 🔗
- [RQ#2 Analysis](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/%23RQ2.ipynb) 🔗
- [RQ#3 Analysis](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/%23RQ3_analysis.ipynb) 🔗
- [Case Study](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/case_study.ipynb) 🔗

---

**The final report can be found here: [Final_Report.pdf](https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm/blob/main/final_report.pdf)!**

---

> Requirements [Project Setup]

Install all the required libraries from requirements.txt

```shell
pip install -r requirements.txt
```
---
### Steps to Run the Project

1. Clone the repository
```shell
git clone https://github.com/haseebshaik00/SEProject-Team4-The-Popularity-Paradigm.git
```
2. Navigate to the project repository
```shell
cd SEProject-Team4-The-Popularity-Paradigm
```
3. Install required dependencies
```shell
pip install -r requirements.txt
```
4. Run the Analysis
```shell
python3 preprocessing.ipynb
python3 #RQ3_preprocessing.ipynb
python3 #RQ1.ipynb
python3 #RQ2.ipynb
python3 #RQ3.ipynb
python3 case_study.ipynb
```
5. Analyse the results!
---
> Pre-processing for [RQ#1 and RQ#2] - `preprocessing.ipynb`

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

- Merged both datasets, calculated **popularity score**, normalized it, found popularity, and stored the final dataset in `final-popularity-dataset.csv`.
- Then this dataset was merged with the ASFI dataset and the final data taken into consideration was stored in `final-dataset.csv`.

---

> 📘 **Disclaimer:**  
This research and its findings are intended solely for academic and study purposes. The content is shared publicly to promote open knowledge and may be reused, referenced, or extended by others with appropriate credit. Contributions, feedback, and collaborations are welcome!

