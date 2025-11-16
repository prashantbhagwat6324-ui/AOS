#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <time.h>

int main()
{
    DIR *dp;
    struct dirent *entry;
    struct stat st;

    int month;
    printf("Enter month number (1-12): ");
    scanf("%d", &month);

    dp = opendir(".");
    if (dp == NULL) {
        perror("opendir");
        exit(1);
    }

    printf("\nFiles created in month %d:\n", month);

    while ((entry = readdir(dp)) != NULL) {
        if (stat(entry->d_name, &st) == -1)
            continue;

        struct tm *timeinfo = localtime(&st.st_mtime);
        int file_month = timeinfo->tm_mon + 1; // 0-11 → +1

        if (file_month == month) {
            printf("%s\n", entry->d_name);
        }
    }

    closedir(dp);
    return 0;
}
