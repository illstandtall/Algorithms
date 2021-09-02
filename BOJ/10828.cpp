#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
	string s;
	stack<int> sk;
	int n;
	cin >> n;

	while (n--)
	{
		cin >> s;
		if (s == "push")
		{
			int tmp;
			cin >> tmp;
			sk.push(tmp);
		}
		else if(s == "top")
		{
			if (sk.empty() == 0)
			{
				cout << sk.top() << endl;
			}
			else
			{
				cout << -1 << endl;
			}
		}
		else if (s == "size")
		{
			cout << sk.size() << endl;
		}
		else if (s == "empty")
		{
			cout << sk.empty() << endl;
		}
		else if (s == "pop")
		{
			if (sk.empty() ==0)
			{
				cout << sk.top() << endl;
				sk.pop();
			}
			else
			{
				cout << -1 << endl;
			}
		}
	}
	return 0;
}