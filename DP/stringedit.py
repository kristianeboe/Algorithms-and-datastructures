def stringedit(r_word, w_word):
    c = [[1]*len(r_word)]*len(w_word)
    if r_word[0] == w_word[0]:
        c[0][0] = 0
    else:
        c[0][0] = 1
    for col in range(1,len(c[0])):
        c[0][col] = c[0][col-1]+1
    #for row in range(1,len(c)):
    #    c[row][0] = c[row-1][0]+1
    print c
    print c[0]
    print c[1]
    print
    prinstString = ""
    for row in c:
        for col in row:
            prinstString = prinstString + str(col)
        print prinstString+" "
        prinstString = ""


stringedit("gulrot", "gullerot")
