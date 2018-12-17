#include <stdio.h>
#include <dlfcn.h>
#include <stdlib.h>
#include <string.h>

#define CONF_FILE_PATH  "Config.ini"    
#define MAX_PATH 240

int main(void)
{
    void *handle;
    char *pError;
    typedef char* (*pf_t)();

    handle = dlopen("libINI.so", RTLD_NOW);

    if(!handle)
    {
        fprintf (stderr, "%s\n", dlerror());
        exit(1);
    }
    
    dlerror();  
    
    pf_t pfGetCurrentPath = (pf_t)dlsym(handle,"GetCurrentPath");
    pf_t pfGetIniKeyInt = (pf_t)dlsym(handle,"GetIniKeyInt");
    pf_t pfGetIniKeyString = (pf_t)dlsym(handle,"GetIniKeyString");

    char g_szConfigPath[MAX_PATH];   
    char buf[MAX_PATH];   
    
    memset(buf,0,sizeof(buf));   
    pfGetCurrentPath(buf,CONF_FILE_PATH);   
    strcpy(g_szConfigPath,buf);   
    printf(g_szConfigPath);
   
    int iCatAge;   
    char szCatName[32];   
    memset(szCatName, 0, sizeof(szCatName));
       
    //iCatAge = (int)pfGetIniKeyInt("CAT","age","/home/test/C/readINI/Config.ini");   
    iCatAge = (int)pfGetIniKeyInt("CAT","age",g_szConfigPath);   
    strcpy(szCatName,(char*)pfGetIniKeyString("CAT","name",g_szConfigPath));   
    //strcpy(szCatName,(char*)pfGetIniKeyString("CAT","name","/home/test/C/readINI/Config.ini"));   
   
    printf("%s Cat is age %d yes old \r\n", szCatName, iCatAge);

    dlclose(handle); 
    return 0;   	
}
