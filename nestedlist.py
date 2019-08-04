def sortsecond(l):
	return l[1]
def sortfirst(l):
	return l[0]
student = []
n = int(input("Enter No of student: "))
for i in range(n):
    name = input("Enter name of Student{}: ".format(i))
    per = float(input("Enter Per of student{}: ".format(i)))
    student.append([name,per])
student = sorted(student,key = sortsecond)
min = student[0]
for i in student:
	if min[1] != i[1]:
		act = i
		break
ans = []
for i in student:
	if act[1] == i[1]:
		ans.append(i)
ans = sorted(ans,key = sortfirst)
for i in ans:
	print(i[0])
