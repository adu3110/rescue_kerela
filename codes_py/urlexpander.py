import httplib
import urlparse
import csv

def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status / 100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url


def getlatlon(short_url):
    if("cid=" not in short_url):
        if(short_url.startswith("https")):
            if (("google" in short_url) or (".gl/" in short_url)):
                if (("?q=9" in short_url) or ("?q=10" in short_url)):
                    url_split_up = short_url.split('&')
                    url_split_up = url_split_up[0]
                    url_split = url_split_up.split('=')
                    loc_part = url_split[1]
                    if("," in loc_part):
                        loc_split = loc_part.split(',')
                    elif("%2C" in loc_part):
                        loc_split = loc_part.split('%2C')
                    else:
                        return("")

                else:
                    url_long = unshorten_url(short_url)
                    if('@' in url_long):
                        url_split = url_long.split('@')
                        loc_part = url_split[1]
                        loc_split = loc_part.split(',')
                    elif(("?q=9" in url_long) or ("?q=10" in url_long)):
                        url_split_up = url_long.split('&')
                        url_split_up = url_split_up[0]
                        url_split = url_split_up.split('=')
                        loc_part = url_split[1]
                        if ("," in loc_part):
                            loc_split = loc_part.split(',')
                        elif ("%2C" in loc_part):
                            loc_split = loc_part.split('%2C')
                        else:
                            return ("")
                    else:
                        return ("")
                return (','.join([loc_split[0], loc_split[1]]))
            else:
                return("")
        else:
            return("")
    else:
        return("")



import csv

file_list = []
with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_list.append(row)

for i in range(10493,17795):
    curr_url = file_list[i][5]
    # print(curr_url)
    # print(i)
    curr_latlon = getlatlon(curr_url)
    file_list[i][8] = curr_latlon
    print(file_list[i][8])

with open('/Users/apple/Downloads/merged_sheet_Sheet1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(file_list)


print(file_list[0])