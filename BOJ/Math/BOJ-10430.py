nums = (input()).split()

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
