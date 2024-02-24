#include <map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;
        
        for (int num : nums)
        {
            if (mySet.count(num) > 0)
            {
                return true;
            }
            else 
            {
                mySet.insert(num);
            }
        }
        return false;
    } 
};