#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/syscall.h>
#include <pthread.h>
#include <stdbool.h>
#include <time.h>
#include <semaphore.h>

pthread_mutex_t mutex_combination = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex_car_finding = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex_captain = PTHREAD_MUTEX_INITIALIZER;
pthread_barrier_t barrier;
sem_t semaphore;
pthread_cond_t condition;

int counterA = 0;
int counterB = 0;

struct lock{
	char ch;
	};
	


bool inputcheck(int A, int B)
{ 
    if((A%2 !=0) || (B %2 != 0)){
    
    	//printf("Not valid input!\n");
    	return false;
    }	
 	if((A + B) % 4 != 0){
 		//printf("Not valid input!\n");
 		return false;
 	}   
	return true;	
}
/*
int count = 0;
void hmm(pid_t tid){
	printf("Thread ID: %d and total thread count: %d\n", tid, count);
	count += 1;
}*/
int counter_of_people_looking_car = 0;
int game_turn = 0; // 0: looking for a car turn, 1: finding a car
bool check_combination = true;
int groupA = 0;
int groupB = 0;
bool captain = true;
int thread_counter = 0;
int thread_counter2 = 0;
bool flag_for_people = true;
bool group_formed = false;

void* playing(void *arg)
{
	struct lock *temp = (struct lock *) arg;
	
	sem_wait(&semaphore);
	while(game_turn != 0);
	//pid_t tid = syscall(SYS_gettid);
	printf("Thread ID: %ld, Team: %c, I am looking for a car \n", pthread_self(), temp->ch);
	counter_of_people_looking_car += 1;
	if(temp->ch == 'A') 
	{	
		counterA += 1;
	}
	else
	{
	    counterB += 1;
	}  
	if(  ((counterA != 4)  && (counterB != 4)) && !(counterA >= 2 && counterB >= 2)){
		//printf("Girdik\n");
		sem_post(&semaphore);
	}	
	else{
		pthread_cond_signal(&condition);			
		game_turn = 1;

	}
	
	
	
	//hmm(tid);
	//printf("CounterA: %d\n", counterA);
	//printf("CounterB: %d\n", counterB);
	
	while(game_turn != 1);

	
	pthread_mutex_lock(&mutex_car_finding);
	//printf("Buradayim, %d\n", tid);
	if((counterA == 4)){
		if(temp->ch == 'B' && counterB < 2){
			//printf("I am sleeping: %d\n", tid);
			thread_counter2 += 1;
			pthread_cond_wait(&condition, &mutex_car_finding);
				
			while((counterA == 4 && counterB ==1)){
			//printf("I am sleeping again: %d\n", tid);
			pthread_cond_wait(&condition, &mutex_car_finding);	
			}
		}		
		printf("Thread ID: %ld, Team: %c, I have found a spot in a car\n", pthread_self(), temp->ch);	
		thread_counter2 += 1;
		if(temp->ch == 'A') groupA += 1;
		else if(temp->ch == 'B') groupB += 1;	
	}
	else if((counterB == 4)){
		if(temp->ch == 'A' && counterA < 2){
			//printf("I am sleeping: %d\n", tid);
			thread_counter2 += 1;
			pthread_cond_wait(&condition, &mutex_car_finding);
			while((counterA ==1 && counterB ==4)){
			//printf("I am sleeping again: %d\n", tid);
			pthread_cond_wait(&condition, &mutex_car_finding);	
			}		
		}		
		printf("Thread ID: %ld, Team: %c, I have found a spot in a car\n", pthread_self(), temp->ch);	
		thread_counter2 += 1;	
		if(temp->ch == 'A') groupA += 1;
		else if(temp->ch == 'B') groupB += 1;	
	}
	else if((counterA == 2) && (counterB == 2)){
		printf("Thread ID: %ld, Team: %c, I have found a spot in a car\n", pthread_self(), temp->ch);	
		thread_counter2 += 1;	
		if(temp->ch == 'A') groupA += 1;
		else if(temp->ch == 'B') groupB += 1;		
	}
	else if((counterA == 3) && (counterB == 2)){
		if(groupA == 2 && temp->ch == 'A'){
			//printf("I am sleeping: %d\n", tid);
			thread_counter2 += 1;
			pthread_cond_wait(&condition, &mutex_car_finding);	
			while((counterA == 1 && counterB ==4)){
			//printf("I am sleeping again: %d\n", tid);
			pthread_cond_wait(&condition, &mutex_car_finding);	
			}
		}
		printf("Thread ID: %ld, Team: %c, I have found a spot in a car\n", pthread_self(), temp->ch);	
		thread_counter2 += 1;	
		if(temp->ch == 'A') groupA += 1;
		else if(temp->ch == 'B') groupB += 1;		
	}	
	else if((counterA == 2) && (counterB == 3)){
		if(groupB == 2 && temp->ch == 'B'){
			//printf("I am sleeping: %d\n", tid);
			thread_counter2 += 1;
			pthread_cond_wait(&condition, &mutex_car_finding);	
			while((counterA == 4 && counterB ==1)){
			//printf("I am sleeping again: %d\n", tid);
			pthread_cond_wait(&condition, &mutex_car_finding);	
			}
		}
		printf("Thread ID: %ld, Team: %c, I have found a spot in a car\n", pthread_self(), temp->ch);	
		thread_counter2 += 1;	
		if(temp->ch == 'A') groupA += 1;
		else if(temp->ch == 'B') groupB += 1;		
	}		
	pthread_mutex_unlock(&mutex_car_finding);
	
	if((groupA == 2 && groupB == 2) || (groupA ==4) || (groupB == 4)) group_formed = true;
	//printf("Total people looking for a car: %d\n", counter_of_people_looking_car);
	//printf("Thread Counter2: %d\n", thread_counter2);
	//while(thread_counter2 != counter_of_people_looking_car);
	while(group_formed != true);
	
	pthread_barrier_wait(&barrier);
	pthread_mutex_lock(&mutex_captain);
	if(captain){
		captain = false;
		printf("Thread ID: %ld, Team: %c, I am the captain and driving the car\n", pthread_self(), temp->ch);
	}	
	thread_counter += 1;
	if(thread_counter == 4){
		group_formed = false;
		thread_counter = 0;
		thread_counter2 = 0;
		captain = true;
		counterA -= groupA;
		counterB -= groupB;
		//printf("Total people looking for a car: %d\n", counter_of_people_looking_car);
		counter_of_people_looking_car -= groupA + groupB;
		groupA = 0;
		groupB = 0;	
		//printf("Remaining people looking for a car: %d\n", counter_of_people_looking_car);
		game_turn = 0;
		sem_post(&semaphore);
	}
	pthread_mutex_unlock(&mutex_captain);
}





