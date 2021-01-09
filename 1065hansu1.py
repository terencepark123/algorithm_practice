a = int(input())
sum = 0
    
for i in range(1,a+1): #1부터 a까지 의 수에 대해 
    temp = list(map(int, str(i))) 
    print(temp)
    if len(temp) <=2: # 자릿수가 1,0일 경우 자동 만족
        sum += 1
    else: # 자릿수가 2 이상 일 경우
        arr = []
        for j in range(len(temp)-1): # 자릿수 - 다음 자릿수 저장
            arr.append(temp[j] -temp[j+1] ) 
        iter = 0
        while iter<len(arr) -1:

            if arr[iter]==arr[iter+1]: # 
                iter+=1
            else:
                iter = len(arr)    
        if iter == len(arr)-1:
            sum +=1
print(sum)
