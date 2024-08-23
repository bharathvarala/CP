#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        vector<int> x(n);
        vector<int> ans;
        map<int, vector<int>> d;
        
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            x[i] = a[i] % k;
            if (x[i] == 0) {
                ans.push_back(i + 1);
            } else {
                d[x[i]].push_back(i + 1);
            }
        }
        
        vector<pair<int, vector<int>>> y;
        for (auto &p : d) {
            y.push_back(p);
        }
        
        sort(y.rbegin(), y.rend());
        
        for (auto &p : y) {
            for (int idx : p.second) {
                ans.push_back(idx);
            }
        }
        
        for (int i : ans) {
            cout << i << " ";
        }
        cout << endl;
    }
    
    return 0;
}

// python equivalent also resulted in tle 
// # heap solution gives tle
// # import heapq as h 
 
// # t=int(input())
// # while t:
// #     n,k=map(int,input().split())
// #     a=list(map(int,input().split()))
// #     pq = []
// #     for i in range(len(a)):
// #         h.heappush(pq,(-a[i],i+1))
// #     ans=[]
// #     while pq:
// #         x=h.heappop(pq)
// #         x=list(x)
// #         x[0]+=k 
// #         if x[0]>=0:
// #             ans.append(x[1])
// #         else:
// #             h.heappush(pq,tuple(x))
// #     print(*ans)
// #     t-=1