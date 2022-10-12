#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
  string longestCommonPrefix(vector<string> &strs){
    if(strs.empty())
      return "";
    string prefix = strs[0];
    for (size_t i = 1; i < strs.size(); ++i){
      for (size_t j = 0; j < prefix.length(); ++j){
        if(prefix[j] != strs[i][j]){
          prefix.erase(prefix.begin()+j, prefix.end());
          break;
        }
      }
    }
    return prefix;
  }
};

int main(){
  Solution sl;
  vector<string> ss;
  ss.push_back("flower");
  ss.push_back("fly");
  ss.push_back("fling");
  cout << sl.longestCommonPrefix(ss) << endl;
}
