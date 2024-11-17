import datetime

class Disease:
    def __init__(self, name, symptoms):
        self.name=name
        self.symptoms=symptoms
        self.timeline=datetime.date(1970,1,1)
        self.severity=0

    def get_name(self):
        return self.name
    
    def get_symptoms(self):
        x=""
        for symptom in self.symptoms:
            x+=str(symptom)+"\n"
        return x
    
    def get_timeline(self):
        return self.timeline
    
    def get_severity(self):
        return self.severity

    def set_name(self,new_name):
        self.name=new_name

    def set_symptoms(self,new_symptoms):
        self.symptoms=new_symptoms

    def set_timeline(self,new_timeline):
        self.timeline=new_timeline

    def set_severity(self,new_severity):
        self.severity=new_severity
    
