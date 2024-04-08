import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().strip()
for i in croatia:
    s = s.replace(i, 'a')
    
print(len(s))
