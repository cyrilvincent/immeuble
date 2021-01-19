import csv

with open("res/AuditData.csv") as f:
    db = list(csv.DictReader(f, delimiter=";"))

videDb = [row for row in db if row["BatimentVide"] == "O" or row["BatimentVide"] == "N"]
positives = [row for row in videDb if row["BatimentVide"] == "O"]
print(f"BatimentVide: {len(videDb)} items with {len(positives)} positives")

aVendreDb = [row for row in db if row["PanneauAVendre"] == "O" or row["PanneauAVendre"] == "N"]
positives = [row for row in aVendreDb if row["PanneauAVendre"] == "O"]
print(f"PanneauAVendre: {len(aVendreDb)} items with {len(positives)} positives")

fissuresDb = [row for row in db if row["FissureFacade"] == "O" or row["FissureFacade"] == "N"]
positives = [row for row in fissuresDb if row["FissureFacade"] == "O"]
print(f"Fissures: {len(fissuresDb)} items with {len(positives)} positives")

voletDb = [row for row in db if row["VoletVetuste"] == "O" or row["VoletVetuste"] == "N"]
positives = [row for row in voletDb  if row["VoletVetuste"] == "O"]
print(f"VoletVetuste: {len(voletDb)} items with {len(positives)} positives")

humiditeDb = [row for row in db if row["TraceHumidite"] == "O" or row["TraceHumidite"] == "N"]
positives = [row for row in humiditeDb if row["TraceHumidite"] == "O"]
print(f"TraceHumidite: {len(humiditeDb)} items with {len(positives)} positives")

ornementDb = [row for row in db if row["ChateauMoulureOrnement"] == "O" or row["ChateauMoulureOrnement"] == "N"]
positives = [row for row in ornementDb if row["ChateauMoulureOrnement"] == "O"]
print(f"ChateauMoulureOrnement: {len(ornementDb)} items with {len(positives)} positives")

bardageDb = [row for row in db if row["BardageBoisAcierFacade"] == "O" or row["BardageBoisAcierFacade"] == "N"]
positives = [row for row in bardageDb if row["BardageBoisAcierFacade"] == "O"]
print(f"BardageBoisAcierFacade: {len(bardageDb)} items with {len(positives)} positives")

jardinDb = [row for row in db if row["JardinExterieurNonEntretenu"] == "O" or row["JardinExterieurNonEntretenu"] == "N"]
positives = [row for row in jardinDb if row["JardinExterieurNonEntretenu"] == "O"]
print(f"JardinExterieurNonEntretenu: {len(jardinDb)} items with {len(positives)} positives")

toitureDb = [row for row in db if row["MauvaisEtatToiture"] == "O" or row["MauvaisEtatToiture"] == "N"]
positives = [row for row in toitureDb if row["MauvaisEtatToiture"] == "O"]
print(f"MauvaisEtatToiture: {len(toitureDb)} items with {len(positives)} positives")

graffitiDb = [row for row in db if row["MultipleGraffitis"] == "O" or row["MultipleGraffitis"] == "N"]
positives = [row for row in graffitiDb if row["MultipleGraffitis"] == "O"]
print(f"MultipleGraffitis: {len(graffitiDb)} items with {len(positives)} positives")

cableDb = [row for row in db if row["CablePendantEnSurface"] == "O" or row["CablePendantEnSurface"] == "N"]
positives = [row for row in cableDb if row["CablePendantEnSurface"] == "O"]
print(f"CablePendantEnSurface: {len(cableDb)} items with {len(positives)} positives")

mitoyenDb = [row for row in db if row["BatimentMitoyenVetuste"] == "O" or row["BatimentMitoyenVetuste"] == "N"]
positives = [row for row in mitoyenDb if row["BatimentMitoyenVetuste"] == "O"]
print(f"BatimentMitoyenVetuste: {len(mitoyenDb)} items with {len(positives)} positives")

innocupeDb = [row for row in db if row["BatimentInnocupe"] == "O" or row["BatimentInnocupe"] == "N"]
positives = [row for row in innocupeDb if row["BatimentInnocupe"] == "O"]
print(f"BatimentInnocupe: {len(innocupeDb)} items with {len(positives)} positives")

commerceDb = [row for row in db if row["CommerceEnRdcVideFerme"] == "O" or row["CommerceEnRdcVideFerme"] == "N"]
positives = [row for row in commerceDb if row["CommerceEnRdcVideFerme"] == "O"]
print(f"CommerceEnRdcVideFerme: {len(commerceDb)} items with {len(positives)} positives")

activiteDb = [row for row in db if row["PresenceActiviteSuivantes"] == "O" or row["PresenceActiviteSuivantes"] == "N"]
positives = [row for row in activiteDb if row["PresenceActiviteSuivantes"] == "O"]
print(f"PresenceActiviteSuivantes: {len(activiteDb)} items with {len(positives)} positives")

vetusteDb = [row for row in db if row["RevetementVetuste"] == "O" or row["RevetementVetuste"] == "N"]
positives = [row for row in vetusteDb if row["RevetementVetuste"] == "O"]
print(f"RevetementVetuste: {len(vetusteDb)} items with {len(positives)} positives")

goutiereDb = [row for row in db if row["MauvaisEtatGoutiere"] == "O" or row["MauvaisEtatGoutiere"] == "N"]
positives = [row for row in goutiereDb if row["MauvaisEtatGoutiere"] == "O"]
print(f"MauvaisEtatGoutiere: {len(goutiereDb)} items with {len(positives)} positives")

mureDb = [row for row in db if row["PorteFenetreMurees"] == "O" or row["PorteFenetreMurees"] == "N"]
positives = [row for row in mureDb if row["PorteFenetreMurees"] == "O"]
print(f"PorteFenetreMurees: {len(mureDb)} items with {len(positives)} positives")