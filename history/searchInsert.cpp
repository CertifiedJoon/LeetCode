#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
  int searchInsert(vector<int> &nums, int target){
    return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
  }
};

int main(){
  Solution sl;
  int myints[] = {1,3,5,6};
  vector<int> test (myints, myints + sizeof(myints) / sizeof(int));
  cout << sl.searchInsert(test, 2) << endl;
}
