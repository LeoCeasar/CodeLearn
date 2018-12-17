#include<iostream>
#include <stdio.h>
#include<unistd.h>
#include <sys/time.h>
using namespace std;

main()
{
	time_t timep;
	time (&timep);
	cout << asctime(gmtime(&timep));
	printf("%s",ctime(&timep));

	{
		int seconds= time((time_t*)NULL);
		printf("%d\n",seconds);
	}

	{
		struct timeval tv;
		struct timezone tz;
		gettimeofday (&tv , &tz);
		printf("tv_sec; %d\n", tv.tv_sec) ;
		printf("tv_usec; %d\n",tv.tv_usec);
		printf("tz_minuteswest; %d\n", tz.tz_minuteswest);
		printf("tz_dsttime, %d\n",tz.tz_dsttime);
	}

	{
		time_t timep;
		static tm *p;
		time(&timep);
		printf("time() : %d \n",timep);
		p=localtime(&timep);
		timep = mktime(p);
		printf("time()->localtime()->mktime():%d\n",timep);
	}
}

