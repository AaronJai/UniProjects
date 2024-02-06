#include "mysync.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Helper function to find a file in an array of FileInfo by filename
FileInfo* find_file_by_name(const char *filename, FileInfo *files, int num_files) {
    for (int i = 0; i < num_files; i++) {
        if (strcmp(filename, files[i].filename) == 0) {
            return &files[i];
        }
    }
    return NULL;
}

// Synchronize directories based on options
void sync_directories(const char *dir1, const char *dir2, const Options *options) {
    printf("Pattern to ignore/only: %s\n", options->pattern);
    int num_files1, num_files2;
    FileInfo *files1 = list_directory(dir1, &num_files1);
    FileInfo *files2 = list_directory(dir2, &num_files2);

    for (int i = 0; i < num_files1; i++) {
        // Check ignore pattern
        if (options->ignore_pattern && matches_pattern(files1[i].filename, options->pattern)) {
            printf("Ignoring file: %s\n", files1[i].filename);
            continue; // Skip this file
        }

        // Check only pattern
        if (options->only_pattern && !matches_pattern(files1[i].filename, options->pattern)) {
            printf("Not copying file due to -o pattern: %s\n", files1[i].filename);
            continue; // Skip this file
        }  
        
        FileInfo *matching_file = find_file_by_name(files1[i].filename, files2, num_files2);
        
        char src_path[1024];
        char dst_path[1024];
        snprintf(src_path, sizeof(src_path), "%s/%s", dir1, files1[i].filename);
        snprintf(dst_path, sizeof(dst_path), "%s/%s", dir2, files1[i].filename);
        
        // If the file doesn't exist in dir2, or if it's older than the one in dir1
        if (!matching_file || matching_file->modification_time < files1[i].modification_time) {
            if (options->verbose) {
                printf("Copying %s to %s\n", src_path, dst_path);
            }
            if (!options->no_act) {
                copy_file(src_path, dst_path, options->preserve);
            }
        }
    }

    // Cleanup
    for (int i = 0; i < num_files1; i++) {
        free(files1[i].filename);
    }
    for (int i = 0; i < num_files2; i++) {
        free(files2[i].filename);
    }
    free(files1);
    free(files2);
}
