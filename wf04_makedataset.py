import os
import json
import shutil

feature = "RevetementVetuste"
path = "../images"

print(f"Loading data/{feature}/db_{feature}.json")
with open(f"data/{feature}/db_{feature}.json") as f:
    s = f.read()
    db = json.loads(s)

for item in db["items"]:
    file = f"{path}/{item['name']}"
    if os.path.isfile(file):
        shutil.copy(file, f"data/{feature}/{item['cat']}")
    else:
        print(f"Can't found {file}")