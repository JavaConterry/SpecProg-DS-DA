def parseYWYW(time):
    dot_counter = 0
    iter = 0
    vals = ['']
    for s in time:
        if(s == '.' and dot_counter == 0):
            dot_counter +=1
            iter+=1
            vals.append('')
        elif(s == "-"):
            dot_counter = 0
            iter+=1
            vals.append('')
        else:
            vals[iter] += s
    for i in range(len(vals)):
        vals[i] = int(vals[i])
    return vals[0],vals[1], vals[2], vals[3]


print(parseYWYW("1990.12-2000.12"))