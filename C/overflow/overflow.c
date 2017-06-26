#include <stdio.h>
typedef unsigned short uint16_t;
void main()
{
	printf("Hello world\n");
	unsigned long long l = 65534;
    uint16_t u16 = 0;
	u16 = l;
	printf("first l = %lld\n", l);
	printf("first u16 = %d\n", u16);
	l = 65539;
	u16 = l;
	printf("second l = %lld\n", l);
	printf("second  u16 = %d\n", u16);
	l = 1565539;
	u16 = l;
	printf("third l = %lld\n", l);
	printf("third  u16 = %d\n", u16);
	u16 =65535;
	printf("last u16 = %d\n", u16);
	u16 += 1;
	printf("reset u16 = %d\n", u16);


}
