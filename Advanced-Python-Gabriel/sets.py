#Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
print(set("my name is Eric and Eric is my name".split()))

#To find out which members attended both events, you may use the "intersection" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))


#To find out which members attended only one of the events, use the "symmetric_difference" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


#To find out which members attended only one event and not the other, use the "difference" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

#To receive a list of all participants, use the "union" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))






#converting list to sets
#finding the difference between two sets


a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))
