class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            sWord = ''.join(sorted(word))
            anagrams[sWord] = anagrams.get(sWord, []) + [word]

        ans = []
        for key, words in anagrams.items():
            ans.append(words)

        return ans