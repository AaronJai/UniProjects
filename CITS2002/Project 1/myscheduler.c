//  CITS2002 Project 1 2023
//  Student:    22884212    AARON ZHENG JIE TAN

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
    char name[MAX_DEVICE_NAME];                                                                             //  Name of device
    unsigned long read_speed;                                                                               //  Read speed
    unsigned long write_speed;                                                                              //  Write speed
} Device;

//  Structure to represent a command
typedef struct {
    char name[MAX_COMMAND_NAME];                                                                            //  Name of command
    char syscalls[MAX_SYSCALLS_PER_PROCESS][20];                                                            //  Array to hold syscalls associated with the command
    int num_syscalls;                                                                                       //  Number of syscalls in command
} Command;

//  Function prototypes
void read_sysconfig(char argv0[], char filename[]);
void read_commands(char argv0[], char filename[]);
void execute_command(const Command *cmd);

//  Initialise variables for use
Device devices[MAX_DEVICES];                                                                                //  Array to hold device information
int num_devices = 0;                                                                                        //  Counter for number of devices read from sysconfig-file 
unsigned long time_quantum = DEFAULT_TIME_QUANTUM;                                                          //  Default time quantum value
Command commands[MAX_COMMANDS];                                                                             //  Array to hold command information
int num_commands = 0;                                                                                       //  Counter for number of commands read from command-file
unsigned long total_possible_time = 0;                                                                      //  Total time that could be used (busy and idle time)
unsigned long total_busy_time = 0;                                                                          //  Total time CPU is busy executing commands    

//  ----------------------------------------------------------------------

//  Function to read sysconfig file and populate device and time quantum data
void read_sysconfig(char argv0[], char filename[]) {
    FILE *sysconfig = fopen(filename, "r");
    if (!sysconfig) {
        perror("Error opening sysconfig file");
        exit(EXIT_FAILURE);
    }

    char line[256];
    //  Loop to read lines from sysconfig file
    while (fgets(line, sizeof(line), sysconfig)) {
        //  Check for valid lines in sysconfig file
        if (line[0] != '#' && line[0] != '\n') {
            if (strncmp(line, "device", 6) == 0) {                                                          //  Check line to start with "device" in sysconfig-file ('6' finds number of characters)
                //  Parse and store device data
                sscanf(line, "%*s %s %luBps %luBps", devices[num_devices].name,
                       &devices[num_devices].read_speed, &devices[num_devices].write_speed);                //  Read device name and read/write speeds in bps
                num_devices++;
            } else if (strncmp(line, "timequantum", 11) == 0) {                                             //  Check if sysconfig specifies a certain time quantum
                //  Parse and store time quantum value
                sscanf(line, "%*s %luusec", &time_quantum);                                                 //  Extract and store time quantum value
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
    int cmd_index = -1;                                                                                     //  Initialised to -1 to indicate not currently processing commands
    //  Loop to read from command file
    while (fgets(line, sizeof(line), command_file)) {
        //  Check for valid lines in command file
        if (line[0] == '#' || line[0] == '\n') {
            continue;
        }
        if (line[0] == '\t') {
            //  Parse and store system calls for a command
            if (cmd_index >= 0 && cmd_index < num_commands && 
                commands[cmd_index].num_syscalls < MAX_SYSCALLS_PER_PROCESS) {                              //  Checking if processing a valid command, not exceeded max commands, and if more syscalls can be accomodated
                strncpy(commands[cmd_index].syscalls[commands[cmd_index].num_syscalls], line + 1, 20);      //  Copy syscall details from 'line' and skips first char (an indent)
                commands[cmd_index].num_syscalls++;
            }
        } else {
            //  Parse and store command name
            if (num_commands < MAX_COMMANDS) {                                                              //  Check for space available for more 'commands' in the commands array
                sscanf(line, "%s", commands[num_commands].name);                                            //  To set name of current command based on details in 'line'
                cmd_index = num_commands;                                                                   //  Indicate this specific command is currently being processed
                commands[num_commands].num_syscalls = 0;                                                    //  Initialise number of syscalls for the current command
                num_commands++;
            }
        }
    }
    fclose(command_file);
}

//  ----------------------------------------------------------------------

//  Function to execute a given command
void execute_command(const Command *cmd) {
    unsigned long elapsed_time = 0;
    unsigned long idle_time = 0;
    unsigned long syscall_time;

    //  Loop through each syscall in the command
    for (int i = 0; i < cmd->num_syscalls; i++) {
        //  Extract operation, device, and bytes from syscall string
        char operation[10], device[20];
        unsigned long bytes;
        sscanf(cmd->syscalls[i], "%luusecs %s %s %luB", &syscall_time, operation, device, &bytes);          //  Parse syscall information from a string and store in variables

        //  Calculate the remaining execution time for this syscall
        unsigned long remaining_time = syscall_time;

        //  Execute context switch, core state transitions, and data-bus acquisition
        elapsed_time += TIME_CONTEXT_SWITCH + TIME_CORE_STATE_TRANSITIONS + TIME_ACQUIRE_BUS;
        total_possible_time += TIME_CONTEXT_SWITCH + TIME_CORE_STATE_TRANSITIONS + TIME_ACQUIRE_BUS;

        //  Check if the remaining execution time exceeds the time quantum
        if (remaining_time > time_quantum) {
            //  Ensure syscall is within the time quantum
            syscall_time = time_quantum;
        } 
        //  Add syscall_time to elapsed_time (not the full time quantum)
        elapsed_time += syscall_time;

        //  Check for idle time before syscall string
        if (syscall_time > 0) {
            idle_time = syscall_time;
            total_possible_time += idle_time;
        }

        //  Determine time taken by syscall based on device speeds
        for (int j = 0; j < num_devices; j++) {
            if (strcmp(devices[j].name, device) == 0) {
                if (strcmp(operation, "read") == 0) {
                    syscall_time = (bytes / devices[j].read_speed) * 1000000;                               // Multiply by 1000000 to convert to microseconds
                } else if (strcmp(operation, "write") == 0) {
                    syscall_time = (bytes / devices[j].write_speed) * 1000000;
                }
                break;                                                                                      // Exit loop - matching device found and processed
            }
        }

        //  Update total execution time for this command
        total_possible_time += elapsed_time;
        total_busy_time += elapsed_time;

        //  Simulate the command (print the syscall)
        printf("%s\n", cmd->syscalls[i]);
    }
}

//  ----------------------------------------------------------------------

int main(int argc, char *argv[]) {
    //  Check command-line arguments
    if (argc != 3) {
        fprintf(stderr, "Usage: %s sysconfig-file command-file\n", argv[0]);
        return EXIT_FAILURE;
    }

    //  Read sysconfig-file
    read_sysconfig(argv[0], argv[1]);

    //  Read command-file
    read_commands(argv[0], argv[2]);

    // Print system configuration
    printf("found %d devices\n", num_devices);
    printf("time quantum is %lu\n", time_quantum);
    printf("found %d commands\n", num_commands);

    //  Execute each command and track time
    for (int i = 0; i < num_commands; i++) {
        execute_command(&commands[i]);
    }

    //  Calculate CPU-utilisation
    int cpu_utilisation = (total_busy_time * 100) / total_possible_time;

    //  Print final measurements
    printf("measurements  %lu  %d\n", total_possible_time, cpu_utilisation);

    return EXIT_SUCCESS;
}