+## 2022 06 06
# 막대기를 오른쪽으로 보았을때 갯수 세기

count = int(input(""))
stick = []
if(2<=count and count<=100000):
    for i in range(count):
        num = int(input(""))

        if(num >= 1 and num <= 100000):
            stick.append(num)
    
    standard = stick[len(stick)-1]
    howManyShow = 1
   
    for i in range(len(stick)-1,-1, -1) :
        if(standard < stick[i]):
            howManyShow += 1
    print(howManyShow)
