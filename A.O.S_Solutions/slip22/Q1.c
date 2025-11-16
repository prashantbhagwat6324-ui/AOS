#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd = open("output.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);

    if (fd < 0) {
        perror("open");
        exit(1);
    }

    dup2(fd, STDOUT_FILENO);  // redirect stdout to output.txt

    printf("This is redirected output.\n");
    printf("Hello from Slip 22 Q1!\n");

    close(fd);
    return 0;
}
