#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    queue<int> que;

    que.push(0);
    for (int i=0; i<numbers.size(); i++) {
        int lent = que.size();
        while (lent--) {
            int x = que.front();
            que.pop();
            que.push(x + numbers[i]);
            que.push(x - numbers[i]);
        }
    }
    int q_lenth = que.size();
    for (int i=0; i<q_lenth; i++) {
        int x = que.front();
        que.pop();
        if (x == target) {
            answer++;
        }
    }
    return answer;
}