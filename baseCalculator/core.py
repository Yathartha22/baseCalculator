from dic import hexdic
# Core module for conversion from any base to any other base
# At present only converts decimal to any base b
# TODO: implementing such that `convert` converts from any base to b se b

def convert(N, b):
    # main function that converts decimal number N to any base b
        number = N
        ans=''
        if N == 0:
                return None
        
        while N > 0:
                res = int(N % b)
                ans += str(res)
                N //= b
        if number < b:
                if b == 16:
                       return hexdic[int(ans)] 
                else:
                        return ans
        else:
                return ans[::-1]
