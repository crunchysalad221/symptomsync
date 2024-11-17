
#This is the code for the symtpom Log class

class SymptomLog:
    def __init__(self, symptom_type, description, severity):
        self.symptom_type = symptom_type #Type of symptom ('physical' or 'mental')
        self.description = description#Symptom description (e.g., 'Headache', 'Fatigue')
        self.severity = severity #Severity scale (1 to 5)

    def __str__(self):
        return f"{self.symptom_type.capitalize()} Symptom: {self.description} (Severity: {self.severity})"

