class Temperature:
    def __init__(self, celsius):
       
        self._celsius = celsius

    @property
    def celsius(self):
        
        print("Getting value...")
        return self._celsius

   
t = Temperature(25)

current_temp = t.celsius
print(f"Current temp: {current_temp}")


