#include <iostream>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
using namespace std;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
//sem_t semaphore;
struct node
{
	int ID;
	int size;
	int index;
	//bool free;
	node *next;
	node *previous;
};

class HeapManager
{
private:
    node *head;
public:
    HeapManager()
    {
        head = NULL;   
    }
    
    void print(){
    	node *temp = head;
    	while(temp != NULL){
    		if(temp->next == NULL){
    			cout << "[" << temp->ID << "]" << "[" << temp->size << "]" << "[" << temp->index << "]";
    		}
    		else{
    			cout << "[" << temp->ID << "]" << "[" << temp->size << "]" << "[" << temp->index << "]" << "---";
    		}
    		temp = temp->next;
    	}
    	cout << endl;
    }
    
    int initHeap(int size){
    	head = new node;
    	head->ID = -1;
    	head->size = size;
    	head->index = 0;
    	//head->free = true;
    	head->next = NULL;
    	head->previous = NULL;
    	return 1;
    }
    
    int myMalloc(int ID, int size){
    	pthread_mutex_lock(&mutex);
    	//cout << "Thread: "<< ID << " Size: " << size << endl;
    	node *temp = head;
		while(temp != NULL){
			if(temp->ID == -1 && size <= temp->size){
				if(temp->size == size){
					temp->ID = ID;
    				cout << "Allocated for thread " << ID << endl;
    				print();
    				pthread_mutex_unlock(&mutex);
    				return temp->index;							
				}
				else{
					node *temp2 = new node;
					temp2->size = temp->size - size;
					temp2->ID = -1;
					temp2->index = temp->index + size;
					temp2->next = temp->next;
					temp2->previous = temp;
					
					temp->ID = ID;
					temp->size = size;
					if(temp->next != NULL)
						temp->next->previous = temp2;
					temp->next = temp2;
    				cout << "Allocated for thread " << ID << endl;
    				print();
    				pthread_mutex_unlock(&mutex);
    				return temp->index;										
				}			
			}		
			temp = temp->next;
		}
    	cout << "Can not allocate, requested size " << size <<" for thread " << ID << " is bigger than remaining size" << endl;
    	print();
    	pthread_mutex_unlock(&mutex);
    	return -1;    
    }
    
   int myFree(int ID, int index){
   		pthread_mutex_lock(&mutex);
   		//cout << "Thread: "<< ID << " Index: " << index << endl;
   		node* temp = head;
   		while(temp != NULL){
   			if(temp->ID == ID && temp->index == index){
   				if(temp->previous != NULL && temp->next != NULL){
   					if(temp->previous->ID == -1 && temp->next->ID == -1){
   						temp->size += temp->previous->size + temp->next->size;
   						//temp->free = true;
   						
   						temp->ID = -1;
   						temp->index = temp->previous->index;
   						
   						if(temp->previous->previous != NULL){
   							
   							node * del = temp->previous;
   							temp->previous->previous->next = temp;
   							temp->previous = temp->previous->previous;
   							delete(del);
   						}
   						else{
   							delete(head);
   							head = temp;
   							temp->previous = NULL;
   						}
   						if(temp->next->next != NULL){
   							
   							node *del = temp->next;
   							temp->next->next->previous = temp;	
   							temp->next = temp->next->next;
   							delete(del);
   						}
   						else{
   							delete(temp->next);
   							temp->next = NULL;
   						}				
   						
   						
   					}
   					else if(temp->previous->ID != -1 && temp->next->ID == -1){
	   					temp->size += temp->next->size;
	   					//temp->free = true;
	   					
	   					temp->ID = -1;
	   					
   						if(temp->next->next != NULL){
   						
   							node *del = temp->next;
   							temp->next->next->previous = temp;	
   							temp->next = temp->next->next;
   							delete(del);
   						}
   						else{
   							delete(temp->next);
   							temp->next = NULL;
   						}		   					
	   					
	   					
   		  			}
	   				else if(temp->previous->ID == -1 && temp->next->ID != -1){
	   					temp->size += temp->previous->size;
	   					temp->index = temp->previous->index;
	   					//temp->free = true;
	   			
	   					temp->ID = -1;
   						if(temp->previous->previous != NULL){
   					
   							node *del = temp->previous;
   							temp->previous->previous->next = temp;
   							temp->previous = temp->previous->previous;	
   							delete(del);
   						}
   						else{
   							delete(head);
   							head = temp;
   							temp->previous = NULL;
   						}
	   					   					  				
	   				}	
	   				else{
	   					//temp->free = true;
	   					temp->ID = -1;  					
	   				}			
   				}
   				else if(temp->previous == NULL && temp->next != NULL){
   					if(temp->next->ID == -1){
 	   					temp->size += temp->next->size;
	   					//temp->free = true;
	   		
	   					temp->ID = -1;
   						if(temp->next->next != NULL){
   		
   							node *del = temp->next;
   							temp->next->next->previous = temp;	
   							temp->next = temp->next->next;
   							delete(del);
   						} 
   						else{
   							delete(temp->next);
   							temp->next = NULL;
   						}	   					
	   					 							
   					}
	   				else{
	   					//temp->free = true;
	   					temp->ID = -1;  					
	   				}	   									
   				}
   				else if(temp->previous != NULL && temp->next == NULL){
   					if(temp->previous->ID == -1){
 	   					temp->size += temp->previous->size;
 	   					temp->index = temp->previous->index;
	   					//temp->free = true;
	   			
	   					temp->ID = -1;
   						if(temp->previous->previous != NULL){
   		
   							node *del = temp->previous;
   							temp->previous->previous->next = temp;
   							temp->previous = temp->previous->previous;
   							delete(del);
   						}  
   						else{
   							delete(head);
   							head = temp;
   							temp->previous = NULL;
   						}
	   												
   					}
	   				else{
	   					//temp->free = true;
	   					temp->ID = -1;  					
	   				}   						
   				}
   				else{
	   					//temp->free = true;
	   		
	   					temp->ID = -1;  
   				} 
   				
   				cout << "Freed for thread " << ID << endl;
   				print();
   				pthread_mutex_unlock(&mutex);
   				return 1;			
   			}
   			temp = temp->next;  			
   		}
   		cout << "Can not free for " << ID << endl;
   		pthread_mutex_unlock(&mutex);
   		return -1;
   
   }

};


