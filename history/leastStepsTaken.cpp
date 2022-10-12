#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  int leastStepsTaken(int start, int end){
    for(int i = 0; i < c; ++i){
      int count = 1;
      int step = 0;
      end++;
      int d = end - start;

      while (d != 0){
        for (int i = 0; i < 2; ++i){
          //cout << step << " " << count << " " << d << endl;
          step++;
          if (d - count <= 0){
            d = 0;
            break;
          }
          else d -= count;
        }
        count++;
      }
    }
  return step;
  }
};

int main(){
  Solution sl;
  int c; cin >> c;
  for(;c > 0; --c){
    int start, end;
    cin >> start >> end;
    cout << sl.leastStepsTaken(start, end) << endl;
  }
}
