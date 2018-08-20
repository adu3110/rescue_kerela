import csv

file_list = []
with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_list.append(row)

file_list[0][32] = "is_caller_outside_kerala"


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

print(file_list[0])

for i in range(1, 10493):
    curr_latlon = file_list[i][23]
    lat_lon = curr_latlon.split(",")
    print(lat_lon)
    print(is_number(lat_lon[0]))
    if(len(lat_lon)==2 and is_number(lat_lon[0]) and is_number(lat_lon[1])):
        lat = float(lat_lon[0])
        lon = float(lat_lon[1])
        print(lat, lon)
        if (lat > 8 and lat < 14 and lon > 74 and lon < 80):
            file_list[i][32] = "no"
        else:
            file_list[i][32] = "yes"
    else:
        file_list[i][32] = "not known"
    print(file_list[i][32])

with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(file_list)


print(file_list[10000])