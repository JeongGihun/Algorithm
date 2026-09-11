#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> v;
    stringstream ss(s);
    int num;
    while (ss>>num)
      v.push_back(num);
    
    int maxvalue = *max_element(v.begin(), v.end());
    int minvalue = *min_element(v.begin(), v.end());
        
    answer = to_string(minvalue) + " " + to_string(maxvalue);
    
    return answer;
}