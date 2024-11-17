class Symptom:
    def __init__(self,name):
        self.name=name
        self.description=""
        self.fast_acting=False
    
    def set_name(self,new_name):
        self.name=new_name

    def set_description(self,new_description):
        self.description=new_description

    def set_fast_acting(self,new_fast_acting):
        self.fast_acting=new_fast_acting
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def is_fast_acting(self):
        return self.fast_acting

    def __str__(self):
        return self.name