class Solution(object):
    def reverse(self, x):
        if x<0:fn=int('-'+str(x)[1:][::-1]) 
        else:fn=int(str(x)[::-1])
        return 0 if (fn<-2**31 or fn>2**31-1) else fn
        

        