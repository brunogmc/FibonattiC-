#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n1 , n2, th;
    cin >> n1 >> n2 >> th;

	int temp;

	for (int times = 0; times<th-2; times++){
		temp = n2;
		n2 = n1+ n2;
		n1 = temp;
	}

    printf("%i",n2);
	return 0;
}
