# lst = ['aba', '12221', 'rewr', 'aau']
# ctr = 0
# for i in lst:
#     if len(i) > 1 and i[0] == i[-1]:
#         ctr += 1
# print(ctr)


l1 = [1, 2, 3]
l2 = [1, 2, 6]


print(set(l1) - set(l2))
print(list(set(l1).difference(set(l2))))
