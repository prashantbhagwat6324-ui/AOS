#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd = open("output1.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }

    dup2(fd, STDOUT_FILENO);  // Redirect stdout to file

    printf("This output is redirected to output1.txt\n");
    printf("Slip 25 Q1 completed.\n");

    close(fd);
    return 0;
}
