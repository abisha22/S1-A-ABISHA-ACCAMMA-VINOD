def find(word):
    wl = []
    for n in word:
        wl.append((len(n), n))
    wl.sort()
    result = wl[-1][0], wl[-1][1]
    print("longest word: ", result[1])
    print("length of the longest word: ", result[0])


find(["hi", "how are uh", "helloii"])
