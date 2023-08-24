// 1768. Merge Strings Alternately
//
// You are given two strings word1 and word2. Merge the strings by
// adding letters in alternating order, starting with word1. If a string
// is longer than the other, append the additional letters onto the end
// of the merged string. Return the merged string.

public class Solution1768
{
    public string MergeAlternately(string word1, string word2) {
        string result = "";
        int w1l = word1.Length;
        int w2l = word2.Length;
        int merge_max = 0;
        bool w1long = false;
        int end = 0;
        if (w1l >= w2l)
        {
            merge_max = w2l;
            w1long = true;
            end = w1l;
        }
        else
        {
            merge_max = w1l;
            end = w2l;
        }
        for (int i = 0; i < end; i++)
        {
            if (i < merge_max)
            {
                result += word1[i];
                result += word2[i];
            }
            else
            {
                if (w1long == true)
                {
                    result += word1[i];
                }
                else
                {
                    result += word2[i];
                }
            }
        }
        return result;
    }
}