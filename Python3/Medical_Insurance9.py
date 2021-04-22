class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):
        estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi + \
            425*self.num_of_children + 2400*self.smoker - 12500
        print(f'{self.name}’s estimated insurance costs is {estimated_cost} dollars.')

    def update_age(self, new_age):
        self.age = new_age
        print(f'{self.name} is now {self.age} years old.')
        self.estimated_insurance_cost()

    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        print(f"{self.name} has {self.num_of_children} {'child' if self.num_of_children == 1 else 'children'}.")
        self.estimated_insurance_cost()

    def update_bmi(self, new_bmi):
        self.bmi = new_bmi
        print(f"{self.name} now has a BMI of {self.bmi}.")
        self.estimated_insurance_cost()

    def update_smoking_status(self, new_smoker):
        self.smoker = new_smoker
        print(f"{self.name} is now a {'smoker' if self.smoker == 1 else 'non-smoker'}.")
        self.estimated_insurance_cost()

    def patient_profile(self):
        patient_information = {}
        p1_k = [a for a in dir(self) if (not a.startswith(
            '__')) and (not '<' in str(getattr(self, a)))]
        for i in p1_k:
            patient_information[i] = getattr(self, i)
        return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
p1_k = [a for a in dir(patient1) if not a.startswith('__')]
print(patient1.patient_profile())
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
patient1.update_bmi(23)
patient1.update_smoking_status(1)
patient1.patient_profile()
print(patient1.patient_profile())
