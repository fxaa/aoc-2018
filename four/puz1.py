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

for i in range(len(lines)):
    if lines[i][1] == "Guard":
        current = lines[i][1] + " " + lines[i][2]
    
    elif lines[i][1] == "falls":
        if current not in sleep_times:
            sleep_times[current] = (timedelta(0), lines[i][0], [0 for i in range(60)])
        else:
            sleep_times[current] = (sleep_times[current][0], lines[i][0], sleep_times[current][2])
    
    elif lines[i][1] == "wakes":
        time_now = lines[i][0]
        old_time = sleep_times[current][1]
        new_minutes = sleep_times[current][2]
        for j in range(time_now.minute - old_time.minute):
            new_minutes[j+old_time.minute] += 1
        sleep_times[current] = (sleep_times[current][0] + (time_now - old_time), None, new_minutes)
    
longest = [timedelta(0)]
for guard in sleep_times:
    if sleep_times[guard][0] > longest[0]:
        longest = sleep_times[guard]
        worst = guard

worst = int(worst.split(' ')[1][1:])
minute_counts = longest[2]
minute = -1
idx = 0
for i in range(len(minute_counts)):

    if minute_counts[i] > minute:
        minute = minute_counts[i]
        idx = i

print(worst*idx)

