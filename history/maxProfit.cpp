#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int kadaneSum = 0, maxp = 0;
        for (int i = 1; i < prices.size(); i++){
            kadaneSum = max(0, kadaneSum += (prices[i] - prices[i-1]));
            maxp = max (kadaneSum, maxp);
        }

        return maxp;
    }
};

int main(){
    Solution sl;
    vector<int> v = {7,1,5,3,6,4};
    cout << sl.maxProfit(v);
}
