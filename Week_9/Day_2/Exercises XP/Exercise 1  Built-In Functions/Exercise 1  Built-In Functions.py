class m():
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        if self.num < 0:
            return (f"abs : ({(-1) * self.num})")
        elif self.num > 0 :
            return self.num
    def __int__(self):
        self.num = int(self.num * 10)
        return self.num
        
ab = m(-7.5)
print(abs(ab))
print(int(ab))
