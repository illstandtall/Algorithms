#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main()
{
    string s;
    queue<int> q;
    int n;
    cin >> n;

    while (n--)
    {
        cin >> s;
        if (s == "push")
        {
            int tmp;
            cin >> tmp;
            q.push(tmp);
        }
        else if (s == "pop")
        {
            if (q.empty() == 0)
            {
                cout << q.front() << endl;
                q.pop();
            }
            else
            {
                cout << -1 << endl;
            }
        }
        else if (s == "size")
        {
            cout << q.size() << endl;
        }
        else if (s == "empty")
        {
            cout << q.empty() << endl;
        }
        else if (s == "front")
        {
            if (q.empty() == 0)
            {
                cout << q.front() << endl;
            }
            else
            {
                cout << -1 << endl;
            }
        }
        else if (s == "back")
        {
            if (q.empty() == 0)
            {
                cout << q.back() << endl;
            }
            else
            {
                cout << -1 << endl;
            }
        }
    }
    return 0;
}