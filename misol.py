n = int(input())
nums =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
toq_nums = []
for num in nums:
    if num % 2 != 0:
        toq_nums.append(num)
    if len(toq_nums) == 5:
        break
print(toq_nums)
    