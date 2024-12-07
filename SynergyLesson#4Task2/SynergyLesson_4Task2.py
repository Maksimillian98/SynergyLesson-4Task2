number = int(input('Введите пятизначное число: '))

unit = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousends = (number // 1000 ) % 10
ten_thousends = (number // 10000) % 10

step1 = tens ** unit

step2 = step1 * hundreds

step3 = ten_thousends - thousends

step4 = step2 / step3

print(step4)