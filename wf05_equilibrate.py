import os
import random

feature = "RevetementVetuste"

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
    os.remove(f"data/{feature}/0/{f}")
