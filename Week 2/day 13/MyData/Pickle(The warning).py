import pickle

# The Python object you want to save
data = {"name": "John", "age": 30, "city": "New York"}


with open('data.pkl', 'wb') as file:
    
    pickle.dump(data, file)