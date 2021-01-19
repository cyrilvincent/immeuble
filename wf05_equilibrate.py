import os
import random

feature = "RevetementVetuste"
feature = "TraceHumidite"
feature = "ChateauMoulureOrnement"
feature = "FissureFacade"
feature = "CablePendantEnSurface"
feature = "BatimentVide"
feature = "VoletVetuste"
feature = "PanneauAVendre"
# feature = "BardageBoisAcierFacade"
# feature = "JardinExterieurNonEntretenu"
# feature = "MauvaisEtatToiture"
# feature = "MultipleGraffitis"
# feature = "BatimentMitoyenVetuste"
# feature = "BatimentInnocupe"
# feature = "CommerceEnRdcVideFerme"
# feature = "MauvaisEtatGoutiere"
# feature = "PorteFenetreMurees"
# feature = "PresenceActiviteSuivantes"

files = os.listdir(f"data/{feature}/1")
print(f"Found {len(files)} files in data/{feature}/1")

nb = int(len(files) * 1.1)

files = os.listdir(f"data/{feature}/0")
print(f"Found {len(files)} files in data/{feature}/0")

print(f"Take {nb} files")
nb = len(files) - nb
print(f"Delete {nb} files")

random.shuffle(files)
for f in files[0:nb]:
    print(f"Delete data/{feature}/0/{f}")
    try:
        os.remove(f"data/{feature}/0/{f}")
    except Exception as ex:
        print(ex)
