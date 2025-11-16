#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int fd[2];
    pid_t pid1, pid2;

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid1 = fork();

    if (pid1 < 0) {
        perror("fork");
        exit(1);
    }

    if (pid1 == 0) {
        // First child → execute "ls -l"
        close(fd[0]);               // close read end
        dup2(fd[1], STDOUT_FILENO); // redirect stdout to pipe
        close(fd[1]);

        execlp("ls", "ls", "-l", NULL);
        perror("execlp"); // only if exec fails
        exit(1);
    }

    pid2 = fork();

    if (pid2 < 0) {
        perror("fork");
        exit(1);
    }

    if (pid2 == 0) {
        // Second child → execute "wc -l"
        close(fd[1]);               // close write end
        dup2(fd[0], STDIN_FILENO);  // redirect stdin to pipe
        close(fd[0]);

        execlp("wc", "wc", "-l", NULL);
        perror("execlp");
        exit(1);
    }

    // Parent closes both ends
    close(fd[0]);
    close(fd[1]);

    wait(NULL);
    wait(NULL);

    return 0;
}
