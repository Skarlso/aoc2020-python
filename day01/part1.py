my_file=open("day01/input.txt","r")
content = my_file.read()
nums = [int(i) for i in content.split('\n')]

for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == 2020:
            print(nums[i]*nums[j])
            exit(0)

# this would also work, but makes no sense. Just practicing list
num = [nums[i]*nums[j] for i in range(0, len(nums)-1) for j in range(i+1, len(nums)) if nums[i]+nums[j] == 2020]
print(num)