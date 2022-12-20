import re

n = int(input())
s = input().split()
b = input()

word_count = 0

i = 0
for j in range(len(s)):
    len_ = len(s[j])
    word_mask = b[i:i+len_]
    i = len_
    regex = re.compile(r'^.*(.)(\1)(\1).*$')
    if regex.match(word_mask):
        word_count += 1

print(word_count)


