class dateType():
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y
    def getDay(self):
        return self.day
    def getDoB(self):
        return [self.day,self.month,self.year]
    def getDoJ(self):
        return [self.day, self.month, self.year]

class person():
    def __init__(self, DoB, n):
        self.DoB=DoB
        self.name=n

    def getName(self):
        return self.name

class visitor(person):
    def __init__(self,DoB,n):
        person.__init__(self,DoB,n)

class memberMU(person):  # inherits person
    def __init__(self, n, DoB, DoJoining):
        person.__init__(self, DoB, n)  # for super class
        self.DoJ = DoJoining

    def get_join_date(self):
        return self.DoJ


class studentMU(memberMU):
    def __init__(self, n, DoB, DoJoining, Major):
        memberMU.__init__(self, n, DoB, DoJoining)
        self.Major = Major

    def getMajor(self):
        return self.Major

class staff(memberMU):
    def __init__(self,n, DoB, DoJoining,department):
        memberMU.__init__(self, n, DoB, DoJoining)
        self.department = department

    def get_department(self):
        return self.department

def getFormattedDate(D):
    return str(D[0])+"/"+str(D[1])+"/"+str(D[2])

def input_validator(msg,category):
    while True:
        try:
            user_input = int(input(msg))

            if user_input < 0 or user_input == 0:
                print("Please Enter valid Number for " + category)
                continue
            else:
                break
        except ValueError:
            print("Please Enter Valid "+category)
            continue
    return user_input

def existance_checker(dict:dict,name):
    if name in dict:
        return True

def checkout(dict:dict,name):
    if existance_checker(dict, name):
        print(name + " removing from the database  ....")
        dict.pop(name)
    else:
        print(name + " not exist in the database....")

def display_students(list_student):
    for i in list_student.keys():
        print("Name:  " + list_student[i].name + "   DoB: " + getFormattedDate(
            list_student[i].DoB.getDoB()) + "   DoJ: " + getFormattedDate(list_student[i].get_join_date().getDoJ())
              + "  Major: " + list_student[i].getMajor())

def display_staff(list_staff):
    for i in list_staff.keys():
        print("Name:  " + list_staff[i].name + "   Department: ", list_staff[i].get_department(), "   DoB: ",
              getFormattedDate(list_staff[i].DoB.getDoB()),
              "  DoJ : " + getFormattedDate(list_staff[i].get_join_date().getDoJ()))

def display_visitors(list_visitor):
    for i in list_visitor.keys():
        print("Name:  ", list_visitor[i].name, "   DoB: ", getFormattedDate(list_visitor[i].DoB.getDoB()))

def gather_basic_info():
    n = input("Name:  ")
    d = input_validator("DoB Day: ", "Day")
    m = input_validator("DoB Month: ", "Month")
    y = input_validator("DoB Year: ", "Year")
    dob = dateType(d, m, y)
    d = input_validator("DoJ Day: ", "Day")
    m = input_validator("DoJ Month: ", "Month")
    y = input_validator("DoJ Year: ", "Year")
    doj = dateType(d, m, y)
    return n,dob,doj

ch = 1
list_student = {}
list_staff = {}
list_visitor={}

######################### Menu ####################################

while not ch==0:
    print("1-Check-in student")
    print("2-Check-in staff")
    print("3-Check-in visitor")
    print("4-Display student")
    print("5-Display staff")
    print("6-Display visitor")
    print("7-Check-out student")
    print("8-Check-out staff")
    print("9-Check-out visitor")
    print("0-Exit")

    while True:
        try:
            ch=int(input("Choice......"))

            if ch < 0:
                print("Please Enter positive Number as your Selection !!!!")
                continue
            elif ch == 0:
                break
            break
        except ValueError:
            print("Please Enter Valid Number Please")
            continue


################################ Student #############################

    if ch==1: # student in
        n,dob,doj=gather_basic_info()
        mjr=input("Major: ")
        tmpSt=studentMU(n,dob,doj,mjr)
        list_student[n]=tmpSt

    if ch == 4:  # display all students
        display_students(list_student)

############################## Staff ##################################
    if ch==2:
        n, dob, doj = gather_basic_info()
        department = input("Department : ")
        tmpStaff = staff(n,dob,doj,department)
        list_staff[n] = tmpStaff

    if ch == 5:  # display all staff
        display_staff(list_staff)

############################## visitor ##################################

    if ch==3:
        n = input("Name: ")
        d = input_validator("DoB Day: ", "Day")
        m = input_validator("DoB Month: ", "Month")
        y = input_validator("DoB Year: ", "Year")
        dob = dateType(d, m, y)
        tmpVisitor = visitor(dob,n)
        list_visitor[n] = tmpVisitor

    if ch == 6:  # display all visitors
        display_visitors(list_visitor)

############################## checkout student ##################################

    if ch == 7:
        name = input("Enter Name of the Student : ")
        checkout(list_student,name)
        display_students(list_student)


############################## checkout staff ##################################

    if ch == 8:
        name = input("Enter Name of the Staff Member : ")
        checkout(list_staff,name)
        display_staff(list_staff)

############################## checkout visitor ##################################

    if ch == 9:
        name = input("Enter Name of the Visitor : ")
        checkout(list_visitor,name)
        display_visitors(list_visitor)

print("END")
