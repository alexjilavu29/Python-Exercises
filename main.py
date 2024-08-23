def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    maux = m
    ok = nums1[i]
    while i < (m + n) and j < n:
        if nums1[i] == 0 and (ok > 0 or maux == 0):
            nums1[i] = nums2[j]
            i += 1
            j += 1
        elif nums1[i] >= nums2[j]:
            for k in range(m + n - 1, i, -1):
                nums1[k] = nums1[k - 1]
            if nums1[i] != nums2[j]:
                nums1[i] = nums2[j]
                maux += 1
            else:
                i += 1
            ok = nums1[i]
            j += 1

        else:
            ok = nums1[i]
            i += 1
            maux -= 1
    return nums1

nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 1
nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
n = 90
print(merge(nums1, m, nums2, n))

