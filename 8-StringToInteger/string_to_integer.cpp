#include <string>
#include <climits>

class Solution
{
public:
    int myAtoi(std::string s)
    {
        int result = 0;
        int sign = 1;
        int i = 0;
        int n = s.length();

        while (i < n && s[i] == ' ')
        {
            i++;
        }

        if (i < n && (s[i] == '-' || s[i] == '+'))
        {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        while (i < n && isdigit(s[i]))
        {
            int digit = s[i] - '0';
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10))
            {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            result = result * 10 + digit;
            i++;
        }

        return sign * result;
    }
};
