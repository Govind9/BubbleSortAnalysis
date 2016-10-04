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

int main()
{
	s = "123456";
	permute("");
	print_combo();
	return 0;
}
