# Longest common subsequence

def longestCommonSubsequence(s1,s2):
    if(len(s1) == 0 or len(s2) == 0):
    	return 0
    if(s1[len(s1)-1] == s2[len(s2)-1]):
        return 1+longestCommonSubsequence(s1[:-1],s2[:-1])
    else:
    	return max(longestCommonSubsequence(s1[:-1],s2),longestCommonSubsequence(s1,s2[:-1]))

def main():
	s1 = [1,5,2,6,3,7]
	s2 = [5,6,7,1,2,3]
	print(longestCommonSubsequence(s1,s2))

if __name__ == "__main__":
	main()