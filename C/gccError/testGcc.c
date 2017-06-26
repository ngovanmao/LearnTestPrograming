#include <stdio.h>
#define  SIZE 20
double mult(double z[], int n)
{
	int i, j;
	i = 0;
	for (j=0; j < n; j++) {
		//i = i + j + 1;
		i + j + 1;
		z[i] = z[i] * (z[0] +1.0);
	}
	return z[n];
}
int main() {
	double z[] = {1.0, 2.3, 4.5};
	printf("hello world\n");
	printf("mult = %f\n", mult(z, 3));
	return 0;
}
