n = int(input())
l = int(input())

result = ''

for s1 in range(1, n + 1):
    for s2 in range(1, n + 1):
        for s3 in range(97, l + 97):
            for s4 in range(97, l + 97):
                for s5 in range(max(s1,s2) + 1, n + 1):
                    result += ('' + str(s1) + str(s2) 
                                  + str(s3) + str(s4) 
                                  + str(s5 + ''))