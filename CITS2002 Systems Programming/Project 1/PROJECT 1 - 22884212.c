//  CITS2002 Project 1 2023
//  myscheduler (v1.0)
//  Student:    22884212    AARON ZHENG JIE TAN

//  Device data-transfer rates measured in bytes/second,
//  All times measured in microseconds (usecs),
//  Total process completion time will not exceed 2000 seconds.

//  Compile with:  cc -std=c11 -Wall -Werror -o myscheduler myscheduler.c

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//  Maximum limits for devices and commands
#define MAX_DEVICES 4
#define MAX_DEVICE_NAME 20
#define MAX_COMMANDS 10
#define MAX_COMMAND_NAME 20
#define MAX_SYSCALLS_PER_PROCESS 40
#define MAX_RUNNING_PROCESSES 50

//  Default time quantum value
#define DEFAULT_TIME_QUANTUM 100

//  Time durations for various state transitions
#define TIME_CONTEXT_SWITCH 5
#define TIME_CORE_STATE_TRANSITIONS 10
#define TIME_ACQUIRE_BUS 20

//  Structure to represent a device
typedef struct {
    char name[MAX_DEVICE_NAME];
    unsigned long read_speed;
    unsigned long write_speed;
} Device;

//  Structure to represent a command
typedef struct {
    char name[MAX_COMMAND_NAME];
    char syscalls[MAX_SYSCALLS_PER_PROCESS][20];
    int num_syscalls;
} Command;

//  Function prototypes
void read_sysconfig(char argv0[], char filename[]);
void read_commands(char argv0[], char filename[]);
void execute_command(const Command *cmd);

Device devices[MAX_DEVICES];
int num_devices = 0;
unsigned long time_quantum = DEFAULT_TIME_QUANTUM;
Command commands[MAX_COMMANDS];
int num_commands = 0;
unsigned long total_elapsed_time = 0;

//  ----------------------------------------------------------------------

//  Function to read sysconfig file and populate device and time quantum data
void read_sysconfig(char argv0[], char filename[]) {
    FILE *sysconfig = fopen(filename, "r");
    if (!sysconfig) {
        perror("Error opening sysconfig file");
        exit(EXIT_FAILURE);
    }

    char line[256];
    while (fgets(line, sizeof(line), sysconfig)) {
        //  Check for valid lines in sysconfig file
        if (line[0] != '#' && line[0] != '\n') {
            if (strncmp(line, "device", 6) == 0) {
                //  Parse and store device data
                sscanf(line, "%*s %s %luBps %luBps", devices[num_devices].name,
                       &devices[num_devices].read_speed, &devices[num_devices].write_speed);
                num_devices++;
            } else if (strncmp(line, "timequantum", 11) == 0) {
                //  Parse and store time quantum value
                sscanf(line, "%*s %luusec", &time_quantum);
            }
        }
    }
    fclose(sysconfig);
}

//  Function to read command file and populate command data
void read_commands(char argv0[], char filename[]) {
    FILE *command_file = fopen(filename, "r");
    if (!command_file) {
        perror("Error opening command file");
        exit(EXIT_FAILURE);
    }

    char line[256];
    int cmd_index = -1;
    while (fgets(line, sizeof(line), command_file)) {
        //  Check for comments and empty lines
        if (line[0] == '#' && line[0] != '\n') {
            continue;
        } else if (line[0] != '\n') {
            if (line[0] == '\t') {
                //  Parse and store system calls for a command
                if (cmd_index >= 0 && cmd_index < num_commands && 
                    commands[cmd_index].num_syscalls < MAX_SYSCALLS_PER_PROCESS) {
                    strncpy(commands[cmd_index].syscalls[commands[cmd_index].num_syscalls], line + 1, 20);
                    commands[cmd_index].num_syscalls++;
                } else {
                    fprintf(stderr, "Invalid command line format\n");
                    exit(EXIT_FAILURE);
                }
            } else {
                //  Parse and store command name
                if (num_commands < MAX_COMMANDS) {
                    sscanf(line, "%s", commands[num_commands].name);
                    cmd_index = num_commands;
                    commands[num_commands].num_syscalls = 0;
                    num_commands++;
                } else {
                    fprintf(stderr, "Too many commands\n");
                    exit(EXIT_FAILURE);
                }
            }
        }
    }
    fclose(command_file);
}

//  ----------------------------------------------------------------------

//  Function to execute a given command
void execute_command(const Command *cmd) {
    unsigned long elapsed_time = 0;
    for (int i = 0; i < cmd->num_syscalls; i++) {
        //  Simulate time passing
        sleep(elapsed_time / 1000000);
        //  Print the system call being executed
        printf("%s\n", cmd->syscalls[i]);
        elapsed_time += time_quantum;
        total_elapsed_time += elapsed_time;
    }
}

//  ----------------------------------------------------------------------

int main(int argc, char *argv[]) {
    //  Check command-line arguments
    if (argc != 3) {
        fprintf(stderr, "Usage: %s sysconfig-file command-file\n", argv[0]);
        return EXIT_FAILURE;
    }

    //  Read sysconfig file
    read_sysconfig(argv[0], argv[1]);

    //  Read command file
    read_commands(argv[0], argv[2]);

    // Print system configuration
    printf("found %d devices\n", num_devices);
    printf("time quantum is %lu\n", time_quantum);
    printf("found %d commands\n", num_commands);

    //  Execute each command and track time
    for (int i = 0; i < num_commands; i++) {
        execute_command(&commands[i]);
    }

    // Get CPU-utilisation
    int cpu_utilisation = (total_elapsed_time * 100) / (num_commands * time_quantum);

    //  Print final measurements
    printf("measurements  %lu  %d\n", num_commands * time_quantum, cpu_utilisation);

    return EXIT_SUCCESS;
}
