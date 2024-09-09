# bogo sort program
import random

def bogo_sort(lst):
    store_lst = lst.copy()
    
    if type(store_lst) == list:
        sorted_list = []
        for i in range(len(store_lst)):
            rand_index = random.randint(0, len(store_lst)-1)
            sorted_list.append(store_lst.pop(rand_index))
            
        return sorted_list
    else:
        return False

#example = [1, 2, 3, 4, 5]
length = 8
# outputs list with size length like [1, 2, 3, 4, 5]
example = list(range(1, length+1))
counter = 1
sort = bogo_sort(example)

while (sort != example):
    sort = bogo_sort(example)
    counter += 1
    print(sort)

print(f"Counter: {counter}")
print(f"Start: {example}") 
print(f"End: {sort}")
