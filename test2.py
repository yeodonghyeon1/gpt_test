location = {"임지선": (300, 400), "김진호": (1,2)}
# print(location.get("임지선"))
print(location.keys())
for i in location.keys():
    if i in member:
        location[i]
        print("move x: ", location.get(i)[0], "move y: ", location.get(i)[1])