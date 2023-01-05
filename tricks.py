#we have 2d array with only 2 element in it
# need to sort according to a[0] as well as a[1]

a = [[10,16],[2,8],[999,6],[7,12]]
a.sort()
print(a)
a.sort(key=lambda x:x[1]) #sorting according to 2nd ele in array
print(a)

"""
output:
[[2, 8], [7, 12], [10, 16], [999, 6]]
[[999, 6], [2, 8], [7, 12], [10, 16]]
"""
