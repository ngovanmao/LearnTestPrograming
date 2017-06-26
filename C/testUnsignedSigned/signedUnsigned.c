#include <stdio.h>
typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
typedef          short  int16_t;
struct collect_view_data_msg {
  uint16_t len;
  uint16_t clock;
  uint16_t timesynch_time;
  uint16_t cpu;
  uint16_t lpm;
  uint16_t transmit;
  uint16_t listen;
  uint16_t parent;
  uint16_t parent_etx;
  uint16_t current_rtmetric;
  uint16_t num_neighbors;
  uint16_t beacon_interval;

  uint16_t sensors[10];
};

double convert(int t)
{
  return t;
}

uint16_t test1 = 65432;

#define A 5
#define B 10
#define C A + B
int toShort(int a)
{
	short sh = a >> 16;
	printf("sh = %d\n\n", sh);
}
int main(void)
{
  unsigned int plus_one = 1;
  int minus_one = -1;

  if(plus_one < minus_one)
    printf("1 < -1\n");
  else
    printf("boring");

  uint16_t uy= 65506;
  short y;
  uint16_t UMAX = -1;
  y = UMAX + 1 - uy;
  printf("uy(s)=%d, uy(u) = %u, uy(d) = %d, uy(ld)= %ld\n", (short)uy, uy, uy, (long)uy);
  toShort(uy);
  printf("UMAX = %u\n", UMAX);
  printf("y(u) = %u (d) = %d\n", y, y);

  int negY = -100;
  printf(" negY(d) =%d = negY(u)%u = negY(ld) = %ld\n", negY, negY, (long)negY);
  printf("convert negY = %u \n", negY + UMAX + 1);

  printf("===========================\n");
  printf("size of uint16_t = %d\n",sizeof(uint16_t));
  printf("size of int =%d\n", sizeof(int));
  printf("size of int16 (short) = %d\n", sizeof(short));
  printf("===========================\n");
  printf("convert(-100) = %lf\n", convert(-100));
  printf("===========================\n");
  printf("sizeof(struct collect_view_data_msg) / sizeof(uint16_t) = %d\n", sizeof(struct collect_view_data_msg) / sizeof(uint16_t));

  struct {
    uint8_t seqno;
    uint8_t for_alignment;
    struct collect_view_data_msg msg;
  } msg;

  printf("===========================\n");
  printf("sizeof(msg) / sizeof(uint16_t) = %d\n", sizeof(msg) / sizeof(uint16_t));
  printf("===========================\n");
  int16_t mao = -35;
  printf("int16_t(-35) = %d , uint8_t(-35) = %u\n", mao, (uint8_t)mao);
  uint8_t mao1 = 221;
  printf("int16_t(221) = %d\n", (int16_t)mao1);
  printf("A = %d, B= %d, C= %d", A, B, C);
  printf("unsigned number is 65432 = signed number = %d\n", (int16_t)test1);
return 0;
}


