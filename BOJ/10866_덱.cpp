#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
	deque<int> deq;
	int n;
	cin >> n;

	while (n--) {
		string s;
		cin >> s;
		if (s == "push_front") {
			int parm;
			cin >> parm;
			deq.push_front(parm);
		}
		else if (s == "push_back") {
			int parm;
			cin >> parm;
			deq.push_back(parm);
		}
		else if (s == "pop_front") {
			if (deq.empty())
				cout << -1 << endl;
			else {
				cout << deq.front() << endl;
				deq.pop_front();
			}
		}
		else if (s == "pop_back") {
			if (deq.empty())
				cout << -1 << endl;
			else {
				cout << deq.back() << endl;
				deq.pop_back();
			}
		}
		else if (s == "size") {
			cout << deq.size() << endl;
		}
		else if (s == "empty") {
			if (deq.empty())
				cout << "1" << endl;
			else
				cout << "0" << endl;
		}
		else if (s == "front") {
			if (deq.empty())
				cout << "-1" << endl;
			else
				cout << deq.front() << endl;
		}
		else if (s == "back") {
			if (deq.empty())
				cout << "-1" << endl;
			else
				cout << deq.back() << endl;
		}
	}
	return 0;
}