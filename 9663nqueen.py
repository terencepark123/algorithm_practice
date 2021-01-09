def pruning(branch):
    for i in range(0,len(branch)-1):
        if branch[-1] == branch[i]:
            branches.remove(branch)
            break
        if branch[-1] == branch[i] + (len(branch) -1 - i):
            branches.remove(branch)
            break
        if branch[-1] == branch[i] - (len(branch) -1 - i):
            branches.remove(branch)
            break

Num = int(input())

branches=[]
n = 1
for i in range(Num): # initializing
    branches.append([i])
while n < Num:
    workingd=[]
    n += 1
    for i in range(Num):
        for branch in branches:
            workingd.append(branch + [i])

    branches = workingd.copy()

    for working_branch in workingd:
        if working_branch in branches:
            pruning(working_branch)

print(len(branches))