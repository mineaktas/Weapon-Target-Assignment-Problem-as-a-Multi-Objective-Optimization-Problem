weapon=5
site=2
target=7
for s in range (1,site+1):
    for w in range(1,weapon+1):
        for t in range (1,target+1):
            print("@bin(y"+str(w)+str(t)+str(s)+");")
