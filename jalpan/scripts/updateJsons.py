import json
import os
import random

dirname = os.path.dirname(os.path.realpath(__file__))


def isSpicyFalse():
    files = [
        "menus/desserts.json",
        "menus/drinks.json",
        "menus/ice-cream.json",
    ]
    for FilePath in files:
        FilePath = os.path.join(dirname, FilePath)
        with open(FilePath) as file:
            fileInit = json.load(file)
        for food in fileInit:
            food["isSpicy"] = False
        print(file, "emnd", end="\n\n\n")
        with open(FilePath, "w") as file:
            file.write(json.dumps(fileInit, indent=4))


def isSpicyTrue():
    files = [
        "menus/sandwiches.json"
    ]
    for FilePath in files:
        FilePath = os.path.join(dirname, FilePath)
        with open(FilePath) as file:
            fileInit = json.load(file)
        for food in fileInit:
            food["isSpicy"] = True
        print(file, "emnd", end="\n\n\n")
        with open(FilePath, "w") as file:
            file.write(json.dumps(fileInit, indent=4))


def isSpicyRandom():
    files = [
        "menus/burgers.json",
        "menus/pizzas.json"
    ]
    choices = [True, False, False, True, False]
    for FilePath in files:
        FilePath = os.path.join(dirname, FilePath)
        with open(FilePath) as file:
            fileInit = json.load(file)
        for food in fileInit:
            food["isSpicy"] = random.choice(choices)
        print(file, "emnd", end="\n\n\n")
        with open(FilePath, "w") as file:
            file.write(json.dumps(fileInit, indent=4))


def imageLocation():
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
            name = food["name"].replace(" ", "")
            name = name.replace("'", '')
            food["img"] = f"images/{name}.png"
        print(file, "emnd", end="\n\n\n")
        with open(FilePath, "w") as file:
            file.write(json.dumps(fileInit, indent=4))


imageLocation()
