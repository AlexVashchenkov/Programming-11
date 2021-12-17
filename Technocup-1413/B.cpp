#include <iostream>
#include <string>
#include <vector>
#include <map>
 
using namespace std;
 
vector<int> read_line(int len){
        vector<int> line;
        for (int i = 0; i < len; i++) {
            int val;
            cin >> val;
            line.push_back (val);
        }
        return line;
}
 
int main() {
    int tests;
    cin >> tests;
    for (int t = 0; t < tests; t++) {
        int m,n;
        cin >> n >> m;
        map<int, vector<int>> key;
        for (int l = 0; l < n; l++) {
            vector<int> x = read_line(m);
            key[x[0]] = x;
 
        }
 
        for (int c = 0; c < m; c++) {
            vector<int> x = read_line(n);
            if (key.find(x[0]) != key.end()) {
                for (auto k = x.begin(); k != x.end(); k++) {
                vector<int> row = key[*k];
                for (auto x = row.begin(); x != row.end(); x++) {
                    cout << *x << "\n";
                }
                cout << "\n";    
                }
            }
        }
    }
}
