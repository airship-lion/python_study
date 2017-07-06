print("all")
print(all([1, 2]))
print(all([1, 2, 0]))
print(all([]))
print()
print("any")
print(any([1, 2]))
print(any([1, 2, 0]))
print(any([0, 0]))
print(any([]))
print()
print("sorted")
a = {4: 103, 2: 11, 7: 88, 6: 99}
print(a)
print(sorted(a.items()))
print(sorted(a.items(), key=lambda x: x[1]))
print()
print("zip")
b = [1, 2, 3, 4]
c = ["a", "b", "c"]
for item in zip(b, c):
    print(item)

print()
print("import")
# import iterable_test
__import__("iterable_test")
