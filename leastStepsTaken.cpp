#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  int leastStepsTaken(int start, int end){
    int step = 2, fibo = 1, prev = 1;
    int d = end - start;
    if (d == 1) return 1;
    else {
      while (d != 0){
        int _ = prev;
        prev = fibo;
        fibo = fibo + _;
        for (int i = 0; i < fibo; ++i){
          step++;
          for (int j = 0; j < fibo; ++j){
            d--;
            if (d == 0) break;
          }
          if (d == 0) break;
        }
      }
    }
    return step;
  }
};

int main(){
  Solution sl;
  cout << sl.leastStepsTaken(1,22) << endl;
}
