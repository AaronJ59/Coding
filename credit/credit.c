#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long number = get_long("Number: ");

    if (!((number >= 340000000000000 && number <= 349999999999999) || // American express
          (number >= 370000000000000 && number <= 379999999999999) || // American Express
          (number >= 5100000000000000 && number <= 5599999999999999) || // MasterCard
          (number >= 4000000000000 && number <= 4999999999999) || // Visa
          (number >= 4000000000000000 && number <= 4999999999999999))) // Visa
    {
        printf("INVALID\n");
        return 0; // exits the code
    }

    long denominator = 10;

    int sum_of_num = 0;

    for (int i = 0; i < 18; i++)
    {
        long digit = (number / denominator) % 10;

        denominator = denominator * 100;
        int digit_multiplied = digit * 2;

        if (digit_multiplied >= 10)
        {
            int integer = (digit_multiplied / 1) % 10;
            integer = integer + 1;
            digit_multiplied = integer;
        }
        sum_of_num = sum_of_num + digit_multiplied;
    }

    denominator = 1;

    for (int j = 0; j < 18; j++)
    {
        long digit_ = (number / denominator) % 10;

        denominator = denominator * 100;

        sum_of_num = sum_of_num + digit_;
    }

    int last_digit = (sum_of_num / 1) % 10;

    if (last_digit != 0)
    {
        printf("INVALID\n");
    }

    if (last_digit == 0)
    {
        if ((number >= 340000000000000 && number <= 349999999999999) || (number >= 370000000000000 && number <= 379999999999999))
        {
            printf("AMEX\n");
        }
        if ((number >= 5100000000000000 && number <= 5599999999999999))
        {
            printf("MASTERCARD\n");
        }
        if ((number >= 4000000000000 && number <= 4999999999999) || (number >= 4000000000000000 && number <= 4999999999999999))
        {
            printf("VISA\n");
        }
    }
}
