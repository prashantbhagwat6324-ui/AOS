#include <stdio.h>
#include <stdlib.h>
#include <sys/resource.h>

int main()
{
    struct rlimit rl;

    // Get current file limit
    getrlimit(RLIMIT_NOFILE, &rl);
    printf("Current File Limit: Soft = %ld Hard = %ld\n",
           rl.rlim_cur, rl.rlim_max);

    // Set new soft file limit
    rl.rlim_cur = 2048;
    setrlimit(RLIMIT_NOFILE, &rl);

    // Display updated file limit
    getrlimit(RLIMIT_NOFILE, &rl);
    printf("Updated File Limit: Soft = %ld Hard = %ld\n",
           rl.rlim_cur, rl.rlim_max);

    // Get memory limit
    getrlimit(RLIMIT_AS, &rl);
    printf("Current Memory Limit: Soft = %ld Hard = %ld\n",
           rl.rlim_cur, rl.rlim_max);

    return 0;
}
