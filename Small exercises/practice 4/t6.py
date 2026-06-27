names = input("enter the username:").split()
best_name = ""
best_score = 0
for name in names:
    if name.startswith("@"):
        name = name[1:]
    if name.endswith("_bot"):
        name = name[:-4]
    name = name.lower()
    if not name.isalpha():
        continue
    score = name.count("a") * 2 + len(name)
    if name.find("admin") != -1:
        score -= 5
    if best_score is None or score > best_score or (score == best_score and name < best_name):
        best_score = score
        best_name = name
print(names)
print(name)
print(score)