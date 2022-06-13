q = ["","What is HTML: "]
a = ["hypertextmarkuplanguage"]

for x in range(0,len(q)):
    user = input(q[x]).replace(" ", "").lower()
    print("Correct!" if user == a[x] else "Wrong!")