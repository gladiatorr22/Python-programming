nums1=[1,3,8,3,6]
nums2=[22,11,88]
def alternatemerge(nums1, nums2):
    i, j, k = 0, 0, 0
    res = []
    len1=len(nums1)
    len2=len(nums2)
    while k< len1 + len2:
        if i < len1 and k%2==0:
            res.append(nums1[i])
            i += 1
            k+= 1
        elif j < len2 and k%2==1:
            res.append(nums2[j])
            j += 1
            k+= 1
        else:
            if i< len1 :
                
                res.append(nums1[i]) 
                i+=1
                k+=1
            else:
                res.append(nums2[j])
                j+=1
    return res
res=alternatemerge(nums1,nums2)
print(res)