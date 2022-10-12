class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> res (m + n);

        int i = 0, j = 0;
        for (int k = 0; k < m + n; k++){
            if(i >= m)
                res[k] = nums2[j++];
            else if (j >= n)
                res[k] = nums1[i++];
            else if(nums1[i] < nums2[j])
                res[k] = nums1[i++];
            else
                res[k] = nums2[j++];
        }

        nums1 = res;
    }
};
