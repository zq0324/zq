
class Fid:
    def __init__(self,n):
        self.prev = 0
        self.cur = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur +=  self.prev
            self.prev = value
            self.n -= 1
            return value
        else:
            raise StopIteration()


f = Fid(10)
#print([i for i in f])


def fun(n):
    prev,cur = 0, 1
    while n > 0:
        n -= 1
        yield cur
        prev ,cur = cur, cur+prev

     
for i in fun(10):
    print(i,end = ' ')   
#print(i for i in fun(10))




