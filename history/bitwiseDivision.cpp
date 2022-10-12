#include <bits/stdc++.h>
using namespace std;

int divide(int dividend, int divisor) {
  if(dividend==Integer.MIN_VALUE){
    if(divisor==-1) return Integer.MAX_VALUE;
    else if(divisor==1)  return dividend;
    else return ((divisor&1)==1)?divide(dividend+1,divisor):divide(dividend>>1,divisor>>1);
  }
  if(divisor==Integer.MIN_VALUE) return 0;
  int sign = ((dividend > 0) == (divisor > 0));
  dividend = abs(dividend), divisor = abs(divisor);
  int result = 0, i;
  while (dividend - divisor >= 0) {
      for (i = 0; dividend - (divisor << i << 1) >= 0; i++);
      result += 1 << i;
      dividend -= divisor << i;
  }
  return sign ? result : -result;
}

int main(){
  cout << divide(8,2) << endl;
}
