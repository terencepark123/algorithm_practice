a = int(input())
sum = 0
    
for i in range(1,a+1): #1부터 a까지 의 수에 대해 
    temp = list(map(int, str(i))) 
    if len(temp) <=2: # 자릿수가 1,0일 경우 자동 만족
        sum += 1
    else: # 자릿수가 2 이상 일 경우
        cnt = 0
        diff = temp[0] - temp[1] 
        
        for j in range(1,len(temp)-1): # 자릿수의 차이가 동일할 경우 cnt+
            if temp[j] - temp[j+1] == diff:
                cnt +=1
        if cnt == len(temp)-2: #차이가 모두 동일하면
            sum += 1

print(sum)



