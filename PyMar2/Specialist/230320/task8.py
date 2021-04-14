nums = []
for i in range(0,1001,2):
    nums.append(i**2)
nums2 = [x ** 2 if x %3 else x **3 for x in range(0,1001,2)]
