class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int lo = 0;
        int hi = nums.size() - 1;
        k = nums.size() - k;
        while (lo < hi){
            int j = partition(nums, lo, hi);
            if (k > j)
                lo = j + 1;
            else if (k < j)
                hi = j - 1;
            else
                return nums[k];
        }
        return nums[k];
}

private:
void swap(vector<int> &a, int i, int j){
    int z = a[i];
    a[i] = a[j];
    a[j] = z;
}

int partition(vector<int>& nums, int left, int right){
    int last = left;
    swap(nums, left, left + (right - left) / 2);

    for (int i = left; i <= right; i++)
        if (nums[i] < nums[left])
            swap(nums, ++last, i);

    swap(nums, last, left);
    return last;
}
};
