import pickle

my_dict={"name":"Avinash", "age":22}

with open("my_dict.pkl","wb") as f:
    pickle.dump(my_dict,f)

with open("my_dict.pkl","rb") as f:
    my_dict_loaded=pickle.load(f)

print(my_dict_loaded)