import csv, random

table_list = [i for i in range(1,95)]
expo_list = ["1"]

#get submissions from csv
title_col = "Submission Title"
description_col = "Plain Description"
sponsors_row = "Opt-in prize"
link_col = "Submission Url"

input_path = 'data/devpost.csv'
output_full_path = 'data/data.csv'
output_gavel_path = 'data/data_gavel.csv'


full  = []

with open(input_path) as csvfile:
    submissions_reader = list(csv.DictReader(csvfile))
    table_list = [i for i in range(1,len(submissions_reader)+1)]
    free_tables = table_list[:]
    print(table_list)
    for row in submissions_reader:
        print(row[title_col])
        table = free_tables[0] #(0, len(free_tables)-1)
        full.append(row)
        # complete_list[-1]["expo"] = expo_list[expo]
        full[-1]['table'] = table
        free_tables.remove(table)

# write full file (for expo website)

with open(output_full_path, 'w') as csvfile:
    fieldnames = ['table', 'project', 'sponsors', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in full:
        writer.writerow(
        {
            'table': row['table'],
            'project': row[title_col],
            'sponsors': row[sponsors_row],
            'link': row[link_col]
            #'category': ',
        })

