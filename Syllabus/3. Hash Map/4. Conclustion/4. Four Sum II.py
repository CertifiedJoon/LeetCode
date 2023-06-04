def four_sum_II(nums1, nums2, nums3, nums4):
  first_two = dict()
  cnt = 0
  for i in range(len(nums1)):
    for j in range(len(nums2)):
      key = nums1[i] + nums2[j]
      if key not in first_two:
        first_two[key] = [[i, j]]
      else:
        first_two[key].append([i, j])
  
  for k in range(len(nums3)):
    for l in range(len(nums4)):
      key = nums3[k] + nums4[l]
      if -key in first_two:
        cnt += len(first_two[-key])

  return cnt

print(four_sum_II(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))