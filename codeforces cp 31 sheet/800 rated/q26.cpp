#include <iostream>
#include <vector>
#include <numeric> 
#include <algorithm>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int& x : a) cin >> x;
        bool c = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && (__gcd(a[i], a[j]) == 1 || __gcd(a[i], a[j]) == 2)) {
                    c = true;
                    break;
                }
            }
            if (c) break;
        }
        if (c) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}