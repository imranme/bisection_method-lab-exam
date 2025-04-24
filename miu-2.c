#include <stdio.h>

int main() {
    int numbers[10];
    int sum = 0;
    int highest = 0;
    int lowest;

    printf("Enter 10 numbers:\n");

    for (int i = 0; i < 10; i++) {
        printf("Number %d: ", i + 1);
        scanf("%d", &numbers[i]);


        sum += numbers[i];
        if (numbers[i] > highest) {
            highest = numbers[i];
        }
        else if (i == 0 || numbers[i] < lowest) {
            lowest = numbers[i];
        }

    }
    float average = (float) sum / 10;

    printf("Average number: %.2f\n", average);
    printf("Highest number: %d\n", highest);
    printf("Lowest number: %d\n", lowest);

    return 0;
}

