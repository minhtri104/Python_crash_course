favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people_to_poll = ["jen", "alex", "edward", "brian", "sarah", "linda"]

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"Please take the poll, {person.title()}!")
