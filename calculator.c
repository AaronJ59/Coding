#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_long("x: ");
    int y = get_long("y: ");

    double z = (double) x / (double) y;

    printf("%.20f\n", z);
}
