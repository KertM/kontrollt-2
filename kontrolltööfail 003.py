#3
List1 = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
List2 = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]

#1)
print("sarnased:")
print(set(List1) & set(List2))

#2)
suurim1 = max(List1)
suurim2 = max(List2)
List3 = [suurim1, suurim2]
suurim = max(List3)
print("kõige suurim on: ", + suurim)
#3)
väikseim1 = min(List1)
väikseim2 = min(List2)
List4 = [väikseim1, väikseim2]
väikseim = min(List4)
print("kõige väikseim on: ", + väikseim)
#4)
print("keskmine list 1'l on: ", + sum(List1))
print("keskmine list 2'l on: ", + sum(List2))
#5)
print("kahe listi keskmine on:", sum(List1) + sum(List2))
