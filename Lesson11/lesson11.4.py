# Write a python function, which add a new value
# with given key in dict.

def add_value(dict,key,value):
    dict[key]=value
my_dict={'name':'Ani'}
add_value(my_dict,'surname','Balyan')
print(my_dict)



# Write a python program which concat 2 dicts.
def concat_dicts(dict1, dict2):
    return{**dict1,**dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(concat_dicts(dict1, dict2))

# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

def new_dict(N):
    result = {i: i**3 for i in range(1, N + 1)}
    return result

N = int(input())
print(new_dict(N))

# Write a python function which create dict from 2
# lists with the same length

def create_dict(list1,list2):
    if len(list1)==len(list2):
        result={}
        for i in range(len(list1)):
            result[list1[i]] = list2[i]
        return result
    else:
        return 'false'
list1=['a','b','c','d']
list2=[1,2,3,4]
print(create_dict(list1,list2))