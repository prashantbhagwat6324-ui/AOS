#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>

int main()
{
    int n;
    printf("Enter number of child processes: ");
    scanf("%d", &n);

    struct rusage usage;
    long total_user = 0, total_sys = 0;

    for (int i = 0; i < n; i++) {
        pid_t pid = fork();

        if (pid < 0) {
            perror("fork");
            exit(1);
        }

        if (pid == 0) {
            // Child process → simulate work
            for (long j = 0; j < 50000000; j++); // busy loop
            exit(0);
        }
    }

    // Parent waits for all children
    for (int i = 0; i < n; i++) {
        wait3(NULL, 0, &usage);
        total_user += usage.ru_utime.tv_sec * 1000000 + usage.ru_utime.tv_usec;
        total_sys  += usage.ru_stime.tv_sec * 1000000 + usage.ru_stime.tv_usec;
    }

    printf("\nTotal cumulative user time   = %ld microseconds\n", total_user);
    printf("Total cumulative system time = %ld microseconds\n", total_sys);

    return 0;
}
