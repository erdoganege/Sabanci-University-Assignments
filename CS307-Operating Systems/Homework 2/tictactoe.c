#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <pthread.h>
#include <stdbool.h>
#include <time.h>

char **table;
int size;

struct lock{
char ch;
int turn;
};

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;

int game_finished()
{
	bool row_check; 
	bool column_check; 
	bool diagonal_check; 
	bool diagonal2_check; 
	for(int i=0; i < size; i++)
	{
	  row_check = true;
	  for(int k=0; k < size; k++)
	  {
	  	if(table[i][0] != table[i][k])
	  	{
	  	    row_check = false;
	  	    break;
	  	}	 
	  }
	  
	  if(row_check == true)
	  {
	     if(table[i][0] == 'X')
	     {
		return 1; //X wins
	     }
	     if(table[i][0] == 'O')
	     {
		return 2; //O wins
	     }
	     
	  }	
	}
	for(int i=0; i < size; i++)
	{
	  column_check = true;
	  for(int k=0; k < size; k++)
	  { 
	  /*
	        fputs("\n", stdout);
	        printf("%c", table[0][i]);
	        printf("%c", table[k][i]);
	        fputs("\n", stdout);
	       */
	  	if(table[0][i] != table[k][i])
	  	{
	  	    column_check = false;
	  	    break;
	  	}	 
	  }
	  if(column_check == true)
	  {
	     if(table[0][i] == 'X')
	     {
		return 1; //X wins
	     }
	     if(table[0][i] == 'O')
	     {
		return 2; //O wins
	     }
	  }		 
	}


	diagonal_check = true;
	for(int k=1; k < size; k++)
	{
		if(table[0][0] != table[k][k])
		{
	    		diagonal_check = false;
	    		break;
		}	 
	}
	if(diagonal_check == true)
	{
		if(table[0][0] == 'X')
		{
		return 1; //X wins
		}
		if(table[0][0] == 'O')
		{
		return 2; //O wins
		}
	}		 

	diagonal2_check = true;
	for(int k=1; k < size; k++)
	{
		if(table[0][size-1] != table[k][size-1-k])
		{
	    		diagonal2_check = false;
	    		break;
		}	 
	}
	if(diagonal2_check == true)
	{
		if(table[0][size-1] == 'X')
		{
			return 1; //X wins
		}
		if(table[0][size-1] == 'O')
		{
			return 2; //O wins
		}
	}
    for(int i = 0; i < size; i++)
    {
    	for(int j = 0; j < size; j++)
    	{
    		if(table[i][j] == ' '){
    		 	return 4;
    		}
    	}
    }

    return 0;
	
}



void print_table()
{
for (int i = 0; i < size; i++) 
{
    for (int j = 0; j < size; j++) 
    {
    	 printf("%c", '[');
         printf("%c", table[i][j]);
         printf("%c", ']');
    }
    fputs("\n", stdout);
  }	   
}

void initialize_table()
{
    table =(char **)malloc(sizeof(int*)*size);
    for (int i=0;i<size;i++)
    {
     table[i]=(char *)malloc(sizeof(int)*size);
    }            
    for(int i = 0; i < size; i++)
    {
    	for(int j = 0; j < size; j++)
    	{
    		table[i][j] = ' ';
    	}
    }    
}


bool end = false;
int turned = 0;
void* playing(void *arg)
{
  struct lock *temp = (struct lock *) arg;
  while(true)
  {
  bool deneme = true;
  	while(turned != temp->turn){
  		if(end == true)
  			break;
  	}
  	
 	pthread_mutex_lock(&mutex);
	    if(end == true){
	    	break;
	    }
	    
		    char ch = temp->ch;    
	    	    //printf("%c", ch);
		    //printf(" starting:");
		    //fputs("\n", stdout);
		    int r = rand() % size;
		    int k = rand() % size;
		    while(table[r][k] != ' ')
		    {
		    	r = rand() % size;
		    	k = rand() % size;
		    }
		    
		    table[r][k] = ch;
		    if(ch == 'X'){
		        printf("Player x played on (%d,%d)",r,k);
		    	turned = 1;
		    }
		    if(ch == 'O'){
		   	printf("Player o played on (%d,%d)",r,k);
		    	turned = 0;
		    }
		    //print_table();
		    //fputs("\n", stdout);
		    
		    int x = game_finished();
		    fputs("\n", stdout); 
		    if(game_finished() == 1){
		    printf("Game end\n");
		    printf("Winner is X");
		    fputs("\n", stdout);
		    print_table();
		    end = true;
		    break;
		    }
		    if(game_finished() == 2){
		    printf("Game end\n");
		    printf("Winner is O");
		    fputs("\n", stdout);
		    print_table();
		    end = true;
		    break;
		    }
		    if(game_finished() == 0){
		    printf("Game end\n");
		    printf("It is a tie");
		    fputs("\n", stdout);
		    print_table();
		    end = true;
		    break;
		    }
		    pthread_mutex_unlock(&mutex);    	
		    
	}

	    pthread_mutex_unlock(&mutex);
}


int main(int argc, char **argv)
{
    srand(time(NULL)); 
    pthread_t player1;
    pthread_t player2;

    size = atoi(argv[1]); 	
    initialize_table();
    struct lock p1;
    p1.ch = 'X';
    p1.turn = 0;
    
    struct lock p2;
    p2.ch = 'O';
    p2.turn = 1;
    
    printf("Board Size: %dx%d", size, size);
    fputs("\n", stdout); 
    
    pthread_create(&player1, NULL, &playing, (void *)&p1);
    
    while(turned == 0);
    pthread_create(&player1, NULL, &playing, (void *)&p2);

  
   pthread_join(player1, NULL); 
   pthread_join(player2, NULL);
 
	  
	
    return 0;
}




