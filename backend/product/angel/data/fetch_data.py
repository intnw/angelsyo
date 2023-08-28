import csv

mapping =  {
  "first_name": 1,
  "last_name": 2,
  "college_university": "",
  "bio": 3,
  "location_city": "",
  "location_country": 4,
  "typical_investment_size": "",
  "number_of_investments": "",
  "interested_category": "",
  "email": 6,
  "linkedin": 5,
  "twitter": 7,
}

#gritt.io
filename = "C:\\Users\\mvrkm\\OneDrive\\Documents\\general_react_tailwind\\angelsandvcs\\backend\product\\angel\\data\\Gritt_Export (20).csv"

def clean(text):
    return text.replace('"', "").strip()

def dep_get_rows_from_csv(fl):
    text = open(fl, "r", encoding="utf8").read()
    records = text.split("\n")

    rows = []
    for rc in records[1:]:
        if(not rc.strip()): continue

        fields = rc.split("\t")
       
        rows.append([clean(fl) for fl in fields])
    return rows

def get_rows_from_csv(fl):
    rows = csv.reader(open(filename, "r", encoding="utf8").read().split('\n'), delimiter=',')

    records = []
    for row in rows:
        records.append(row)
    return records[1:]

rows = get_rows_from_csv(filename)

def get_records():
    records = []
    for row in rows:
        angel_info = []
        for k in mapping:
            try:
                angel_info_row = {"key": k, "value": row[mapping[k]]}
                angel_info.append(angel_info_row)
            except:
                angel_info_row = {"key": k, "value": ""}
                angel_info.append(angel_info_row)
        records.append(angel_info)
    return records

# print(get_records()[-1])

def get_records_generator():
    for row in rows:
        angel_info = []
        for k in mapping:
            if mapping[k]:
                angel_info_row = {"key": k, "value": row[mapping[k]]}
                angel_info.append(angel_info_row)
            else:
                angel_info_row = {"key": k, "value": ""}
                angel_info.append(angel_info_row)
        yield angel_info