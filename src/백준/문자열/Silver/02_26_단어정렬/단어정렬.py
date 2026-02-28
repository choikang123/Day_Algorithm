import sys
input=sys.stdin.readline

n=int(input())

words=[input().strip() for _ in range(n)]

words=list(set(words))
words.sort(key=lambda w:(len(w),w))

print("\n".join(words))