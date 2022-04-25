import re
import string



def displaySingleItemCount(name):
    items = countItems()
    if name not in items:
        return 0
    else: 
        return items[name]

def countItems():
    items = {}
    with open ("groceries.txt") as groceries:
        for item in groceries:
            name = item.strip()
            if name not in items:
                items[name] = 1
            else:
                items[name] += 1

    return items

def generateFrequencies():
    items = countItems()
    with open("frequency.dat", "w") as data:
        for item in items:
            data.write(f"{item} {items[item]}\n")

def displayItemCounts():
    items = countItems()
    for item, count in items.items():
        print(f"{item}: {count}")

    return
