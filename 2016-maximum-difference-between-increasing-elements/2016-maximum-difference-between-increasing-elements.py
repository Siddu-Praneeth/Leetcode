class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        k=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    m=nums[j]-nums[i]
                    k.append(m)
        if len(k)>0:
            return max(k)
        else:
            return -1
        # m=min(nums)
        # mi=0
        # for i in range(n):
        #     if m==nums[i]:
        #         mi=i
        # p=nums[mi:]
        # ml=len(p)
        # for i in range(ml):
        #     diff=p[i]-m   
        #     k.append(diff)
        # if ml>1:
        #     return max(k)
        # else:
        #     return -1