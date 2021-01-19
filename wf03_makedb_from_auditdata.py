import csv
import json

feature = "RevetementVetuste"
feature = "TraceHumidite"
feature = "ChateauMoulureOrnement"
feature = "FissureFacade"
feature = "CablePendantEnSurface"
feature = "BatimentVide"
feature = "VoletVetuste"
feature = "PanneauAVendre"
feature = "BardageBoisAcierFacade"
feature = "JardinExterieurNonEntretenu"
feature = "MauvaisEtatToiture"
feature = "MultipleGraffitis"
feature = "BatimentMitoyenVetuste"
feature = "BatimentInnocupe"
feature = "CommerceEnRdcVideFerme"
feature = "MauvaisEtatGoutiere"
feature = "PorteFenetreMurees"
feature = "PresenceActiviteSuivantes"

print(f"Loading data/db.json")
with open(f"data/db.json") as f:
    s = f.read()
    db = json.loads(s)

print(f"Loading data/AuditData.csv")
with open("res/AuditData.csv") as f:
    rows = list(csv.DictReader(f, delimiter=";"))

rows = [row for row in rows if row[feature] == "O" or row[feature] == "N"]
positives = [row for row in rows if row[feature] == "O"]
print(f"{feature}: {len(rows)} items with {len(positives)} positives without duplicate photo, class_weight={len(rows) / len(positives):0.1f}")

db_auditdata = {}
for row in rows:
    db_auditdata[int(row["Id"])] = row

db["path"] += f"/{feature}"
db["class_weight"] = len(rows) / len(positives)
db["feature"] = feature
db["count"] = 0

l = list(db["items"])
db["items"] = []
positives = 0
for item in l:
    if int(item["dataId"]) in db_auditdata:
        db["count"] += 1
        item["adresseId"] = int(db_auditdata[int(item["dataId"])]["AdresseId"])
        item["isLoc"] = db_auditdata[int(item["dataId"])]["AddresseLocalisable"] == "O"
        item["cat"] = 1 if db_auditdata[int(item["dataId"])][feature] == "O" else 0
        if item["cat"] == 1:
            positives += 1
        db["items"].append(item)

db["positives"] = positives
db["class_weight"] = db["count"] / positives

print(f"Create db_{feature}.json with {db['count']} items")
with open(f"{db['path']}/db_{feature}.json", "w") as f:
    f.write(json.dumps(db, indent=4))


