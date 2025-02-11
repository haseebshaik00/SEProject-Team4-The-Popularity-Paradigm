import os
import json
import pandas as pd 
from tqdm import tqdm 

commit_path = '../commits_raw/'
email_path = '../emails_raw/'

c_projects = set(os.listdir(commit_path))
e_projects = set(os.listdir(email_path))

# projects having both commit and email data
projects = c_projects.intersection(e_projects)

to_email_path = '../processed_data/emails/'
if not os.path.exists(to_email_path):
	os.makedirs(to_email_path)

to_commit_path = '../processed_data/commits/'
if not os.path.exists(to_commit_path):
	os.makedirs(to_commit_path)

# '0 list', '1 messageid', '2 senderaliasid', '3 senderalias',
# '4 referenceid', '5 recipaliasid', '6 recipalias', '7 datetime', 
# '8 subject', '9 body', '10 from_commit'

for p in tqdm(projects):
    # processing emails
	df = pd.read_csv(email_path + p, usecols=[3,4,6,7,9])
	df.columns = ['message_id', 'sender_id', 'reference_id', 'recipalias_id', 'date']
	df.to_csv(to_email_path + p, sep=",", index=False)

	# processing commits
	df = pd.read_csv(commit_path + p, usecols=[2,3,4,5,6,7,8])
	df.columns = ['message_id','committer_id','commit_datetime','file_operation','file_name','additions','deletions']
	df.to_csv(to_commit_path + p, sep=",", index=False)

