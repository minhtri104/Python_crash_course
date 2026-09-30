mimi = {"kind": "mèo", "owner": "An"}
gâu = {"kind": "chó", "owner": "Bình"}
kiki = {"kind": "vẹt", "owner": "Chi"}

pets = [mimi, gâu, kiki]

for pet in pets:
    print("Loài: " + pet["kind"].title())
    print("Chủ sở hữu: " + pet["owner"].title() + "")
