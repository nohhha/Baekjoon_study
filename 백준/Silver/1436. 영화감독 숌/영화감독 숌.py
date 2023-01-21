n=int(input())
cnt=0
i=666
while True:
    if '666' in str(i):
        cnt+=1
        if cnt==n:
            print(i)
            break
        else:
          i+=1
    else:
      i+=1
