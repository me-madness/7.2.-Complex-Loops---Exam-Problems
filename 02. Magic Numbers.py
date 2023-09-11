n = int(input())
result = ''
for a in range(1, 10):
    for b in range(1,10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        if a * b * c * d * e * f == n:
                            result += ('' + str(a) + str(b) 
                                          + str(c) + str(d) 
                                          + str(e) + str(f) + '')
print(result)

# Second way
n = int(input())
result = ''
a = 1

while a <= 9:
    b = 1
    while b <= 9:
        c = 1
        while c <= 9:
            d = 1
            while d <= 9:
                