class Patient:
    def __init__(self,name, sugar_in, fat_in, salt_in):
        self.name = name
        self.sugar = sugar_in
        self.fat = fat_in
        self.salt = salt_in

    def is_healthy(self):
        if self.sugar_in > 37.5 :
            print(f'{self.name}, your sugar intake is {self.sugar_in}, and it is high.')
        else:
            print(f'{self.name}, your sugar intake is okay.')
        if self.fat_in > 77 :
            print(f'{self.name}, your fat intake is {self.fat_in}, and it is high.')
        else:
            print(f'{self.name}, your fat intake is okay.')
        if self.salt_in > 2300 :
            print(f'{self.name}, your salt intake is {self.salt_in}, and it is high.')
        else:
            print(f'{self.name}, your salt intake is okay.')

patient_record = []
for i in range(3):
    pat_name = input('Your name: ')
    pat_sugar = float(input('Your sugar intake: '))
    pat_fat = float(input('Your fat intake: '))
    pat_salt = float(input('Your salt intake: '))
    Patient = Patient(pat_name,pat_sugar,pat_fat,pat_salt)
    patient_record.append(Patient)

for k in range(3):
    patient_record[k].is_healthy()

