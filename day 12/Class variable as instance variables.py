class myClass():
    species="Human"
    def __init__(self,species,name):
        self.species=species
        self.name=name

p1=myClass("Animal","Tom")

print(p1.name)
print(p1.species)           # Animal (instance variable)
print(myClass.species)      # Human (class variable - unchanged!)

# Here class variable will remain unchanged and instance variable will change as per object