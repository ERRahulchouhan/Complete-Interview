Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

import pickle

# # filename = open("new","ab")
# # pickle.dump(Omkar, filename)

# with open("new" , "rb") as fileread:
#     a = pickle.load(fileread)
#     print(a)


with open("new" , "rb") as file:
    a = pickle.load(file)
    print(a)