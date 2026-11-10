# import asyncio
# import time

# async def func1():
#     await asyncio.sleep(4)
#     print("hello")
    
# async def func1():
#     await asyncio.sleep(4)
#     print("hello1")
    
# async def func2():
#     print("hello2")

# async def main():
#     await asyncio.gather(func1(),func2())


# asyncio.run(  
#             main()  
# )


import csv

h = ['name','roll']
d = [['raj',1], ['rahul',2]]

# with open("my.csv","w") as file:
#     csvwriter =     csv.writer(file)
#     csvwriter.writerow(h)
#     csvwriter.writerows(d)

# import pickle

# d = {"name" :"raj"}
# with open("pickl" ,"wb") as p:
#     pickle.dump(d, p)
    
# with open("pickl","rb") as f :
#     d =  pickle.load(f)
#     print(d)

d = open("my.csv")
print(d.readlines())