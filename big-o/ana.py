def anagramSolution(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    for i in range(len(c1)):
        if c1[i] != c2[i]:
            return False
    return True

def main():
    s1 = "popp"
    s2 = "ppop"
    print(anagramSolution(s1, s2))

if __name__ == "__main__":
    main()
