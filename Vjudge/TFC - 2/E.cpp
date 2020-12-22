#include<stdio.h>
#include<string.h>

int main()
{
    int t, x;
    scanf("%d", &t);
    for (x = 0; x < t; x++)
    {
        char s[8000];
        int k;
        scanf("%s %d", &s, &k);
        int c = 0;
        int i, j;

        for (i = 0; i < strlen(s); i++)
        {
            int bound = 0, d = 0, letter[26];
            for (int l = 0; l < 26; l++)
                letter[l] = 0;

            for (j = i; j < strlen(s); j++)
            {
                if (letter[(int)s[j] - 'a']==0)
                    d += 1;
                letter[(int)s[j] - 'a'] += 1;
                if (letter[(int)s[j] - 'a'] > bound)
                    bound = letter[(int)s[j] - 'a'];
                if (d>= k && bound *d == j - i + 1)
                    c += 1;
            }
        }
        printf("%d\n", c);
    }
    return 0;
}