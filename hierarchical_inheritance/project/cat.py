from hierarchical_inheritance.project.animal import Animal

class Cat(Animal):
    
    def __init__(self):
        super().__init__()
        
    def meow(self):
        return "meowing..."
