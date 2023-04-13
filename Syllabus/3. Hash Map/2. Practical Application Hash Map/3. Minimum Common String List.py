from typing import List

def findRestaurant(list1: List[str], list2: List[str]):
  string_index_mapping = dict()
  min_index_sum = [len(list1), len(list1)]

  for i, s in enumerate(list1):
    string_index_mapping[s] = i

  for i, s in enumerate(list2):
    if s in string_index_mapping and (string_index_mapping[s] + i) < sum(min_index_sum):
      print(i, s, min_index_sum)
      print(string_index_mapping[s] + i)
      min_index_sum = [string_index_mapping[s], i]

  return [list1[min_index_sum[0]], list2[min_index_sum[1]]]

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))