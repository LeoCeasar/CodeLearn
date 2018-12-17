/*测试for循环和if相关判断进行的时间快慢问题
 * */

#include <iostream>
#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
#include <unistd.h>

#define TIME_NUM 1000
struct timeval t1,t2;

void ForTime()
{
	int i = 0;
	gettimeofday(&t1, NULL);
	for (; i < TIME_NUM; i++){}
	gettimeofday(&t2, NULL);
	printf("ForTime:%ld\n", t2.tv_sec - t1.tv_sec);
}

void IfTime()
{
	int i = 0;
	gettimeofday(&t1, NULL);
	for (; i < TIME_NUM/2; i++){}
	
	if (i = TIME_NUM/2) i++;

	for (; i < TIME_NUM; i++){}
	gettimeofday(&t2, NULL);
	printf("IfTime:%ld\n", t2.tv_sec - t1.tv_sec);
}

int main()
{

	/*
	 * time_t timep;
	time (&timep);
	print("%s",asctime(gmtime(&timep)));
	*/
	ForTime();
	IfTime();
	return 1;
}
