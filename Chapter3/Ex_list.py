
#Ex-3.4
name_invite = ['Tri', 'Anh', 'Vinh']
print("Hello " + name_invite[0] + " would you like to join me for dinner?")
print("Hello " + name_invite[1] + " would you like to join me for dinner?")
print("Hello " + name_invite[2] + " would you like to join me for dinner?")

#Ex-3.5
print("\nTri can't make it to dinner")
name_invite[1] = 'Khue'
print("\nHello " + name_invite[0] + " would you like to join me for dinner?")
print("Hello " + name_invite[1] + " would you like to join me for dinner?")
print("Hello " + name_invite[2] + " would you like to join me for dinner?")

#Ex-3.6
print("\nI found a bigger dinner table!")
name_invite.insert(0, 'Anna')
name_invite.insert(1, 'Hai')
name_invite.append('Phong')
print("\nHello " + name_invite[0] + " would you like to join me for dinner?")
print("Hello " + name_invite[1] + " would you like to join me for dinner?")
print("Hello " + name_invite[2] + " would you like to join me for dinner?")
print("Hello " + name_invite[3] + " would you like to join me for dinner?")
print("Hello " + name_invite[4] + " would you like to join me for dinner?")

print(name_invite)

#3-7
guests = ['Emma', 'Alice', 'Frank', 'David', 'Charlie', 'Grace']

print("I can invite only two people for dinner.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you to dinner.")

print(guests[0] + ", you are still invited to dinner!")
print(guests[1] + ", you are still invited to dinner!")

del guests[1]
del guests[0]

print(guests)


