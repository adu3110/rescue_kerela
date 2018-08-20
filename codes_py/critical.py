import csv

file_list = []
with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_list.append(row)

for i in range(10493,len(file_list)):
    curr_line = []
    for j in range(0,31):
        curr_line.append(file_list[i][j])
    curr_line.append("")
    curr_line.append("")
    curr_line.append(file_list[i][31])
    file_list[i] = curr_line

file_list[0].append("is_critical")

for i in range(1,len(file_list)):
    curr_need = file_list[i][26]
    curr_detail = file_list[i][1]
    if(("baby" in curr_line) or
            ("babies" in curr_line) or
            ("dialysis" in curr_line) or
            ("injur" in curr_line) or
            ("injur" in curr_line) or
            ("diabet" in curr_line) or
            ("child" in curr_line) or
            ("pregnant" in curr_line) or
            ("old" in curr_line) or
            ("aged" in curr_line) or
            ("senior" in curr_line) or
            ("baby" in curr_detail) or
            ("babies" in curr_detail) or
            ("dialysis" in curr_detail) or
            ("injur" in curr_detail) or
            ("injur" in curr_detail) or
            ("diabet" in curr_detail) or
            ("child" in curr_detail) or
            ("pregnant" in curr_detail) or
            ("old" in curr_detail) or
            ("aged" in curr_detail) or
            ("senior" in curr_detail)):
        file_list[i].append("yes")
    else:
        file_list[i].append("no")

    print(file_list[i][34])


with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(file_list)

