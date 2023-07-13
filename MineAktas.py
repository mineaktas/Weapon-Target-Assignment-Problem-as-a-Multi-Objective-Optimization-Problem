
# Tucker - Miller

N=8
x="x"

for i in range(N):
    for j in range(N):
        if i==j:
            pass
        else:
            r=x+"u"+str(i)+"-"+x+"u"+str(j)+"+"+str(N)+"*"+x+str(i)+str(j)+"<="+str(N-1)+";"
            print(r)
    r = x+"u"+str(i)+">="+str(1)+";"
    print(r)
    r = x+"u"+str(i)+"<="+str(N-1)+";"
    print(r)


for i in range(N):
    for j in range(N):
        print("@bin("+x+str(i)+str(j)+");")

for i in range(N):
    print("@gin("+x+"u"+str(i)+");" )

