if __name__ == '__main__':
    N = int(input())
    l = [input().split() for i in range(N)]
    # print(l[1][0])
    for i in range(len(l)):
        if l[i][0] == "insert":
            l.insert(int(l[i][1]), int(l[i][2]))

        elif l[i][0] == "remove":
            l.remove(int(l[i][1]))

        elif l[i][0] == "print":
            print(l)

        elif l[i][0] == "append":
            l.append(int(l[i][1]))

        elif l[i][0] == "sort":
            l.sort()