class Solution {
public:
    int minimum;
    int res;

    int threeSumClosest(vector<int>& nums, int target) {
        res = accumulate(nums.begin(), nums.begin() + 3, 0);
	    minimum = fabs(target - res);
	    Solution().RecSubset(vector<int>(), nums, target);
	    return res;
    }
	
    void RecSubset(vector<int> SoFar, vector<int> rest, int target){
	    if (rest.empty()){
		    if (SoFar.size() == 3){
			    int temp = accumulate(SoFar.begin(), SoFar.begin() + 3, 0);
			    if(fabs(target - temp) < minimum){
				    res = temp;
				    minimum = target - res;
			    }				
		    }
	    }
	    else {
		    SoFar.push_back(rest[0]);
		    Solution().RecSubset(SoFar, vector<int>(rest.begin() + 1, rest.end()), target);
		    SoFar.pop_back();
		    Solution().RecSubset(SoFar, vector<int>(rest.begin() + 1, rest.end()), target);
	    }
    }
};
