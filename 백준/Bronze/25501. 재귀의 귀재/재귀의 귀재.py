t=int(input())

strings=[]

for _ in range(t):
    strings.append(input())

def isPalindrome(string, start, end, count):
    if start>=end:
        print(1, count)
        return
  
    if string[start]==string[end]:
        isPalindrome(string, start+1, end-1, count+1)
    else:
        print(0, count)

for i in range(t):
    isPalindrome(strings[i], 0, len(strings[i])-1, 1)