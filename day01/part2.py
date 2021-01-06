my_file=open("day01/input.txt","r")
content = my_file.read()
nums = [int(i) for i in content.split('\n')]

for i in range(0, len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for g in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[g] == 2020:
                print(nums[i]*nums[j]*nums[g])
                exit(0)