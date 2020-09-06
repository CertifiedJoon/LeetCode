#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;
class Solution{
public:
  int romanToInt(string s){
    unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    int sum = 0;
    int i = 0;
    while(i < s.size()){
      if (roman[s[i]] < roman[s[i+1]])
        sum -= roman[s[i]];
      else
        sum += roman[s[i]];
      i++;
    }
    return sum;
  }
};
int main(){
  Solution sl;
  cout << (sl.romanToInt("MCMXCIV")) << endl;
};
