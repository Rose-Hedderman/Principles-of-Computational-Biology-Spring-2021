L1 = ['G']
L2 = ['C']
L3 = ['T']
L4 = ['A']
L5 = L1 + L2
L3.extend(L4)
L3.extend(L2)
L3.sort()
L3.pop()
del(L3[0])
L3.extend(['T','T'])
print(L3)
