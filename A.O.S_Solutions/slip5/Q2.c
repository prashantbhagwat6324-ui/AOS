#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    int fd[2];
    pid_t pid;
    char buffer[50];

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child process → write to pipe
        close(fd[0]);  // close read end

        write(fd[1], "Hello World\n", 12);
        write(fd[1], "Hello SPPU\n", 11);
        write(fd[1], "Linux is Funny\n", 16);

        close(fd[1]);
    }
    else {
        // Parent process → read from pipe
        close(fd[1]);  // close write end

        printf("Messages from pipe:\n");
        while (read(fd[0], buffer, sizeof(buffer)) > 0) {
            printf("%s", buffer);
        }

        close(fd[0]);
    }

    return 0;
}
