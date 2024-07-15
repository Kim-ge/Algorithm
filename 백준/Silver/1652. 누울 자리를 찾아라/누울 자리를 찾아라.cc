#include<iostream>
#include<string>
using namespace std;

int main(){
	char space[100][100];
	int N;
	int row = 0,col=0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> space[i];
	}
	for (int i = 0; i < N; i++) {
		int num = 0;
		for (int k = 0; k < N; k++) {
			if (space[i][k] == '.') {
				num++;
			}
			else {
				if (num > 1) {
					row++;
				}
				num = 0;
			}
		}
		if (num > 1) {
			row++;
		}
	}
	for (int i = 0; i < N; i++) {
		int num = 0;
		for (int k = 0; k < N; k++) {
			if (space[k][i] == '.') {
				num++;
			}
			else {
				if (num > 1) {
					col++;
				}
				num = 0;
			}
		}
		if (num > 1) {
			col++;
		}
	}
	cout << row << endl;
	cout << col;

	return 0;

}