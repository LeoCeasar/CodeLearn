// gcc -o badindex ./
/*
int main() {
	int a[7]= {0,1,2,3,4,5,6};
	a[7] = 20;
}
*/

#include <stdio.h>
int main() {
	int x = 10;
    int a[7]= {0,1,2,3,4,5,6};
    a[7] = 20;
	printf("%d", x);
}
