#include <stdio.h>
#include <string.h> 
 int main(int argc,char *argv[])
 {
   char *strTest = "hello world";
   int strLen=strlen(strTest);
   int i=0;
   FILE *fp;
 if((fp=fopen(argv[1], "wb")) == NULL)
 {
		 printf("file open failed!");
 	return 0;
    }
  printf("%d\n",strLen);
  while(i<strLen)
    {
       fprintf(fp,"%02x",strTest[i++]);
    }
 return 1;
 }

