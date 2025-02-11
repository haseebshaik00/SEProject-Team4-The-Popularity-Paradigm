import os
import json
from datetime import datetime
import math 
from tqdm import tqdm
import pandas as pd

email_path = '../processed_data/emails/'
commit_path = '../processed_data/commits/'

projects = os.listdir(email_path)

with open('../start_date_dict.json', 'r') as f:
	start_date_dict = json.load(f)

with open('../uid_to_name.json', 'r') as f:
	id_to_name = json.load(f)


to_email_path = '../monthly_data/emails/'
to_commit_path = '../monthly_data/commits/'

if not os.path.exists(to_email_path):
	os.makedirs(to_email_path)

if not os.path.exists(to_commit_path):
	os.makedirs(to_commit_path)

non_coding = ['.jar', '.xml', '.yml', '.json', '.png', '.md', '.yaml', '.cfg', '.jpg', '.ini', '.gif', '.txt', '.tex', '.pdf', '.gitignore', '.config', '.info', '.properties']

for project in tqdm(projects):
	# project id
	project_id = project.replace('.csv', '')
	start_date = start_date_dict[project_id]
	start_date = datetime.strptime(start_date, '%m/%d/%Y')

	# dividing emails
	if not os.path.exists(to_email_path + project_id):
		os.makedirs(to_email_path + project_id)

	lines = pd.read_csv(email_path + project).values.tolist()

	for line in lines[1:]:
		line = [str(l) for l in line]
		message_id,sender_id,reference_id,recipalias_id,date = line
		date = date[:-4]

		date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
		month = math.ceil((date - start_date).days / 30)

		# convert ids to names
		sender_id = id_to_name[str(sender_id)]
		recipalias_id = id_to_name[str(int(float(recipalias_id)))]

		things = [str(date), sender_id, recipalias_id]
		with open(to_email_path + project_id + os.sep + str(month) + '.csv', 'a') as f:
			f.write(','.join(things) + '\n')
		
	# dividing commits
	if not os.path.exists(to_commit_path + project_id):
		os.makedirs(to_commit_path + project_id)

	lines = pd.read_csv(commit_path + project).values.tolist()

	for line in lines[1:]:
		message_id, committer_id, commit_datetime, file_operation, file_name, additions, deletions = line
		commit_datetime = commit_datetime[:-3]
		this_time = datetime.strptime(commit_datetime, '%Y-%m-%d %H:%M:%S')
		month = math.ceil((this_time - start_date).days / 30)
		file_name = file_name.split('/')[-1]

		is_coding = True
		# check if it is a coding files (extensions)
		for non_c in non_coding:
			if non_c in file_name:
				is_coding = False
				break

		# continue on it does not have an extension, or it is not a coding file.
		if '.' not in file_name or not is_coding:
			continue

		committer_id = id_to_name[str(committer_id)]
		file_name = file_name.replace(',', '')
		things = [str(commit_datetime), committer_id, str(file_name)]
		# line = [str(l) for l in line]
		with open(to_commit_path + project_id + os.sep + str(month) + '.csv', 'a') as f:
			f.write(','.join(things)+ '\n')
