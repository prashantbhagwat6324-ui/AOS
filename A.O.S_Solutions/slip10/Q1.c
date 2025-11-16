#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int fd[2];
    pid_t p1, p2;

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    p1 = fork();
    if (p1 == 0) {
        // First child → Command 1
        // Example: ls -l
        close(fd[0]);                    // close read end
        dup2(fd[1], STDOUT_FILENO);      // write output to pipe
        close(fd[1]);

        execlp("ls", "ls", "-l", NULL);
        perror("execlp");
        exit(1);
    }

    p2 = fork();
    if (p2 == 0) {
        // Second child → Command 2
        // Example: wc -l
        close(fd[1]);                    // close write end
        dup2(fd[0], STDIN_FILENO);       // read input from pipe
        close(fd[0]);

        execlp("wc", "wc", "-l", NULL);
        perror("execlp");
        exit(1);
    }

    // Parent process
    close(fd[0]);
    close(fd[1]);

    wait(NULL);
    wait(NULL);

    return 0;
}
