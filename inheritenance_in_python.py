class BaseList:
    def __init__(self, data):
        self.data = data
 
    def get_value(self, index):
        if index<len(self.data):
            return self.data[index]
        return 0
 
class SumList(BaseList):
    def sum_with(self, other_list):
        result  =[]
        max_len = max(len(self.data), len(other_list.data))
 
        for i in range(max_len):
            total = self.get_value(i)+other_list.get_value(i)
            result.append(total)
 
        return result
 
list1 = SumList([2,7])
list2 = SumList([5,1,3,8,4])
 
list_sum = list1.sum_with(list2)
print(list_sum)