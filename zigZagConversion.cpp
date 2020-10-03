#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  string convert(string s, int numRows){
    string output = "";
    int n = s.size();

    vector<int> spacing;
    for (int i = numRows-1; i >= 1 ; --i)
      spacing.push_back(i*2);
    spacing.push_back((numRows-1) * 2);

    for (int i = 0; i < numRows; ++i){
      int jump = i;
      for (int j = 0; jump < n; ++j){
        output.push_back(s[jump]);
        jump += (j % 2 == 0) ? spacing[i] : spacing[numRows-(i+1)];
      }
    }
  return output;
  }
};

int main(){
  Solution sl;
  cout << sl.convert("HOGWARTSLEGACY", 5) << endl;
}
