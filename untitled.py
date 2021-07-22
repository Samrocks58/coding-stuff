import threading

r = 69.0
if r == 69:
    print("yay")

def func1():
    while True:
        print("that's so dope")
def func2():
    while True:
        print("that sucks")
t1=threading.Thread(target=func1)
t2=threading.Thread(target=func2)

t1.start()
t2.start()