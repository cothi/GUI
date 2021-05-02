import time

def createGenerator():

    mylist = [i for i in range(1, 30)]

    for i in mylist:
        
        time.sleep(1)
        if i % 2:
            yield i


for i in createGenerator():
    print(i)
