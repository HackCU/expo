import csv, random

table_list = [i for i in range(1,95)]
expo_list = ["1"]

#get submissions from csv
title_col = "Submission Title"
description_col = "Plain Description"
sponsors_row = "Desired Prizes"
link_col = "Submission Url"
room_col = "What Room Are You In?"
table_col = "What's Your Table Number?"

input_path = 'data/devpost.csv'
output_full_path = 'data/data.csv'
output_gavel_path = 'data/data_gavel.csv'


full  = []

with open(input_path) as csvfile:
    submissions_reader = list(csv.DictReader(csvfile))
    for row in submissions_reader:
        print(row[title_col])
        full.append(row)
        

# write full file (for expo website)

with open(output_full_path, 'w') as csvfile:
    fieldnames = ['room','table', 'project', 'sponsors', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in full:
        writer.writerow(
        {
            'room': row[room_col],
            'table': row[table_col],
            'project': row[title_col],
            'sponsors': row[sponsors_row],
            'link': row[link_col]
        })

