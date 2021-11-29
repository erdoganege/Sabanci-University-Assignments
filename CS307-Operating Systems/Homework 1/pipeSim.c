#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("I’m SHELL process, with (PID:%d) - My main command is: man rm | grep '^ *-v' -w -A 1 > output.txt \n", (int) getpid());
    int fd[2];
    pipe(fd);
    int rc = fork(); 
    if (rc < 0) // fork failed; exit
    { 
        fprintf(stderr, "fork failed\n");
        exit(1);
    }   
    else if(rc == 0) //child process = MAN
    {
    	printf("I’m MAN process, with (PID:%d) - My command is: rm \n", (int) getpid());
    	close(STDOUT_FILENO);
    	dup(fd[1]);   
    	close(fd[0]);
    	close(fd[1]);
        char *myargs[3];
        myargs[0] = strdup("man");   //command
        myargs[1] = strdup("rm"); 
        myargs[2] = NULL;           // marks end of array
        execvp(myargs[0], myargs);  
        printf("this shouldn't print out");	    	   	
    }
    else // go back to parent process (shell process)
    {	
 	int wc = wait(NULL);   	// wait until MAN process done	
    	int rc1 = fork();
	if (rc1 < 0) // fork failed; exit
	{ 
		fprintf(stderr, "fork failed\n");
		exit(1);
	}   
	else if(rc1 == 0)    //child process = GREP
	{	
	    	printf("I’m GREP process, with (PID:%d) - My command is: -v \n", (int) getpid());
	    	close(STDIN_FILENO); 
	    	dup(fd[0]);
	    	close(fd[0]);
	    	close(fd[1]);
	        close(STDOUT_FILENO);
	        open("./output.txt", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);	        
		char *myargs[5];
		myargs[0] = strdup("grep"); //command
		myargs[1] = strdup("^ *-v");	
		myargs[2] = strdup("-w");
		myargs[3] = strdup("-A 1");	
		myargs[4] = NULL;    
		execvp(myargs[0], myargs);  // runs word count
		printf("this shouldn't print out");    		   
	 }	
	 else
	 {	 	
	 	close(fd[0]);
	 	close(fd[1]);	 	
	 	int wc2 = wait(NULL);   // wait until GREP process done
	 	printf("I’m SHELL process, with (PID:%d) execution is completed, you can find the results in output.txt \n", (int) getpid());
	 }   		
    }
    
    
    
    
    

    return 0;
}
