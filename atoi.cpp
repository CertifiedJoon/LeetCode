#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  int stringtoi(string s){
    int sign = 1, res = 0;
    char *t = new char [s.length()+1];
    strcpy (t, s.c_str());
    while (*t++ == " ")
      ;
    if(*t == "-"){
      sign = -1;
      s++;
    }

    while(isdigit(*t++)){
      if (INT_MIN / 10.0 < res && INT_MIN % 10 > ((*t) - '0') && sign < 0)
        return INT_MIN;
      else if (INT_MAX / 10.0 < res && INT_MAX % 10 > ((*t) - '0')) && sign > 0)
        return INT_MAX;
      res = res*10 + (*t - '0');
    }
    delete[] t;
    return res;
  }
};

int main(){
  Solution sl;
  cout << sl.stringtoi("    -2147483649")
}
