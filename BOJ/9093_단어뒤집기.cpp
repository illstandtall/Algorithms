#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	cin.ignore();
	while (t--)
	{
		string s, tmp;
		getline(cin, s);
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == ' ') {
				reverse(tmp.begin(), tmp.end());
				cout << tmp << " ";
				tmp.clear();
			}
			else {
				tmp += s[i];
			}
		}
		reverse(tmp.begin(), tmp.end());
		cout << tmp << "\n";
	}
	return 0;
}