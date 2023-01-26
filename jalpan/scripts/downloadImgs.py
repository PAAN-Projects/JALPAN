import urllib.request
import json
import os

dirname = os.path.dirname(os.path.realpath(__file__))

files = [
    "menus/burgers.json",
    "menus/desserts.json",
    "menus/drinks.json",
    "menus/ice-cream.json",
    "menus/pizzas.json",
    "menus/sandwiches.json"
]

for FilePath in files:
    FilePath = os.path.join(dirname, FilePath)
    with open(FilePath) as file:
        fileInit = json.load(file)
    for food in fileInit:
        imageUrl = food["img"]
        name = food["name"].replace(" ", "")
        name = name.replace("'", '')
        print("Downloading => ", name, " : ", imageUrl)
        downloadPath = os.path.join(dirname, f"images/{name}.png")
        urllib.request.urlretrieve(imageUrl, downloadPath)
        print("Downloaded => ", imageUrl, end='\n\n\n\n\n')
    with open(FilePath, "w") as file:
        file.write(json.dumps(fileInit, indent=4))
