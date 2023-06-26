from difflib import SequenceMatcher


def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()


a = input("String-1 :")
b = input("String-2 :")
res = similar(a, b)
print(str(res))


# import difflib
#
#
# def compute_similarity(input_string, reference_string):
#     diff = difflib.ndiff(input_string, reference_string)
#     diff_count = 0
#     for line in diff:
#         if line.startswith("-"):
#             diff_count += 1
#     return 1 - (diff_count / len(input_string))
#
#
# a = "helLo"
# b = "Hello"
# similarity = compute_similarity(a, b)
# print(similarity)
