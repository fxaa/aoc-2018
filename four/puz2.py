from datetime import *

file = open('input.txt', 'r')
lines = []
line = file.readline()[:-1]
while len(line) > 1:
    lines.append(line)
    line = file.readline()[:-1]


for i in range(len(lines)):
    lines[i] = [datetime.strptime(lines[i][1:17], "%Y-%m-%d %H:%M")] + lines[i][19:].split(' ')[0:2]

lines.sort(key=lambda x: x[0])
sleep_times = {}
minute_sleeps = [{} for i in range(60)]

for i in range(len(lines)):
    if lines[i][1] == "Guard":
        current = lines[i][1] + " " + lines[i][2]
    
    elif lines[i][1] == "falls":
        if current not in sleep_times:
            sleep_times[current] = (timedelta(0), lines[i][0])
        else:
            sleep_times[current] = (sleep_times[current][0], lines[i][0])
    
    elif lines[i][1] == "wakes":
        time_now = lines[i][0]
        old_time = sleep_times[current][1]
        for j in range(time_now.minute - old_time.minute):
            if current in minute_sleeps[j+old_time.minute]:
                minute_sleeps[j+old_time.minute][current] += 1
            else: 
                minute_sleeps[j+old_time.minute][current] = 1
        sleep_times[current] = (sleep_times[current][0] + (time_now - old_time), None)
    
sleeper = None
big_minute = 0
big_minute_amount = 0
for i in range(len(minute_sleeps)):
    for guard in minute_sleeps[i]:
        if minute_sleeps[i][guard] > big_minute_amount:
            sleeper = guard
            big_minute = i
            big_minute_amount = minute_sleeps[i][guard]

sleeper = int(sleeper.split(' ')[1][1:])

print(sleeper*big_minute)