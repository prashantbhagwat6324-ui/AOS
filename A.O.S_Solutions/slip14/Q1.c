#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>

int main()
{
    DIR *dp;
    struct dirent *entry;
    struct stat st;
    int n;

    printf("Enter minimum file size in bytes: ");
    scanf("%d", &n);

    dp = opendir(".");
    if (dp == NULL) {
        perror("opendir");
        exit(1);
    }

    printf("\nFiles greater than %d bytes:\n", n);

    while ((entry = readdir(dp)) != NULL) {
        if (stat(entry->d_name, &st) == -1)
            continue;

        if (S_ISREG(st.st_mode)) {  // Only regular files
            if (st.st_size > n)
                printf("%s (%ld bytes)\n", entry->d_name, st.st_size);
        }
    }

    closedir(dp);
    return 0;
}
