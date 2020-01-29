import os
import json
import shutil

feature = "RevetementVetuste"
feature = "TraceHumidite"
feature = "ChateauMoulureOrnement"
feature = "FissureFacade"
feature = "CablePendantEnSurface"
feature = "BatimentVide"
feature = "VoletVetutste"
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
# feature = "PresenceActiviteSuivantes"

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