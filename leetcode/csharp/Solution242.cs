// 242.Valid Anagram

public class Solution242
{
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sHash = new Dictionary<char, int>();
        Dictionary<char, int> tHash = new Dictionary<char, int>();

        foreach(char i in s)
        {
            if(!sHash.ContainsKey(i))
            {
                sHash.Add(i, 1);
            }
            else
            {
                sHash[i]++;
            }
        }

        foreach(char i in t)
        {
            if(!tHash.ContainsKey(i))
            {
                tHash.Add(i, 1);
            }
            else
            {
                tHash[i]++;
            }
        }

        if(sHash.Count != tHash.Count)
        {
            return false;
        }

        foreach(KeyValuePair<char, int> i in tHash)
        {
            if(sHash.ContainsKey(i.Key))
            {
                if(sHash[i.Key] != i.Value)
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return true;
    }
}