#define _POSIX_C_SOURCE 200809L
#include "mysync.h"
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// Check if a given path is a directory
bool is_directory(const char *path) {
    struct stat s;
    if (stat(path, &s) == 0) {
        if (S_ISDIR(s.st_mode)) {
            return true;
        }
    }
    return false;
}

// List all files in a directory and store their modification times
FileInfo* list_directory(const char *dir_path, int *num_files) {
    DIR *dir = opendir(dir_path);
    if (!dir) {
        perror("Failed to open directory");
        return NULL;
    }

    int capacity = 10;
    *num_files = 0;
    FileInfo *files = malloc(capacity * sizeof(FileInfo));

    struct dirent *entry;
    while ((entry = readdir(dir))) {
        // Skip '.' and '..' entries
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        // Resize array if necessary
        if (*num_files >= capacity) {
            capacity *= 2;
            files = realloc(files, capacity * sizeof(FileInfo));
        }

        files[*num_files].filename = strdup(entry->d_name);
        
        // Fetch and store modification time
        char full_path[1024];
        snprintf(full_path, sizeof(full_path), "%s/%s", dir_path, entry->d_name);
        struct stat file_stat;
        if (stat(full_path, &file_stat) == 0) {
            files[*num_files].modification_time = file_stat.st_mtime;
        } else {
            files[*num_files].modification_time = 0;
        }

        (*num_files)++;
    }

    closedir(dir);
    return files;
}
