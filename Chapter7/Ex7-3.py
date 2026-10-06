prompt = "Tôi sẽ nói cho bạn số nào là bội của 10."
prompt += "\nVui lòng nhập một số: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("\nSố " + str(number) + " là bội của 10.")
else:
    print("\nSố " + str(number) + " không phải là bội của 10.")
