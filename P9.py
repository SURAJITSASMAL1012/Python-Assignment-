
#list to store all user details
user=[]

#list for student names
name_list=[]

#list for subject list
sub_list=[]

#list for marks for corresponsing subjects
mark_list=[]

flag=True

#loop to repetatively enter student details
while(flag):
	print("\n 1.Enter Name\n 2.Exit")
	ch=int(input("\nEnter your choice:"))
	if(ch==1):
		name=input("Enter Student Name:")

#store names uniquely
		if name not in name_list:
			name_list.append(name)

		temp=True

#temporary subjects list
		sub=[]

#temporary marks list
		m=[]

#loop to iteratively enter subject name and it's marks
		while(temp):
			print("\n 1.Enter Subject Name\n 2.Exit")
			ch1=int(input("\nEnter your choice:"))
			if(ch1==1):
				s=input("Enter Subject Name:")

#only unique subjects
				if(s not in sub_list):
					sub_list.append(s)
				marks=int(input("Enter Marks:"))
				m.append(marks)
				sub1=[s,marks]
				sub.append(sub1)
			elif(ch1==2):
				temp=False
			else:
				print("\nWrong Choice")
		mark_list.append(m)
		stu=[name,sub]
		user.append(stu)
	elif(ch==2):
		flag=False
	else:
		print("\nWrong Choice")
print("User Details:",user)
print("User Names:",name_list)
print("Subject Details:",sub_list)
print("Marks Details:",mark_list)

#loop to find max scored subject for every student
for i in range(len(user)):
    record=user[i]
    index=mark_list[i].index(max(mark_list[i]))
    print("\nFor Student Name:"+str(record[0]))
    print("\nSubject Name:"+str(record[1][index][0]))
    print("\nMarks:"+str(record[1][index][1]))
