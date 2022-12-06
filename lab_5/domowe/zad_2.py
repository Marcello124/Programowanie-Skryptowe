# from collections import Counter
# import sys

# dict(Counter(map(len, sys.stdin.read())))

from collections import Counter; import sys; result = dict(Counter(map(len, sys.stdin.read().split()))); print(result)