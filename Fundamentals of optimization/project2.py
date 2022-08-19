a = open("Fb.txt")
for i in range(50):
    b = a.readline()
    c = "https://www.facebook.com/profile.php?id="+b
    print(c)