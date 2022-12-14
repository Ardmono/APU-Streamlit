#!/usr/bin/env python3
# vim: set ts=8 sts=4 et sw=4 tw=99:
#
# Calculates points columns for the provided CSV.
# Overwrites the input file in-place.
#
import pandas as pd
import sys
from coefficient import glossbrenner, wilks, mcculloch, ipf




csv = 'filename.csv'
csv = pd.read_csv(csv)
print(csv)
# Ensure points columns exist.
if 'Wilks' not in csv.columns:
    csv.append_column('Wilks')
if 'McCulloch' not in csv.fieldnames:
    csv.append_column('McCulloch')
if 'Glossbrenner' not in csv.fieldnames:
    csv.append_column('Glossbrenner')
if 'IPFPoints' not in csv.fieldnames:
    csv.append_column('IPFPoints')

# indexSex = csv.index('Sex')
# indexEquipment = csv.index('Equipment')
# indexEvent = csv.index('Event')
# indexAge = csv.index('Age')
# indexBodyweight = csv.index('BodyweightKg')
# indexTotal = csv.index('TotalKg')
# indexWilks = csv.index('Wilks')
# indexMcCulloch = csv.index('McCulloch')
# indexGlossbrenner = csv.index('Glossbrenner')
# indexIPFPoints = csv.index('IPFPoints')

# for row in csv.rows:
#     sex = row[indexSex]
#     bodyweight = row[indexBodyweight]
#     total = row[indexTotal]

#     if sex not in ['M', 'F']:
#         continue

#     if not bodyweight:
#         continue
#     bodyweight = float(bodyweight)

#     if not total:
#         continue
#     total = float(total)

#     # Add the Wilks score to the row.
#     score = wilks(sex == 'M', bodyweight, total)
#     row[indexWilks] = to_string(score)

#     # Calculate the age-adusted score.
#     age = row[indexAge].replace('.5', '')  # Round down when unknown.
#     if is_int(age):
#         row[indexMcCulloch] = to_string(
#             mcculloch(sex == 'M', int(age), bodyweight, total))
#     else:
#         # Better than just leaving it blank, when we have some data.
#         row[indexMcCulloch] = row[indexWilks]

#     # Add the Glossbrenner score to the row.
#     gloss = glossbrenner(sex == 'M', bodyweight, total)
#     row[indexGlossbrenner] = to_string(gloss)

#     # Add the IPF Points to the row.
#     ipfpoints = ipf(sex, row[indexEquipment], row[indexEvent], bodyweight, total)
#     row[indexIPFPoints] = to_string(ipfpoints)

# csv.write_filename(filename)
    


# if __name__ == '__main__':
#     main("filename.csv")