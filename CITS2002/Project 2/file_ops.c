#define _POSIX_C_SOURCE 200809L
#include "mysync.h"
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <utime.h>
#include <dirent.h>
#include <stdlib.h>
#include <string.h>

char** list_dir_contents(const char *dir_path, int *num_items) {
    DIR *dir = opendir(dir_path);
    if (!dir) {
        perror("Failed to open directory");
        *num_items = 0;
        return NULL;
    }

    char **file_list = malloc(1024 * sizeof(char*)); // Assuming max 1024 files, you might want to handle this dynamically
    int count = 0;

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) { // Exclude . and ..
            file_list[count] = strdup(entry->d_name);
            count++;
        }
    }
    closedir(dir);

    *num_items = count;
    return file_list;
}

// Copies a file from the source path to the destination path
void copy_file(const char *src_path, const char *dst_path, bool preserve) {
    struct stat src_stat;
    if (stat(src_path, &src_stat) == -1) {
        perror("Failed to stat source path");
        return;
    }

    // Check if src_path is a directory
    if (S_ISDIR(src_stat.st_mode)) {
        mkdir(dst_path, 0755);
        return;
    }

    int src_fd = open(src_path, O_RDONLY);
    if (src_fd == -1) {
        perror("Failed to open source file");
        return;
    }

    // After opening the destination file...
    int dst_fd = open(dst_path, O_WRONLY | O_CREAT, 0666);
    if (dst_fd == -1) {
        perror("Failed to open destination file");
        close(src_fd);
        return;
    }

    // Set the file permissions using fchmod
    if (preserve) {
        fchmod(dst_fd, src_stat.st_mode);
    }

    char buffer[4096];
    ssize_t bytes_read;

    while ((bytes_read = read(src_fd, buffer, sizeof(buffer))) > 0) {
        write(dst_fd, buffer, bytes_read);
    }

    close(src_fd);
    close(dst_fd);

    printf("Source permissions: %o\n", src_stat.st_mode & 0777);
    // Handle preservation of modification time if 'preserve' is true
    if (preserve) {
        struct utimbuf new_times;
        new_times.actime = src_stat.st_atime;  // access time
        new_times.modtime = src_stat.st_mtime; // modification time
        utime(dst_path, &new_times);           // set the times
    }
}

// Get the modification time of a file
long get_file_modification_time(const char *path) {
    struct stat s;
    if (stat(path, &s) == 0) {
        return s.st_mtime;
    }
    return 0;
}
