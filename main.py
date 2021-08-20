n = int (input("人数の入力："))
data = {}
new_students = []
stu_points = []
for i in range(n):
    name = input(f"{i+1}. ")
    new_students.append(name)

print("Start counting!")
s = input()

for i in range(n):
    count = 0
    for j in range(len(s)):
        if int(s[j]) == i+1:
            count+=1
    stu_points.append(count)

data.update(zip(new_students,stu_points))

for key, value in data.items():
    print(f"{key}の得点は{value}点")