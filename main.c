#include <stdio.h>
#include <stdlib.h>
#include <string.h>  // Add this header for strcspn and strcmp

int main() {
    char user_input[256];
    int return_value;

    while (1) {
        // Prompt user for input
        printf("Enter your message (or type 'exit' to quit): ");
        fgets(user_input, sizeof(user_input), stdin);

        // Remove trailing newline if it exists
        user_input[strcspn(user_input, "\n")] = '\0';

        // Check if user wants to exit
        if (strcmp(user_input, "exit") == 0) {
            printf("Exiting chatbot...\n");
            break;
        }

        // Call the shell script with the user's input
        return_value = system("/Users/mhmh/Desktop/data/d2/script.sh");

        // Check if the script executed successfully
        if (return_value == -1) {
            perror("Error executing the script");
            return EXIT_FAILURE;
        }
    }

    return EXIT_SUCCESS;
}
