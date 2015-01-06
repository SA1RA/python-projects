import time

countdown = 5

while countdown > 0:
    print('self destructing in ...')
    print(countdown)
    countdown -= 1
    time.sleep(1)

print('B' + 'A' * 100 + 'M!!!')
