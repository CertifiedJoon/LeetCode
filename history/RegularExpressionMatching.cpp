#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        if (s.empty() && p.empty()) return true;
        else if (!s.empty() && p.empty()) return false;

        if (!s.empty() && isalpha(s.back()) && isalpha(p.back()) && s.back() == p.back()){
            s.pop_back();
            p.pop_back();
        }

        else if (p.back() == '*'){
            p.pop_back();

            if (s.empty())
                p.pop_back();

            else if (!p.empty() && p.back() == '.'){
                p.pop_back();
                if (p.empty()){
                    while(!s.empty())
                        s.pop_back();
                }
                while (!s.empty() && !p.empty() && s.back() != p.back())
                    s.pop_back();
            }

            else if (!s.empty() && !p.empty() && isalpha(p.back())){
                if (s.find(p.back()) == -1)
                    p.pop_back();

                else {
                    while (!s.empty() && !p.empty() && s.back() == p.back())
                        s.pop_back();
                    p.pop_back();
                }
            }
        }

        else if(!s.empty() && p.back() == '.'){
            s.pop_back();
            p.pop_back();
        }

        else
            return false;

        return isMatch(s, p);

    }
};

int main(){
    Solution sl;
    cout << sl.isMatch("mississippi", "mis*is*p*.");
}
