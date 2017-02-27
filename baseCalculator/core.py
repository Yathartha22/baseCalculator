from dic import hexdic
def convert(N, b):
        number = N
        ans=''
        if N == 0:
                return None
        
        while N > 0:
                res = int(N%b)
                ans += str(res)
                N //= b
        if number < b:
                if b == 16:
                       return hexdic[int(ans)] 
                else:
                        return ans
        else:
                return ans[::-1]
print(convert(64,16))
