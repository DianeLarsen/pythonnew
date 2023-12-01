import csv
import statistics

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
all_records = []
meninfo = {}
womeninfo = {}
totalmen = 0
totalwomen = 0
nummen = 0
numwomen = 0
with open('insurance.csv') as file_object:
    insurance_csv = csv.DictReader(file_object)
    
    for rows in insurance_csv:
        all_records.append(rows)
        if rows["sex"] == "male":
            totalmen += float(rows["charges"])
            nummen += 1
        else:
            totalwomen += float(rows["charges"])
            numwomen += 1
        
        age.append(rows["age"])
        sex.append(rows["sex"])
        bmi.append(rows["bmi"])
        children.append(rows["children"])
        smoker.append(rows["smoker"])
        region.append(rows["region"])
        charges.append(rows["charges"])
#average cost of men non/smokers
meninfo["avcharges"] = totalmen/nummen
meninfo["avcharges"] = totalmen/nummen
meninfo["nummen"] = nummen
womeninfo["avcharges"] = totalwomen/numwomen
womeninfo["avcharges"] = totalwomen/numwomen
womeninfo["numwomen"] = numwomen
print(meninfo)

print(womeninfo)

# average cost of women non.smokers        
file_object.close()
