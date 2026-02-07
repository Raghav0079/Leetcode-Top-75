//Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map < int , int > mp ;

        for (int & x : arr){
            mp[x] ++ ;

        }
        unordered_set <int> st ;

        for (auto & it : mp ){
            int freq = it .second ;

            if(st.find(freq) != st.end())
                return false ;
            st.insert(freq);
        }
        return true;
    }
};

// Time Complexity: O(n) where n is the size of the input array arr. We iterate through the array once to count the occurrences and then iterate through the map to check for unique frequencies.
// Space Complexity: O(n) in the worst case, if all elements in the array are
