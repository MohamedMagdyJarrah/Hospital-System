from operator import itemgetter
import random

def printChoices():
  print("Program Options:")
  print("1) Add new Patient","2) Print all patients.","3) Get next patient.","4) Remove a leaving patient","5) End the program.",sep='\n')

specializations=[[] for i in range(20)]

class patient():
    def __init__(self, noSpec):
        self.noSpec = noSpec
        self.queue = []

    def store(self,name,status):
        self.name= name
        self.status = status
        self.queue.append([name,status])
        if len(self.queue) > 10 :
            self.queue.pop()

    def checkQueue(self):
        if len(self.queue) == 10 :
            return False
        else:
            return True

    def printingQueue(self):
        self.sorting = self.queue
        for i in range(len(self.queue)):
            self.sorting[i][0] = self.queue[i][0]
            if self.queue[i][1] == "Super Urgent":
                self.sorting[i][1] = 0
            elif self.queue[i][1] == "Urgent":
                self.sorting[i][1] = 1
            elif self.queue[i][1] == "Normal":
                self.sorting[i][1] = 2
        self.sorting = sorted(self.sorting, key=itemgetter(1))
        # print(self.sorting)
        for i in range(len(self.sorting)):
            self.sorting[i][0] = self.sorting[i][0]
            if self.sorting[i][1] == 0:
                self.sorting[i][1] = "Super Urgent"
            if self.sorting[i][1] == 1:
                self.sorting[i][1] = "Urgent"
            if self.sorting[i][1] == 2:
                self.sorting[i][1] = "Normal"
        self.queue = self.sorting

        if len(self.queue) > 0 :
            print(f"Specialization {self.noSpec}: There are {len(self.queue)} patients.")
            for i in range(len(self.queue)):
                print(f"Patient: {self.sorting[i][0]} is {self.sorting[i][1]}")
            print()
        else:
            pass

    def getNextPatient(self):
        print(f"{self.sorting[0][0]}, Please go with the Dr")
        self.sorting.pop(0)

    def removePatient(self,name):
        flag = 0
        for i in range(len(self.sorting)):
            # print(self.sorting[i][0])
            if name == self.sorting[i][0]:
                flag = 1
                self.sorting.pop(i)
        if flag == 0:
            print("No Patient with such a name in this specialization!")


for i in range(len(specializations)):
    specializations[i] = patient(i+1)

# ----------------------------------------------------------------------------------------------------------------------------------------------
def dummyData():
    specializations[2] = patient(3)
    specializations[5] = patient(6)
    specializations[8] = patient(9)
    specializations[12] = patient(13)
    specializations[13] = patient(14)

    data = list(range(0,10))
    random.shuffle(data)
    a = ["Normal","Urgent","Super Urgent"]
    for i in range(10):
        specializations[2].store("Dummy" + str(data[i]) , random.choice(a))

    for i in range(4):
        specializations[5].store("AnotherDummy" + str(i), "Normal")
    for i in range(5):
        specializations[8].store("ThirdDummy"+str(i),"Urgant")
    for i in range(3):
        specializations[12].store("ForthDummy" + str(i), "SuperUrgant")

    data1 = list(range(0,6))
    random.shuffle(data1)
    b=["Urgent", "Super Urgent"]
    for i in range(6):
        specializations[13].store("FifthDummy" + str(data1[i]), random.choice(b))

# ----------------------------------------------------------------------------------------------------------------------------------------------

dummyData()
printChoices()
choice = int(input("Enter your choice (from 1 to 5): "))

while choice != 5:
    if choice == 1:
        spec = int(input("Enter specialization: "))
        if specializations[spec-1].checkQueue():
            patient_name = input("Enter Patient Name: ")
            patient_status = int(input("Enter status (0 Normal / 1 Urgent / 2 Super Urgent): "))
            status = ["Normal","Urgent","Super Urgent"]
            specializations[spec - 1].store(patient_name,status[patient_status])
        else:
            print("Sorry, We can't add more Patients for this specialization at the moment.")

    elif choice == 2:
        for i in range(len(specializations)):
            specializations[i].printingQueue()

    elif choice == 3:
        spec = int(input("Enter specialization: "))
        specializations[spec-1].getNextPatient()

    elif choice == 4:
        spec = int(input("Enter specialization: "))
        patient_name = input("Enter Patient name: ")
        specializations[spec - 1].removePatient(patient_name)

    print()
    printChoices()
    choice = int(input("Enter your choice (from 1 to 5): "))