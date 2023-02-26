import pickle

class exam:
    num=35
    st="meow"
    l=[1,2,3]
    dict={"first":"a","second":"b"}
    tup=(3,8)

obj = exam()
pickobj=pickle.dumps(obj)
print(pickobj)