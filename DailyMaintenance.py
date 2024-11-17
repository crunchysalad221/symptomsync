from userclass import *

class DailyMaintenance:
    def __init__(self,user,sleep_hours):
        self.user=user
        self.sleep_hours=sleep_hours
        self.blood_glucose=0
        self.a1c=0
        self.weight=user.get_weight()
        self.meals=0
        self.heartrate=0
        self.blood_pressure=0
        self.physicalsymptom_logs = []
        self.mentalsymptom_logs = []

    def set_user(self,new_user):
        self.user=new_user
    def set_sleep(self,new_sleep):
        self.sleep_hours=new_sleep
    def set_blood_glucose(self,new_blood_glucose):
        self.blood_glucose=new_blood_glucose
    def set_a1c(self,new_a1c):
        self.a1c=new_a1c
    def set_weight(self,new_weight):
        self.weight=new_weight
    def set_meals(self,new_meals):
        self.meals=new_meals
    def set_heartrate(self,new_heartrate):
        self.heartrate=new_heartrate
    def set_blood_pressure(self,new_blood_pressure):
        self.blood_pressure=new_blood_pressure

    def get_user(self):
        return self.user
    def get_sleep(self):
        return self.sleep_hours
    def get_blood_glucose(self):
        return self.blood_glucose
    def get_a1c(self):
        return self.a1c
    def get_weight(self):
        return self.weight
    def get_meals(self):
        return self.meals
    def get_heartrate(self):
        return self.heartrate
    def get_blood_pressure(self):
        return self.blood_pressure

    def get_symptom_logs(self):
        return {"physical": self.physicalsymptom_logs, "mental": self.mentalsymptom_logs}

    def document_physicallog(self, symptom_log):
        self.physicalsymptom_logs.append(symptom_log)

    def document_mentallog(self, symptom_log):
        self.mentalsymptom_logs.append(symptom_log)
