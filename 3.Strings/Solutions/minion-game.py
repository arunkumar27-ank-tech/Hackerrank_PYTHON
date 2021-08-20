def minion_game(string):
    k=0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            k += len(string)-i
    s = sum(range(1,len(string)+1))-k
    if s>k: print(f"stuart {s}")
    elif k>s: print(f"kevin {k}")
    else:print("Draw")


string = input().upper()
minion_game(string)