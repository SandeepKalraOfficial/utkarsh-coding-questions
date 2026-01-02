dict_1 = {0:2, 1:7}
dict_2 = {0:5, 1:2, 2:4, 3:8, 4:9, 5:3}
sum_dict = {}
for key in set(dict_1)|set(dict_2):
    sum_dict[key] = dict_1.get(key,0)+dict_2.get(key, 0)
 
print(sum_dict)