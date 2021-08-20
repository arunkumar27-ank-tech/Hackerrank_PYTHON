import re
for _ in range(int(input())):
    N = input()
    try:
        x =re.search(N,N)
        print(True)
    except:
        print(False)