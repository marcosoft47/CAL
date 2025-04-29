#include <stdio.h>
#include <stdlib.h>


#define N 61
// #define N 10
#define PAREDE "#"
#define CAMINHO "o"



void printMaze(int maze[N][N]){
    printf("Caminho no labirinto:\n");
    printf("%s ",PAREDE);
    for (int j = 1; j < N+1; j++) {
        printf("%s",PAREDE);
    }
    printf("\n");
    for (int i = 0; i < N; i++) {
        printf("%s",PAREDE);
        for (int j = 0; j < N; j++) {
            if(maze[i][j] == 1){
                printf("%s",PAREDE);
            }else if(maze[i][j] == 2){
                printf("%s", CAMINHO);
            }else{
                printf(" ");
            }
            //printf("%d ", maze[i][j]);
        }
        printf("%s\n",PAREDE);
    }
    for (int j = 0; j < N; j++) {
        printf("%s",PAREDE);
    }
    printf(" %s\n",PAREDE);
}

int isSafe(int maze[N][N], int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 0);
}

int solveMazeUtil(int maze[N][N], int x, int y) {
    
    maze[x][y] = 2;
    if (isSafe(maze,x,y+1)){ // Cima
        if (solveMazeUtil(maze,x,y+1)==1){
            return 1;
        }
    }

    if (isSafe(maze,x+1,y)){ // Direita
        if (solveMazeUtil(maze,x+1,y)==1){
            return 1;
        }
    }

    if (isSafe(maze,x,y-1)){ // Baixo
        if (solveMazeUtil(maze,x,y-1)==1){
            return 1;
        }
    }

    if (isSafe(maze,x-1,y)){ // Esquerda
        if (solveMazeUtil(maze,x-1,y)==1){
            return 1;
        }
    }

    // printMaze(maze);
    if (x == N-1 && y == N-1)
        return 1; // caminho certo
    maze[x][y] = 0;
    return 0; // caminho errado
}


int solveMaze(int maze[N][N]) {
    // Iniciar a busca a partir do ponto de partida (0, 0)

    if (solveMazeUtil(maze, 0, 0) == 0) {
        printf("Não há solução para o labirinto.\n");
        return 0;
    }

    // Imprimir
    printMaze(maze);
    return 1;
}

void loadMaze(int maze[N][N], char *fname){
    //gere um nesse site, cole no arquivo lab.txt ou outro
    //https://www.dcode.fr/maze-generator
    //veja quantas linhas e colunas tem e altere o valor de N
    //uma diferença de 1 na quantia de colunas geralmente não causa problema
    //pois o algoritmo aqui inclui uma borda extra
    FILE *f;
    int i, lineN = 0;
    char line[N+10];
    f = fopen(fname, "r");
    while(fgets(line, sizeof(line), f) != NULL){
        i = 0;
        if(line[0]=='0' || line[0] == '1'){
            while(line[i] != '\0'){
                maze[lineN][i] = line[i] - '0';
                i++;
                if(i>=N) break;
            }
            lineN++;
            if(lineN>=N){ break;}
        }
    }

    printf("i: %d, LineN: %d\n", i, lineN);

}

int main() {
    /*
    //1 = parede
    //0 = vazio
    //2 = caminho
    */
    // int maze[N][N] = {
    //     {0, 1, 0, 0, 0, 0, 0, 1, 0, 0},
    //     {0, 1, 0, 1, 1, 0, 1, 1, 0, 1},
    //     {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
    //     {1, 1, 0, 1, 0, 1, 1, 1, 1, 0},
    //     {0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
    //     {0, 1, 0, 0, 0, 1, 1, 0, 1, 1},
    //     {0, 1, 1, 1, 1, 1, 1, 0, 1, 0},
    //     {0, 1, 0, 0, 0, 1, 0, 0, 0, 0},
    //     {0, 1, 0, 1, 0, 1, 1, 1, 1, 0},
    //     {0, 0, 0, 1, 0, 0, 0, 0, 0, 0}
    // };
    int maze[N][N];

    loadMaze(maze, "lab.txt");

    if (solveMaze(maze)) {
        printf("Labirinto resolvido!\n");
    } else {
        printf("Não foi possível encontrar uma solução.\n");
    }

    return 0;
}

