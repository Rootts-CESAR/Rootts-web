#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct Lista{
    struct Lista *head1,*head2;
    char individuo[25];
    struct Lista*next;
} Lista;
int vazia(Lista *head){ 
	return head == NULL;
}
int inserir(struct Lista **head, char str[50])
{
    struct Lista *novo;
    novo = (struct Lista*)malloc(sizeof(struct Lista));
    strcpy(novo->individuo,str);
    novo->next = NULL;
    if (*head == NULL)     
    {
        *head = novo;       
        return 0;
    }                      
    struct Lista *current;   
    current = *head;
    while (current->next != NULL){
        current = current->next;}     
    current->next = novo;    
    return 0;
}
void remover_duplicado(struct Lista **head) {  
    struct Lista *current = *head, *index = NULL, *temp = NULL;  
      
    if(head == NULL) {  
        return;  
    }  
    else {  
        while(current != NULL){  
            temp = current;
            index = current->next;  
              
            while(index != NULL) {  
                if(strcmp(current->individuo , index->individuo)==0) {  
                    temp->next = index->next;  
                }  
                else {  
                    temp = index;  
                }  
                index = index->next;  
            }  
            current = current->next;  
        }          
    }  
}  
void print(Lista*head) {
    Lista*atual= head;
   	while ( atual!= NULL) {
        printf("%s\n", atual->individuo);
        atual= atual->next;
    }
}
void ordenar(Lista **head) {

    if(*head == NULL || (*head)->next == NULL) return; 
    Lista *aux = *head, *t;
    char s[100]; 

    while(aux != NULL) {
      t = aux->next;
      while(t != NULL) {
        if(strcmp(aux->individuo, t->individuo) > 0) { 
            strcpy(s, aux->individuo);
            strcpy(aux->individuo, t->individuo);
            strcpy(t->individuo, s);
        }
        t = t->next;
      }
      aux = aux->next;
    }
}
int main() {
    struct Lista *head1=NULL,*head2=NULL;
    char nome[50],op[4],amigo[1][20];
    int cont=0,maior;
    while(1){
    scanf("%s",nome);
     if(strcmp(nome,"FIM")==0)
     break;
     scanf("%s",op);
     if (strcmp(op,"YES")==0){
        inserir(&head1,nome);
        if(cont==0){
            strcpy(amigo[0],nome);
            maior=strlen(nome);
        }
        else{
            if (strlen(nome)>maior){
                maior=strlen(nome);
                strcpy(amigo[0],nome);
            }
        }
        cont++;  
     }
     else if(strcmp(op,"NO")==0){
        inserir(&head2,nome);
     }
  
    }
    remover_duplicado(&head1);
    remover_duplicado(&head2);
    ordenar(&head1);
    ordenar(&head2);
    print(head1);
    print(head2);
    printf("\nAmigo do Habay:\n%s",amigo[0]);
}