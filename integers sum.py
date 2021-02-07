sum = 0


def calculateDigitsSum(number: int) -> int:
    global sum
    if number // 10 == 0:
        sum += number % 10
        return 0
    else:
        num = number % 10
        sum += num
        number //= 10
        return calculateDigitsSum(number)

calculateDigitsSum(1234)
print(sum)