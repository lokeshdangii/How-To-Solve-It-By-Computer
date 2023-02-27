num = 0
# dict1 = {}
dictcount = {}
number = []

for i in range(0,100):
    num = num + 1
    list1 = []
    for i in range(2,num+1):
        if num%i == 0:
            list1.append(i)
    no_of_divsrs = len(list1)
    # dict1.update({num:list1})
    dictcount.update({num:no_of_divsrs})

# print(dict1)
# print(dictcount)

max_value = max(dictcount.values())
print("maximum value : ",max_value)
 

for x, y in dictcount.items():
  if y == max_value:
      number.append(x)
print("From 1 to 100 the number with the most divisors is : ",number)

"""
# taking list of dictionary values in v
v = list(dictcount.values())
 
# taking list of dictionary keys in k
k = list(dictcount.keys())

max_div_of_num = k[v.index(max(v))]
print(max_div_of_num)

# another way to get the maximum from the dictionary
# print(max(dictcount, key=dictcount.get))
"""