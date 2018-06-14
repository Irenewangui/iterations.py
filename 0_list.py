students =["Irene","Judith","lauren"]
welcome_str="Welcome Ms {} to akirachix"
print(welcome_str.format(students[0]))
print(welcome_str.format(students[1]))
print(welcome_str.format(students[2]))
students.append("Yvonne")
students.append("Jane")
print(welcome_str.format(students[3]))
print(welcome_str.format(students[4]))