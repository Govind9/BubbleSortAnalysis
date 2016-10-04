#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

#define LEN 6

string s;
vector <string> combo;

bool finefind(string x, char c)
{
	for (int i = 0; i < x.length(); i++)
	{
		if (x[i] == c)
			return true;
	}
	return false;
}

void print_combo()
{
	for (int i = 0; i < combo.size(); i++)
	{
		cout << combo[i] << endl;
	}
}

void permute(string x)
{
	if (x.length() == LEN)
	{
		string p = "";
		for (int i = 0; i < LEN; i++)
		{
			int n = int(x[i]) - '0';
			p = p + s[n];
		}
		combo.push_back(p);
	}

	for (int i = 0; i < LEN; i++)
	{
		if (!finefind(x, s[i]))
		{
			permute(x + s[i]);
		}
	}
}

int Bubble(string x)
{
	int moves = 0;

	for (int j = 0; j < LEN; j++)
	{
		moves = moves + 1;
		for (int i = 0; i < LEN -1 - j; i++)
		{
			moves = moves + 2;
			if (x[i] > x[i + 1])
			{
				char temp = x[i];
				x[i] = x[i + 1];
				x[i + 1] = temp;
			}
		}
	}

	return moves;
}

int Better(string x)
{
	int moves = 0;
	bool flag;

	for (int j = 0; j < LEN; j++)
	{
		moves = moves + 3;
		flag = false;
		for (int i = 0; i < LEN -1 - j; i++)
		{
			moves = moves + 2;
			if (x[i] > x[i + 1])
			{
				moves = moves + 2;
				flag = true;
				char temp = x[i];
				x[i] = x[i + 1];
				x[i + 1] = temp;
			}
		}
		if (!flag)
			break;
	}

	return moves;
}

int Qsort(string x)
{
	int moves = 0;
	int swap = 0;

	for (int j = 0; j < LEN; j++)
	{
		moves = moves + 3;
		swap = 0;
		for (int i = 0; i < LEN -1 - j; i++)
		{
			moves = moves + 2;
			if (x[i] > x[i + 1])
			{
				moves = moves + 2;
				swap = swap + 1;
				char temp = x[i];
				x[i] = x[i + 1];
				x[i + 1] = temp;
			}
		}

		if (swap < 2)
			break;
	}

	return moves;
}

void analyze()
{
	int Q = 0;
	int B = 0;
	int BB = 0;

	for (int i = 0; i < combo.size(); i++)
	{
		Q += Qsort(combo[i]);
		B += Bubble(combo[i]);
		BB += Better(combo[i]);
	}

	cout << "Qsort: " << Q << endl;
	cout << "Bubble: " << B << endl;
	cout << "Better: " << BB << endl;
}

int main()
{
	s = "123456";
	
	permute("");
	
	analyze();

	return 0;
}
