import csv
from datetime import datetime, timedelta 
with open('_____.csv') as csvfile: 
	reader = csv.DictReader(csvfile)
	supporter = {}
	for row in reader:
		if datetime.strptime('2017-08-14', '%Y-%m-%d') - datetime.strptime(row['most recent recurring donation'], '%Y-%m-%d') > timedelta(days = 33):
			if row['recurring start date']:
				start = datetime.strptime(row['recurring start date'], '%Y-%m-%d')
			else:
				start = datetime.strptime(row['donation date'], '%Y-%m-%d')
			if row['most recent recurring donation']:
				end = datetime.strptime(row['most recent recurring donation'], '%Y-%m-%d')
			else:
				end = None
			if row['donation amount']:
				amount = float(row['donation amount'])
			if row['public_outreach_id']:
				outreach = row['public_outreach_id']
			else:
				outreach = None 

			if start is not None and end is not None: 
				length = end - start
				if supporter.get(row['supporter_id']) is not None: 
					if end > supporter[row['supporter_id']]['recurring_end_date']:
						supporter[row['supporter_id']]['recurring_end_date'] = end
						supporter[row['supporter_id']]['length_of_donor'] = end - supporter[row['supporter_id']]['recurring_start_date']
				
					if supporter[row['supporter_id']]['recurring_start_date'] > start:
						supporter[row['supporter_id']]['recurring_start_date'] = start
						supporter[row['supporter_id']]['length_of_donor'] = supporter[row['supporter_id']]['recurring_end_date'] - start
				
					if supporter[row['supporter_id']]['donation_amount']: 
						supporter[row['supporter_id']]['donation_amount'] = supporter[row['supporter_id']]['donation_amount'] + amount 

					if supporter[row['supporter_id']]['public_outreach_id'] == None and row['public_outreach_id']:
						supporter[row['supporter_id']]['is_renewal'] = True

				else:
					supporter[row['supporter_id']] = {'recurring_start_date': start,
	                                					'recurring_end_date': end,
	                               						'length_of_donor': length,
	                               						'donation_amount': amount,
	                               						'public_outreach_id': outreach,
	                               						'is_renewal': False}
		elif supporter.get(row['supporter_id']):
			del	supporter[row['supporter_id']] 

total_lengths_1 = 0
total_donation_1 = 0
total_lengths_2 = 0
total_donation_2 = 0
total_lengths_3 = 0
total_donation_3 = 0
i = 0
k = 0
j= 0
for x,y in supporter.iteritems():
	if y['public_outreach_id'] is None and y['is_renewal'] == False: 
		total_lengths_1 = total_lengths_1 + y['length_of_donor'].days
		total_donation_1 = total_donation_1 + y['donation_amount']
		try:
			average_monthly_donation = total_donation_1/(total_lengths_1/30)
		except ZeroDivisionError:
			pass
		i = i + 1

average_length_of_supporter = total_lengths_1/i

for x,y in supporter.iteritems():
	if y['public_outreach_id'] is None and y['is_renewal'] == True:
		total_lengths_2 = total_lengths_2 + y['length_of_donor'].days
		total_donation_2 = total_donation_2 + y['donation_amount']
		try:
			average_monthly_donation_2 = total_donation_2/(total_lengths_2/30)
		except ZeroDivisionError:
			pass 
		k = k + 1

average_length_of_supporter_2 = total_lengths_2/k

for x,y in supporter.iteritems():
	if y['public_outreach_id'] is not None:
		total_lengths_3 = total_lengths_3 + y['length_of_donor'].days
		total_donation_3 = total_donation_3 + y['donation_amount']
		try:
			average_monthly_donation_3 = total_donation_3/(total_lengths_3/30)
		except ZeroDivisionError:
			pass 
		j = j + 1

average_length_of_supporter_3 = total_lengths_3/j

print i,k,j
print "Average length of supporter -- Website =" ,round(average_length_of_supporter,0), "days ,", "Average length of supporter -- Phone renewal =" ,round (average_length_of_supporter_2,0), "days", "Average length of supporter -- Phone Only =" ,round (average_length_of_supporter_3,0), "days"
print "Average Monthly Donation -- Website = $" ,round(average_monthly_donation, 2), ",","Average Monthly Donation -- Phone renewal = $" , round(average_monthly_donation_2,2), "Average Monthly Donation -- Phone Only = $" , round(average_monthly_donation_3, 2)
print "Lifetime Value of Donor -- Website = $" ,round(total_donation_1/i,2),  ",", "Lifetime Value of Donor -- Phone renewal = $" , round(total_donation_2/k,2), "Lifetime Value of Donor -- Phone Only = $" , round(total_donation_3/j,2)










   



    						 

		
