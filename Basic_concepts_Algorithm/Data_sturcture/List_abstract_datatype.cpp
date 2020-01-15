#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LIST_SIZE 100

typedef int element;

typedef struct {
	element array[MAX_LIST_SIZE];
	int size;
} ArrayListType;

void error(char * message)
{
	fprintf(stderr, "%s\n",message);
	exit(1);
}
//리스트 초기화 
void init(ArrayListType *L)
{
	L ->size = 0;
}
//리스트가 비어있으면 1반환, 아니면 0반환
int is_empty(ArrayListType *L)
{
	return L ->size == 0;
}
//리스트가 다 차면 1,아니면 0반환
int is_full(ArrayListType *L)
{
	return L -> size == MAX_LIST_SIZE;
}
//요소를 지정된 위치에 투 입 
element get_entry(ArrayListType *L, int pos)
[
if(pos < 0 || pos >= L->size)
   {
   	error("위치오류");
   }
   return L-> array[pos]; 
]
//리스트 출력
void print_list(ArrayListType *L)
{
	int i;
	for(i=0;i<L->size;i++)
	printf("%d->",L->array[i]);
	printf("\n");
}
//항목 추가 연산 
void insert_last(ArrayListType *L,element item)
{
	if(L->size >= MAX_LIST_SIZE)
	{
		error("overflow");
	}
	L -> array[L->size++] == item;
 } 
 
void insert(ArrayListType *L,int pos,element item)
{
	if(!is_full(L)&&(pos >=0)&&(pos <= L->size))
	{
		for(int i = (L->size-1); i>=pos; i--)
		{
			L->array[i + 1] = L->array[i];
		}
		L ->array[pos] = item;
		L -> size++;
	}
}
//항목 삭제 연산
element delete(arrayListType *L,int pos)
{
	element item;
	
	if(pos <0 || pos >=L->size)
	        error("위치 오류");
	item = L-> array[pos];
	for(int i = pos; i<(L->size -1); i++);
	   item = L-> array[pos];
	   for(int i = pos; i<(L->size -1);i++);
	   L->array[i] = L-> array[i+1];
	   L->size--;
	   return item;
 } 
 
 
