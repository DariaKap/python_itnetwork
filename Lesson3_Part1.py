string_to_process = "abcdefghijklmnopqrstuvwxyz"

while string_to_process:
    string_to_process = string_to_process[:-1]
    print(string_to_process)

# Выбрать "самого кого-то" персонажа перебрав всех циклом
infinite_group_dict = [
    {'Name': '김성규', 'BirthDate': 28, 'BirthMonth': 4,
     'BirthYear': 1989, 'Position': "leader, main vocalist"},
    {'Name': '장동우', 'BirthDate': 22, 'BirthMonth': 11,
     'BirthYear': 1990, 'Position': "main rapper"},
    {'Name': '남우현', 'BirthDate': 8, 'BirthMonth': 2,
     'BirthYear': 1991, 'Position': "main vocalist"},
    {'Name': '이성종', 'BirthDate': 3, 'BirthMonth': 9,
     'BirthYear': 1993, 'Position': "vocalist"},
    {'Name': '이성열', 'BirthDate': 27, 'BirthMonth': 8,
     'BirthYear': 1991, 'Position': "vocalist"},
    {'Name': '엘', 'BirthDate': 13, 'BirthMonth': 3,
     'BirthYear': 1992, 'Position': "vocalist"}
]
maknae = infinite_group_dict[0]
for member in infinite_group_dict:
    if member.get("BirthYear") > maknae.get("BirthYear"):
        maknae = member
    elif member.get("BirthYear") == maknae.get("BirthYear"):
        if member.get("BirthMonth") > maknae.get("BirthMonth"):
            maknae = member
        elif member.get("BirthMonth") == maknae.get("BirthMonth"):
            if member.get("BirthDate") >= maknae.get("BirthDate"):
                maknae = member
print(maknae.get("Name"), "is the youngest")
# Сделать запрос данный от пользователя
position = input("Are you looking for a member in what position? ")
seach_members = []
for member in infinite_group_dict:
    if member.get("Position").find(position) != -1:
        seach_members.append(member.get("Name"))
print(seach_members)


