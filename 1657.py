class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False 

        counts1 = Counter(word1)
        counts2=  Counter(word2)
        return ( counts1.keys() == counts2.keys() ) and (sorted (counts1.values()) == sorted (counts2.values()))
