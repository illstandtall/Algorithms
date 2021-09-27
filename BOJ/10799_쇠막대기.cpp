#include <iostream>
#include <stack>
using namespace std;

int main()
{
	int result = 0;
	bool flag = false;
	stack<char> st;
	string pipe;
	cin >> pipe;

	for (int i = 0; i < pipe.length(); i++)
	{
		if (pipe[i] == '(')
		{
			++result;
			st.push('(');
			flag = true;
		}
		else
		{
			if (flag)
			{
				st.pop();
				result = result - 1 + st.size();
			}
			else
			{
				st.pop();
			}
			flag = false;
		}
	}
	cout << result << '\n';

	return 0;
}