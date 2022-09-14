class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a1 = 0
        a2 = 0
        for i in range (m + n):
            if(a1 != m and a2 != n):
                if(nums2[a2] <= nums1[a1]):
                    nums1.pop()
                    nums1.insert(a1 + a2,nums2[a2])
                    a2 = a2 + 1
                else:
                    a1 = a1 + 1
            if (a1 == m):
                while (a2 < n):
                    nums1.pop()
                    nums1.insert(a1 + a2, nums2[a2])
                    a2 = a2 + 1
        nums1.sort()
