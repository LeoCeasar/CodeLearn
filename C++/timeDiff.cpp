#include<iostream>
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

int main()
{
	struct timeval tv;
	gettimeofday(&tv,NULL);
	printf("second:%ld\n",tv.tv_sec);  //秒
	printf("millisecond:%ld\n",tv.tv_sec*1000 + tv.tv_usec/1000);  //毫秒
	printf("microsecond:%ld\n",tv.tv_sec*1000000 + tv.tv_usec);  //微秒


	sleep(3); // 为方便观看，让程序睡三秒后对比
	std::cout << "3s later:" << std::endl;


	gettimeofday(&tv,NULL);
	printf("second:%ld\n",tv.tv_sec);  //秒
	printf("millisecond:%ld\n",tv.tv_sec*1000 + tv.tv_usec/1000);  //毫秒
	printf("microsecond:%ld\n",tv.tv_sec*1000000 + tv.tv_usec);  //微秒	
	return 0;
}
