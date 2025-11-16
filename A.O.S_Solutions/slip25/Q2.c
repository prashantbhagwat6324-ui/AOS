#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd = open("output2.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }

    // Duplicate fd to STDOUT using dup()
    close(STDOUT_FILENO); 
    dup(fd);  // now stdout -> output2.txt

    printf("This text goes to output2.txt using dup()\n");
    printf("Slip 25 Q2 completed.\n");

    close(fd);
    return 0;
}