int main(int argc, char **argv)
{
    if(argc != 3){
    	printf("The main terminates\n");
    	return 0;
    }
    int numA = atoi(argv[1]); 	
    int numB = atoi(argv[2]); 
    
    
    if(!inputcheck(numA, numB)){
    	printf("The main terminates\n");
    	return 0;
    }
    //printf("Nice Input\n");
    
    pthread_t teamA[numA];
    pthread_t teamB[numB];
   
    pthread_barrier_init(&barrier, NULL, 4);
    pthread_cond_init(&condition, NULL);
    
    sem_init(&semaphore, 0 , 1);

    struct lock A;
    A.ch = 'A';   
 
    
    struct lock B;
    B.ch = 'B';   
    
	for(int i =0; i < numA; i++){
		pthread_create(&teamA[i], NULL, &playing, (void *)&A);
	}
	
	for(int i =0; i < numB; i++){
		pthread_create(&teamB[i], NULL, &playing, (void *)&B);
	}
   
    for(int i =0; i < numA; i++){
    		 pthread_join(teamA[i], NULL);
    	}
    for(int i =0; i < numB; i++){
    		 pthread_join(teamB[i], NULL);
    	}
    
    pthread_barrier_destroy(&barrier);
    sem_destroy(&semaphore);

    printf("The main terminates\n");
    //printf("%d\n", numA);
    //printf("%d\n", numB);
    
    
    	  
	
    return 0;
}




