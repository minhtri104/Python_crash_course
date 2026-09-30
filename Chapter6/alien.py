alien_0 = {"x_positon": 0, "y_position": 25, "speed": "speed"}
print(f"Original x-position: {alien_0['x_positon']}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_positon"] = alien_0["x_positon"] + x_increment
print(f"New x-position: {alien_0['x_positon']}")
