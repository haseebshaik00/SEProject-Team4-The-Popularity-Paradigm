# This file is used to process the broadcasts in APACHE incubator.
# The correspoendent are set to be the developers who ever replied to that bc email.

import os
from tqdm import tqdm

path = '../processed_data/emails/'
projects = os.listdir(path)

for p in tqdm(projects):
	to_emails = {}
	# load email data
	with open(path + p, 'r') as f:
		lines = f.readlines()
	# starting from the second line (ignore the index)
	for line in lines[1:]:
		try:
			message_id, sender_id, reference_id, recipalias_id, datetime = line.split(',')
		except: continue
		# if this email is replaying another email
		if reference_id:
			# we add the sender to its dict
			if reference_id not in to_emails:
				to_emails[reference_id] = set()
			to_emails[reference_id].add(sender_id)
	with open(path + p, 'w') as f:
		for line in lines:
			try:
				message_id, sender_id, reference_id, recipalias_id, datetime = line.split(',')
			except: continue
			# if this is a BC email
			if len(recipalias_id) == 0 and message_id not in to_emails:
				# print('Blank BC...')
				continue

			# if there is someone replying this email
			elif message_id in to_emails:
				for recipalias_id in to_emails[message_id]:
					things = [message_id, sender_id, reference_id, recipalias_id, datetime]
					f.write(','.join(things))
			else:
				f.write(line)



