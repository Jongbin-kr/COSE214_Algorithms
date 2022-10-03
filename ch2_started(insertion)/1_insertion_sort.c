#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int* p_arr, int n);

int main(){

    int n, i, j;
    int* p_arr;


    printf("how many input?: ");
    scanf("%d", &n); // input count
    p_arr = (int *)malloc(5 * sizeof(int)); //allocate memory as many as input count

    for (i = 0; i < n; i++){ //input values.
        scanf("%d", p_arr+i);
    }


    insertion_sort(p_arr, n);


    printf("after sort p_arr: ");
    for (i = 0; i < n; i++){
        printf("%d ", p_arr[i]);
    }

    return 0;
}

void insertion_sort(int* p_arr, int n){
    
    int i, j; // i는 기준값을 가리키는 인덱스, j는 비교값을 가리키는 인덱스.
    int key; // 기준값을 저장하는 곳!

    for (i = 1; i < n; i++){
        key = p_arr[i];
        j = i -1;

        while ((j > -1) && ((p_arr[j]) > key)){
            p_arr[j+1] = p_arr[j];
            j -= 1;
        }

        p_arr[j+1] = key;


    }
    
}