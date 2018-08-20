import csv

file_list = []
with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_list.append(row)

file_list[0].append("is_duplicate_phone")
phone_num_dict={}

for i in range(1, 10493):
    curr_ph = file_list[i][28]
    print(curr_ph)
    if(curr_ph in phone_num_dict.keys()):
        file_list[i].append("yes")
    else:
        file_list[i].append("no")
        phone_num_dict[curr_ph] = 1
    print(file_list[i][31])

with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(file_list)

