import random as rand

dummy_data = [list for i in range(1,21)]

class Patient ():
  def __init__(self ,specialization,name ,status ):
    self.specialization = specialization
    self.name = name
    self.status = status
  def patient_data(self):
      return [self.specialization,self.name,self.status]

def create_dummy_data():
    dummy_data = []
    for spec in range(1,21):
        spec_list = [ ]
        for p in range(rand.randint(1, 10)):
           name = 'dummy'+str(p)
           status = rand.choice([0,1,2])
           specialization = spec
           spec_list.append(Patient(specialization,name,status))
        dummy_data.append(spec_list)
    return dummy_data




def Print_all_patient(dummy_data):

    for spec in range(len(dummy_data)):
        q = dummy_data[spec]
        q = sorted(q, key=lambda Patient: Patient.status, reverse=True)
        print('Specialization ' + str(spec+1) + ': There are ' + str(len(q)) + ' patient')
        for o in range(len(dummy_data[spec])):
            if q[o].status == 0:
                print('patient:',q[o].name,'is','Normal')
            if q[o].status == 1:
                print('patient:',q[o].name,'is', 'Urgent')
            if q[o].status == 2:
                print('patient:',q[o].name,'is', 'Super Urgent')



def  Get_next_patient(specialization,dummy_data):
    q = dummy_data[specialization-1]
    q = sorted(q, key=lambda Patient: Patient.status, reverse=True)
    return q[0].name

def Remove_leaving_patient(specialization,name,dummy_data):
    is_exist = False

    for i in range(len(dummy_data[specialization-1])):
        if dummy_data[specialization-1][i].name == name:
            is_exist =True
            dummy_data[specialization-1].pop(i)
            break

    if is_exist == False:
        print('No patient with such a name in this specialization!')


def Add_patient(specialization,name ,status,dummy_data):
    P = Patient(specialization,name,status)
    q = dummy_data[specialization-1]
    q = sorted(q, key=lambda Patient: Patient.status ,reverse=True)
    size = len(q)
    for i in range(len(dummy_data[specialization - 1])):
        ss = dummy_data[specialization - 1]
        print(ss[i].name , ss[i].status,ss[i].specialization)
    if size < 10:
        if status == 0:
            q.append(P)
        elif status == 1:
            for i in range(size):
                if (q[i].status == 1 and q[i+1].status == 0) or (q[i].status == 2 and q[i+1].status == 0 ) :
                    q.insert(i+1,P)
                    break
                elif i == size-1:
                    q.append(P)

        elif status ==2:
            for i in range(size):
                if (q[i].status == 2 and q[i + 1].status == 1):
                    q.insert(i + 1, P)
                    break

                if (q[i].status == 1 and q[i+1].status == 0):
                    q.insert(i,P)
                elif i == size-1:
                    q.append(P)
        dummy_data[specialization - 1] = q
        print('Specialization '+str(specialization)+': There are '+str(len(q))+' patient')
        for o in range(len(q)):
            if q[o].status == 0:
                print('patient:',q[o].name,'is','Normal')
            if q[o].status == 1:
                print('patient:',q[o].name,'is', 'Urgent')
            if q[o].status == 2:
                print('patient:',q[o].name,'is', 'Super Urgent')
    else:
        print('Sorry we can\'t add more patient for this specialization at the moment')

dummy_data = create_dummy_data()

while True :

    option = int(input(''' Program Options:
    1) Add new patient
    2) Print all patient
    3) Get next patient
    4) Remove a leaving patient
    5) End the program
    Enter your choice (from 1 to 5):
    '''))
    if option == 1:
        specialization = int(input('Enter specialization: '))
        name = input('Enter patient name: ')
        status = int(input('Enter status (0 normal / 1 urgent / 2 super urgent): '))
        Add_patient(specialization,name,status,dummy_data)
    elif option == 2:
        Print_all_patient(dummy_data)
    elif option == 3:
        specialization = int(input('Enter specialization: '))
        name = Get_next_patient(specialization,dummy_data)
        print(name + ', Please go with the Dr')
    elif option == 4:
        specialization = int(input('Enter specialization: '))
        name = input('Enter patient name: ')
        Remove_leaving_patient(specialization,name,dummy_data)
    elif option == 5:
        break







