import matplotlib.pyplot as plt
x = "Maths", "Science", "S.St.", "Hindi", "Sanskrit", "Computer"
y = [12, 24, 10, 8, 4, 42]
explodee = (0, 0, 0, 0, 0, 0)
plt.pie(y, explode=explodee, labels=x,
        autopct="%1.2f%%")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.title("Marks Graph")
plt.axis("equal")
# plt.ylable("Marks")
plt.show()

# print(dir(plt))
