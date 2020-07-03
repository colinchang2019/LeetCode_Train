class Solution:
    def numberToWords(self, num: int) -> str:
        a = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        b = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        if num<20:
            return a[num]
        if num<100:
            if num%10!=0:
                return b[num//10] + " " + a[num%10]
            else:
                return b[num//10]
        if num<1000:
            if num%100!=0:
                return  a[num//100] + " Hundred " + self.numberToWords(num%100)
            else:
                return a[num//100] + " Hundred"
        c1,num = num//1000000000,num%1000000000
        c2,num = num//1000000,num%1000000
        c3,c4 = num//1000,num%1000
        r1 = self.numberToWords(c1) + " Billion " if c1>0 else ""
        r2 = self.numberToWords(c2) + " Million " if c2>0 else ""
        r3 = self.numberToWords(c3) + " Thousand " if c3>0 else ""
        r4 = self.numberToWords(c4) if c4>0 else ""
        return (r1 + r2 + r3 + r4).strip()
