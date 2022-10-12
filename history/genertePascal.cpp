#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle(numRows);

        for(int i = 0; i < numRows; i++){
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; j++){
                row[j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
            triangle[i]= row;
        }
    return triangle;
    }
};

int main(){
    Solution sl;

    sl.generate(5);

    return 0;
}
