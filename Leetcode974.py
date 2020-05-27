class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        re = [0 for _ in range(K)]
        re[0] = 1
        s,res = 0,0
        for i in range(len(A)):
            s += A[i]
            modulus = s%K
            res += re[modulus]
            re[modulus] += 1
        return res
/*
 判断子数组的和能否被 KK 整除就等价于判断 (P[j] - P[i-1]) \bmod K == 0(P[j]−P[i−1])modK==0，根据 同余定理，只要 P[j] \bmod K == P[i-1] \bmod KP[j]modK==P[i−1]modK，就可以保证上面的等式成立。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/he-ke-bei-k-zheng-chu-de-zi-shu-zu-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/
