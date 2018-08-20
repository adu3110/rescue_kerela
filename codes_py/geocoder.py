
import csv
import requests

file_list = []
with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_list.append(row)

file_list[0].append("latlng_from_location")
for i in range(1,10493):
    file_list[i].append("")
    print(file_list[i][len(file_list[i]) - 1])

for i in range(10493,17795):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': file_list[i][9]}
    try:
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']

        file_list[i].append(",".join([str(location['lat']), str(location['lng'])]))
        print(file_list[i][len(file_list[i]) - 1])
        pass
    except:
        file_list[i].append("")
        print(file_list[i][len(file_list[i]) - 1])
        continue




with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(file_list)



print()