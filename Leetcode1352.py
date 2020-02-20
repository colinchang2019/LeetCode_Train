class ProductOfNumbers:

    def __init__(self):
        self.lis = [1]
        self.product = [1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.lis = [1]
        else:
            self.lis.append(self.lis[-1]*num)
        
    def getProduct(self, k: int) -> int:
        if k>=len(self.lis):
            return 0
        return self.lis[-1]//self.lis[-k-1]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
