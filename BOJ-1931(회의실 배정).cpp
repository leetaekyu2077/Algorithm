#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int *a, int *b)
{
	if (a[1] == b[1])
		return a[0] < b[0];
	return (a[1] < b[1]);
}

int main()
{
	int N, **meeting, count, finish;

	cin >> N;
	meeting = new int*[N];

	for (int i = 0; i < N; i++) {
		meeting[i] = new int[2];
		cin >> meeting[i][0] >> meeting[i][1];
	}

	sort(meeting, meeting+N, compare);

	count = 1;
	finish = meeting[0][1];
	for (int i = 1; i < N; i++) {
		if (meeting[i][0] >= finish) {
			count++;
			finish = meeting[i][1];
		}
	}
	cout << count;
}