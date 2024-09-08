def obfuscateCardMetadata(card_bin, card_intervals):
    # Read every line of card_intervals and store it in a list
    intervals = []
    for line in card_intervals:
        intervals.append(line.split(","))

    # Iterate through the intervals
    checkpoints=[]
    for interval in intervals:
        checkpoint = []
        checkpoint.append(interval[0])
        checkpoint.append("START")
        checkpoint.append(interval[2])
        checkpoints.append(checkpoint)
        checkpoint = []
        checkpoint.append(interval[1])
        checkpoint.append("END")
        checkpoint.append(interval[2])
        checkpoints.append(checkpoint)
    print(checkpoints)

    # Sort the checkpoints after checkpoints[0]
    checkpoints.sort(key=lambda x: x[0])
    print(checkpoints)

    checkpoints[0][0] = "0000000000"
    checkpoints[len(checkpoints) - 1][0] = "9999999999"

    l = len(checkpoints)
    i=0
    while i<l-2:
        if checkpoints[i][1]=="END" and checkpoints[i+1][1]=="START" and checkpoints[i][2]!=checkpoints[i+1][2]:
            checkpoints[i][0]=str(int(checkpoints[i+1][0])-1)
        elif checkpoints[i][1]=="END" and checkpoints[i+1][1]=="START" and checkpoints[i][2]==checkpoints[i+1][2]:
            j=i+2
            while j<len(checkpoints)-1:
                if checkpoints[j][1]=="END" and checkpoints[j][2]==checkpoints[i+1][2]:
                    checkpoints.pop(i)
                    checkpoints.pop(i)
                    l-=2
                    break
            i-=1
        i+=1
    print(checkpoints)
    results=[]

    while len(checkpoints)>1:
        i=1
        while i<=len(checkpoints)-1:
            if checkpoints[i][1]=="END" and checkpoints[i][2]==checkpoints[0][2]:
                result=[]
                result.append(str(card_bin))
                result[0]+=checkpoints[0][0]
                result.append(str(card_bin))
                result[1]+=checkpoints[i][0]
                result.append(checkpoints[i][2])
                results.append(result)
                checkpoints.pop(i)
                checkpoints.pop(0)
            i+=1
    results.sort(key=lambda x: x[0])
    for result in results:
        print(str(result))



card_intervals = ["4000000000,5999999999,MASTERCARD","1000000000,2999999999,VISA","3000000000,3499999999,VISA","4500000000,4999999999,AMEX"]
card_bin=777777
obfuscateCardMetadata(card_bin, card_intervals)
