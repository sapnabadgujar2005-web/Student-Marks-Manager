Student={}

while True:
    print("\n----------------STUDENT MANAGER APP----------------------")
    print("1.Add Student")
    print("2.View Student")
    print("3.Check Result")
    print("4.Exit")

    choice=input("Enter Your Choice")
    if choice=="1":
        name=input("Enter Student Name :-")
        marks = int(input("Enter The Marks"))
        Student[name]=marks
        print(f"{name}Sucessfully Added")

    #view Student

    elif choice=="2":
        if not Student:
            print("Not Student Found!")
        else:
            for name,marks in Student.items():
                print(name,":",marks)
    

    elif choice=="3":
        name=input("Enter Student Name ")

        if(name in Student):
            marks =Student[name]

            if marks>=35:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student Not Found")


    elif choice=="4":
        print("Existing...")
        break

    else:
        print("Invalid Input")
