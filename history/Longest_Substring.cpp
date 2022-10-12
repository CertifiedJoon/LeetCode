class Solution {
public:
    int lengthOfLongestSubstring(string s) {  //fast but big memory usage
        int maximum = 0, next = 1;
        string strip= "";
        for (char const &c: s){
            if(strip.find(c) != -1){
                strip = strip.substr(strip.find(c)+next);
            }
            strip += c;
            if (strip.length() > maximum){
                maximum = strip.length();
            }
        }
        return maximum;
    }
    int lengthOfLongestSubstring2(string s) { //slow but good memory usage

        map<char, int> charMap;
        int start = -1;
        int maxLen = 0;

        for (int i = 0; i < s.size(); i++) {
            if (charMap.count(s[i]) != 0) {
                start = max(start, charMap[s[i]]);
            }
            charMap[s[i]] = i;
            maxLen = max(maxLen, i-start);
        }

        return maxLen;
    }
};
