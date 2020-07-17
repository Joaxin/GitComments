#! python3
# stopwatch.py - A simple stopwatch program.
'''
假设要记录在没有自动化的枯燥任务上花了多少时间。你没有物理秒表，要为
笔记本或智能手机找到一个免费的秒表应用，没有广告，且不会将你的浏览历史发
送给市场营销人员，又出乎意料地困难（在你同意的许可协议中，它说它可以这样做。
你确实阅读了许可协议，不是吗？）。
'''

import time

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        # 向 print()函数传入 end=''，避免输出重复空行
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
