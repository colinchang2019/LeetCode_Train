class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<1:
            return -1
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                if nums[mid]<nums[left]: #左无序
                    right = mid - 1
                elif nums[mid]>nums[right]: # 右无序
                    if nums[left]<=target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else: # 都有序
                    right = mid - 1
            elif nums[mid]<target:
                if nums[mid]>nums[right]: #右无序
                    left = mid + 1
                elif nums[mid]<nums[left]: # 左无序
                    if nums[right]>=target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else: # 都有序
                    left = mid + 1
            else:
                return mid
        return -1
