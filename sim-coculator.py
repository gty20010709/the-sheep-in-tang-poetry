def jaccard_similarity(s1, s2):
    set1 = set(list(s1))
    set2 = set(list(s2))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)


text1 = """
黃花古城路，上盡見青山。
"""
text2 = """
黃花古城路，上盡見青山。
"""
print(jaccard_similarity(text1, text2))
