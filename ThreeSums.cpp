#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>
using namespace std;


vector<vector<int>> v;
void RecSubset(vector<int>, vector<int>);
bool yes(vector<int>);

vector<vector<int>> threeSum(vector<int>& nums) {
	RecSubset(vector<int>(), nums);
	
	
	return v;
}
	
void RecSubset(vector<int> SoFar, vector<int> rest){

	if (rest.empty()){
		if (yes(SoFar)) v.push_back(SoFar);
	}
	else {
		SoFar.push_back(rest[0]);
		RecSubset(SoFar, vector<int>(rest.begin() + 1, rest.end()));
		SoFar.pop_back();
		RecSubset(SoFar, vector<int>(rest.begin() + 1, rest.end()));

	}
	return;
}
	
bool yes(vector<int> candidate){
	return (candidate.size() == 3 && accumulate(candidate.begin(), candidate.end(), 0) == 0 && find(v.begin(), v.end(), candidate) == v.end());
}


int main(){
	vector<int> nums{-1,0,1,2,-1,-4};
	vector<vector<int>> vec = threeSum(nums);
	
	for (auto &j : vec){
		for (auto &i : j){
			cout << i << " ";
		}
		cout << endl;
	}
}
