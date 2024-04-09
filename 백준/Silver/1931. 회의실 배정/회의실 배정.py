import sys

N = int(sys.stdin.readline().strip())
meeting = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: (x[1], x[0]))
meetingCount = 0
endTime = 0
for start, end in meeting:
    if start >= endTime:
        endTime = end
        meetingCount += 1

print(meetingCount)
