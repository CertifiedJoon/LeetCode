#include <bits/stdc++.h>
class Solution{
public:
  int rand10(){
      int fill, multiple, integers;
      fill = rand7();
      multiple = rand7();
      integers = fill + (multiple - 1)  * 10;
      return 1 + (integers - 1) % 10;
  }
};
