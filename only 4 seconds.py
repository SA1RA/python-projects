import time

countdown = 5

while countdown > 0:
    print('self destructing in ...')
    print(countdown)
    countdown -= 1
    time.sleep(1)

print('B' + 'O' * 100 + 'M!!!')
