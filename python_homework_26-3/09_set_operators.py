set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

def set_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)



print("Union:", set_union(set1, set2))
print("Intersection:", set_intersection(set1, set2))
print("Difference (set1 - set2):", set_difference(set1, set2))
print("Difference (set2 - set1):", set_difference(set2, set1))
print("Symmetric Difference:", set_symmetric_difference(set1, set2))