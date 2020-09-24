#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  int findUnsortedSubarray(vector<int> & nums){
    int i,j, left, right, min, max, middle;
    i = j = left = right = middle = nums.size()/2;
    min = max = nums[n];
    while(i >= 0 || j <nums.size())
    for (int i = n; i >= 0; --i){
      cout << nums[i] << min << endl;
      if (nums[i] <= min){
        min = nums[i];
      }
      else {
        left = i;
      }
    }
    for (int i = n; i < nums.size(); ++i){
      if (nums[i] >= max){
        max = nums[i];
      }
      else{
        right = i;
      }
    }
    return right - left + 1;
  }
};

int main(){
  Solution sl;
  int myints[] = {2,6,4,8,10,9,15};
  vector<int> nums (myints, myints + sizeof(myints)/sizeof(myints[0]));

  cout << sl.findUnsortedSubarray(nums) << endl;
}
