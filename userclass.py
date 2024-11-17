#This is the User Class



class User:
    def __init__(self, user_id, name, age, gender, diagnosis, medication, allergies, height, weight):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.medication = medication
        self.allergies = allergies
        self.height = height
        self.weight = weight
        self.symptoms_logs = []
        
    def get_user_id(self):
        return self.user_id

    def set_user_id(self, new_user_id):
        self.user_id = new_user_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_diagnosis(self):
        return self.diagnosis

    def set_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis

    def get_medication(self):
        return self.medication

    def set_medication(self, new_medication):
        self.medication = new_medication

    def get_allergies(self):
        return self.allergies

    def set_allergies(self, new_allergies):
        self.allergies = new_allergies 

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

    def add_symptom_log(self, log):
        self.symptoms_logs.append(log)


    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
            f"Diagnosis: {self.diagnosis}, Medication: {self.medication}, "
            f"Allergies: {self.allergies}, Height: {self.height} in, Weight: {self.weight} lbs")

    

  
