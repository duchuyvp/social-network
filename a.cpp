#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long l, r, a, k;
    cin >> l >> r >> a >> k;

    long long g = __gcd(a, k);
    a /= g;
    k /= g;
    
    long long ans = floorl(1.0 * r / k) - ceill(1.0 * l / k) + 1;
    cout << ans << endl;

}
