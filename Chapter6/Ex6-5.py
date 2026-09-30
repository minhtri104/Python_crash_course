rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mekong": "vietnam",
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\n---Rivers---")
for river in rivers.keys():
    print(river.title())

print("\n---Countries---")
for country in rivers.values():
    print(country.title())
