def solution(N):
    number = bin(N)[2:]
    count = 0
    last = 0
    max = 0
    for i in number:
        if i == '0':
            if last == '0':
                count += 1
            else:
                count = 1
        if count > max:
            max = count
    print(number)
    return max
print(solution(50))
