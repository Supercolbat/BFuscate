from functools import reduce



def find(substring, string):
    indexes = []
    index   = -1

    while (ind := string[index+1:].find(substring)) != -1 and index < len(string):
        index = ind + index + 1
        indexes.append(index)
    
    return indexes



def split(num):
    nums   = [num]
    ptr    = 0
    offset = 0
    lastn  = None

    while ptr < len(nums):
        while not nums[ptr] in [1, 2, 3, 5, 7]:
            if nums[ptr] == lastn:
                if nums[ptr+1:]:
                    offset += reduce(lambda x,y:x*y, nums[ptr+1:])
                else:
                    break
                    
                nums[ptr] += 1

            lastn = nums[ptr]
            
            for i in [2, 3, 5, 7]:
                if nums[ptr]%i == 0:
                    nums[ptr] //= i
                    nums.append(i)
                    break
    
        ptr += 1
    
    
    nums = sorted(nums)
    l = {}
    for i in nums:
        if not i in l and nums.count(i):
            l[i] = nums.count(i)

    return (l, offset)
