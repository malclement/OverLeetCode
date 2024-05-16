#include <vector>
#include <limits>

class Solution
{
public:
    double findMedianSortedArrays(std::vector<int> &nums1, std::vector<int> &nums2)
    {
        int m = nums1.size();
        int n = nums2.size();

        if (m > n)
        {
            std::swap(nums1, nums2);
            std::swap(m, n);
        }

        int totalLength = m + n;
        int halfLength = (totalLength + 1) / 2;

        int low = 0, high = m;
        while (low <= high)
        {
            int partitionNums1 = (low + high) / 2;
            int partitionNums2 = halfLength - partitionNums1;

            int nums1LeftMax = (partitionNums1 == 0) ? std::numeric_limits<int>::min() : nums1[partitionNums1 - 1];
            int nums1RightMin = (partitionNums1 == m) ? std::numeric_limits<int>::max() : nums1[partitionNums1];
            int nums2LeftMax = (partitionNums2 == 0) ? std::numeric_limits<int>::min() : nums2[partitionNums2 - 1];
            int nums2RightMin = (partitionNums2 == n) ? std::numeric_limits<int>::max() : nums2[partitionNums2];

            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin)
            {
                if (totalLength % 2 == 1)
                {
                    return std::max(nums1LeftMax, nums2LeftMax);
                }
                else
                {
                    return (std::max(nums1LeftMax, nums2LeftMax) + std::min(nums1RightMin, nums2RightMin)) / 2.0;
                }
            }
            else if (nums1LeftMax > nums2RightMin)
            {
                high = partitionNums1 - 1;
            }
            else
            {
                low = partitionNums1 + 1;
            }
        }

        throw std::invalid_argument("Input arrays are not sorted.");
    }
};
