dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
lis = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


RomanString='MCMXCIV'
IN = 0
Str = list(RomanString)
Str.reverse()
i = 0

while i < (len(Str)):
    IN +=dic[Str[i]]
    # print(f'{i} {IN}')
    if i<(len(Str)-1):
        while lis.index(Str[i+1]) < lis.index(Str[i]):
            IN -=dic[Str[i+1]]
            i+=1
            # print(f'{i} {IN}')
            if i >= (len(Str)-1):
                break


    i+=1


print(IN)
