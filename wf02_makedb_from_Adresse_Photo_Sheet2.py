import csv
import json

print("Loading res/Adresse_Photo_Sheet2.csv")
with open("res/Adresse_Photo_Sheet2.csv") as f:
    db_sheet2 = list(csv.DictReader(f, delimiter=";"))

db = {
    "feature":None,
    "path":"data",
    "count":len(db_sheet2),
    "positives":0,
    "class_weight":0,
    "lum": {
        "avg":0,
        "min":0,
        "max":0,
        "std":0
    },
    "contrast": {
        "avg":0,
        "min":0,
        "max":0,
        "std":0
    },
    "items": []
}

for i in db_sheet2:
    item = {
        "id": int(i["Id"]),
        "dataId": int(i["DataId"]),
        "name": i["GeneratedName"],
        "isGen": i["GeneratedPhoto"] == "O",
    }
    db["items"].append(item)

print(f"Create db.json with {db['count']} items")
with open(f"{db['path']}/db.json", "w") as f:
    f.write(json.dumps(db, indent=4))


