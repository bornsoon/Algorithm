class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = []
        while(nums1 or nums2):
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    answer.append(nums1[0])
                    nums1.remove(nums1[0])
                else:
                    answer.append(nums2[0])
                    nums2.remove(nums2[0])
            elif nums1:
                answer.extend(nums1)
                nums1.clear()
            elif nums2:
                answer.extend(nums2)
                nums2.clear()
        if len(answer) == 0:
            return 0
        elif len(answer) % 2 == 0:
            return (answer[len(answer)//2 - 1] + answer[len(answer)//2]) / 2
        elif len(answer) % 2 == 1:
            return answer[len(answer)//2]