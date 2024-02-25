#a list is like a box, that stores the data you put in it. 
#You can bring out that specific data later by calling it's character count/placement in the list.

list = [10000000, 90, 2, 6,75, 100] 
list.sort()
print(list)


list = []
for i in range(1,10):
    num = int(input("Please enter a number: "))
    list.append(num)
    print(list)
list.sort()
print(list)

# you can put lists inside of lists:
#    0     1    - 0 = list one inside the bigger list and 1 = list two inside the bigger list
# [[3,5] [4,7]]

#-------------------------------------------------------------------------------------------------------

#list practice question

def sum2(nums):
  if len(nums)>=2:
    return nums[0] + nums [1]
  if len(nums)==1:
    return nums[0]
  else:
    return 0

nums = [1,1,2]
print(sum2(nums))

