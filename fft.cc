// =====================================================================================
// 
//       Filename:  fft.cc
// 
//    Description:  Fast Fourier Transform
// 
//        Version:  1.0
//        Created:  2013年08月18日 11时33分58秒
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Boyang Yang (barty), maiL@barty.ws
//        Company:  http://barty.ws
// 
// =====================================================================================


#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <complex>
#define clr(x) memset(x, 0, sizeof(x))
using namespace std;

const double pi = acos(-1.);
typedef complex<double> comp;
const comp I = comp(0, 1);
const int L = 200000 + 9;
const double eps = 1e-6;

void dft(comp *y, int n, bool idft = false) {
    comp w, x;
    double root = 2 * pi / n;
    if (idft) root *= -1.;
    int i, j, k, m, h;
    for (m = n; h = m / 2, m >= 2; m = h, root *= 2) 
        for (i = 0; i < h; ++i)
            for (w = exp(i*root*I), j = i; j < n; j += m) 
                k = j + h, x = y[j] - y[k], y[j] += y[k], y[k] = w * x;
    for (i = 0, j = 1; j < n - 1; ++j) {
        for (k = n / 2; k > (i ^= k); k >>= 1);
        if (j < i) swap(y[j], y[i]);
    }
    if (idft) for (i = 0; i < n; ++i) y[i] /= n;
}

comp a[L], b[L], c[L];
int d[L];

int main (int argc, char *argv[]) {
    string sa, sb;
    while (cin >> sa >> sb) {
        clr(a), clr(b), clr(c), clr(d);
        for (int i = 0, l = sa.length(); i < l; ++i) a[i] = comp((double)(sa[l-i-1]-'0'), 0.);
        for (int i = 0, l = sb.length(); i < l; ++i) b[i] = comp((double)(sb[l-i-1]-'0'), 0.);
        int l, j;
        for (l = 1; l < (int)(sa.length() + sb.length()); l <<= 1);
        dft(a, l);
        dft(b, l);
        for (int i = 0; i < l; ++i) c[i] = a[i] * b[i];
        dft(c, l, true);
        for (int i = 0; i < l; ++i) {
            d[i] += (int)(round(c[i].real()) + eps);
            d[i + 1] += d[i] / 10;
            d[i] %= 10;
        }
        while (d[l]) {
            d[l + 1] = d[l] / 10;
            d[l++] %= 10;
        }
        j = l - 1;
        while (j > 0 && !d[j]) --j;
        while (j >= 0) printf("%d", d[j--]);
        printf("\n");
    }
    return 0;
}
