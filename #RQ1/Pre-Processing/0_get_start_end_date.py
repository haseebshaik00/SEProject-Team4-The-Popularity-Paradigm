import json
import pandas as pd
from tqdm import tqdm
# get listid, start_date, end_date from csv
lines = pd.read_csv('../raw_data/lists_2019_8.csv', usecols = [0,4,5]).values.tolist()

start_date_dict = {}
end_date_dict = {}

for line in tqdm(lines):
	listid, start_date, end_date = line
	start_date_dict[listid] = start_date
	end_date_dict[listid] = end_date

with open('../start_date_dict.json', 'w') as f:
	json.dump(start_date_dict, f, indent=4)

with open('../end_date_dict.json', 'w') as f:
	json.dump(end_date_dict, f, indent=4)

