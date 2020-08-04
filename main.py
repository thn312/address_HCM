import unicodecsv
import csv
import library
import re

# import csv file in to list of Address List
addrList = []
with open('diachi.csv', newline='', encoding='utf-8') as csvFile:
    csvList = csv.reader(csvFile, delimiter=',')
    
    for row in csvList:
        # print("{0}. {1}".format(str(count),''.join(row)))
            addrList.append(','.join(row))
       

# remove accent from string
addrLisccent = []

for item in addrList:
    item = library.remove_accent(item)
    addrLisccent.append([item])
    # print("{0}. {1}".format(str(count), addrLisccent[len(addrLisccent)-1][0]))
    

# Parsing
addrListAccent = []

for item in addrList:
    addrListAccent.append([item])
    

# print(addrListAccent)
# combine list

for i in range(0, len(addrLisccent)):

    # districtIndex = library.detect_district_index(addrLisccent[i][0].lower())
    # wardIndex = library.detect_ward_index(addrLisccent[i][0].lower())
    # streetIndex = library.detect_street_index(addrLisccent[i][0].lower())

    district = library.detect_district(addrLisccent[i][0])
    ward = library.detect_ward(addrLisccent[i][0])
    street = library.detect_street(addrLisccent[i][0])[0]
    streetccent = library.detect_street(addrLisccent[i][0])[1]
    num = library.detect_num(addrListAccent[i][0], addrLisccent[i][0].lower(), streetccent.lower())

    if district != "":
        addrListAccent[i].append(district)
    else:
        addrListAccent[i].append("")
    
    if ward != "":
        addrListAccent[i].append(ward)
    else:
        addrListAccent[i].append("")

    if street != "":
        addrListAccent[i].append(street)
    else:
        addrListAccent[i].append("")

    addrListAccent[i].append(num)

# for i in range(0, len(addrListAccent)):
#     print("{0: <20}{1: <20}{2: <20}{3: <20}{4}".format(str(addrListAccent[i][4]), str(addrListAccent[i][3]), str(addrListAccent[i][2]), str(addrListAccent[i][1]), str(addrListAccent[i][0]) ))

# export to aggregated list CSV
# with open('test_out.csv', 'wb', encoding='utf-8', newline='') as csvFile:
with open('test_out.csv', 'wb') as csvFile:
    wr = unicodecsv.writer(csvFile, quoting=csv.QUOTE_ALL)
    for i in range(0, len(addrListAccent)):
        # print(addrLisccent[i])
        # wr.writerow("\"" + addrListAccent[i][0] + "\",\"" + addrListAccent[i][1] + "\",\"" + addrListAccent[i][2] + "\"")
        wr.writerow((str(addrListAccent[i][4]),str(addrListAccent[i][3]), str(addrListAccent[i][2]), str(addrListAccent[i][1]), str("Hồ Chí Minh")))

print("oke")
