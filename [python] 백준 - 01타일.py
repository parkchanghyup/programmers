n = int(input())


dp = [0] * (n+2) 

# dp [1] : '1' -> 1개
# dp [2] : '11' ,'00'  - > 2개 
# dp [3] : '111',' 100','001' -> 3개
# dp[4] : '1111','1100','1001','0011','0000' -> 5개

# 점화식 : dp[i] = dp[i-1] + dp[i-2]


dp[1] = 1
dp[2] = 2


for i in range(3,n+1):
    
    # dp[i]를 구할때마다 나머지 연산
    dp[i] = (dp[i-1] + dp[i-2])%15746
    
print(dp[n]%15746)