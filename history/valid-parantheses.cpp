#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  bool match(char left, char right){
    if (left == '(' && right == ')') return true;
    else if (left == '[' && right == ']') return true;
    else if (left == '{' && right == '}') return true;
    else return false;
  }

  bool isValid(string s){
    stack<char> parantheses;
    if (s.length() % 2 != 0)
      return false;
    for (auto c : s){
      if (parantheses.empty())
        parantheses.push(c);
      else if (match(parantheses.top(),c))
        parantheses.pop();
      else
        parantheses.push(c);
    }
    return parantheses.empty();
  }
};
