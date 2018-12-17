#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	char* s00 = "1234567890";
	printf(" s00 - > %d \r\n", atoi(s00));

	if (NULL)
	{	
		printf("NULL is true \r\n");
	}
	else
	{
		printf("NULL is false \r\n ");
	}

	time_t rawtime;
	struct tm * timeinfo;
	time ( &rawtime );
	timeinfo = localtime ( &rawtime );	
	printf ( "%d/%d/%d %d:%d:%d\n",timeinfo->tm_year+1900, timeinfo->tm_mon, timeinfo->tm_mday,timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);//Êä³ö½á¹û
	
	if (strcmp("2015-0-03", "2015-08-02") > 0)
	{
		printf("large \r\n");	
	}
	else
	{
		printf("small \r\n");		
	}

	return 1;
}
