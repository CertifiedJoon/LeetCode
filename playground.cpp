#include <string>
#include <vector>
#include <iostream>

using namespace std;


bool check_valid(vector<bool> braces, int stack_size){  
  int curr_size = 0;

  for (bool b : braces){
    if (b) {
      if (--curr_size < 0) return false;
    } else {
      if (++curr_size > stack_size) return false;
    }
  }

  return true;
}


int main(int argc, char *argv[]){
  int length;
  cin >> length;
  
  vector<bool> braces;
  braces.push_back(true);

  for (int i = 0; i < length; i++){
    char bracket;
    cin >> bracket;
    braces.push_back((bracket == '(' ? false : true));
  }
  braces.pop_back();

  int stack_size;
  cin >> stack_size;

  int counter = 0;

  for (int i = 1; i < length; i++) {
    bool temp = braces[i];
    braces[i] = braces[i-1];
    braces[i - 1] = temp;

    if (check_valid(braces, stack_size))
      counter++;
  }

  cout << counter << endl;

  return 0;
}