#include <string>
#include <algorithm>

class Solution
{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        if (s.empty())
            return 0;

        int charIndex[128];
        std::fill_n(charIndex, 128, -1);
        int maxLength = 0;
        int startIndex = 0;

        for (int endIndex = 0; endIndex < s.size(); ++endIndex)
        {
            int charCode = static_cast<int>(s[endIndex]);
            startIndex = std::max(startIndex, charIndex[charCode] + 1);
            charIndex[charCode] = endIndex;
            maxLength = std::max(maxLength, endIndex - startIndex + 1);
        }

        return maxLength;
    }
};
