#include <stdio.h>

int main(void)
{
  int i;
  for(i = 1; i < 6; i++) {
    if(i%2 == 0) {
      printf("signed jump = %d\n", i);
    } else {
      printf("signed jump = %d\n", -i);
    }
  }
  printf("hello world\n");
  return 0;
}
