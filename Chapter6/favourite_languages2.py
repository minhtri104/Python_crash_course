favourite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

friends = ["phil", "sarah"]

for name in favourite_language.keys():
    print(name.title())
    if name in friends:
        print(
            "Hi "
            + name.title()
            + ", I see your favourite language is "
            + favourite_language[name].title()
            + "!"
        )
