#include <stdio.h>
#include <stdlib.h>


void printArr(int *v, int n){
    for (int i = 0; i < n; i++)
        printf("%i ", v[i]);
    printf("\n");
}
int isOrdered(int *v, int n){
    for (int i = 0; i < n-1; i++){
        if (v[i] > v[i+1])
            return 0;
    }
    return 1;
}

void bubble(int *v, int n){
	int i, j, aux;
    int flag = 0;
	for(i = n-1; i > 0 && flag != 1; i--){
        flag = isOrdered(v, n);
		for (j = 0; j < i && flag != 1; j++){
			if(v[j] > v[j+1]){
				aux = v[j];
				v[j] = v[j+1];
				v[j+1] = aux;
                
                
			}
            printArr(v, n);
		}
	}
}
void insert(int *v, int n){
    int i, j, x;
    for(i = 0; i < n; i++){
        x = v[i];
        j = i-1;
        while(j >= 0 && v[j] > x){
            v[j+1] = v[j];
            j--;
            printf("\ni: %i j: %i x: %i\n", i, j, x);
            printArr(v, n);
        }
        v[j+1] = x;
        printf("\ni: %i j: %i x: %i\n", i, j, x);
        printArr(v, n);
    }
}
int main(){
    int v[] = {50,40,10,30};
    int n = sizeof(v) / sizeof(int);
    // bubble(v, n);
    insert(v, n);
}