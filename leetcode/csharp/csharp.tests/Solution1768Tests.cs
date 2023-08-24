namespace csharp.tests
{
    public class Solution1768Fixture
    {
        public Solution1768Fixture()
        {
            sol = new Solution1768();
        }

        public Solution1768 sol { get; private set; }
    }

    public class Solution1768Tests : IClassFixture<Solution1768Fixture>
    {
        private readonly Solution1768Fixture fixture;

        public Solution1768Tests(Solution1768Fixture fixture)
        {
            this.fixture = fixture;
        }

        [Fact]
        public void Example1()
        {
            string word1 = "abc";
            string word2 = "pqr";
            string output = "apbqcr";
            string result = fixture.sol.MergeAlternately(word1, word2);
            Assert.Equal(output, result);
        }

        [Fact]
        public void Example2()
        {
            string word1 = "ab";
            string word2 = "pqrs";
            string output = "apbqrs";
            string result = fixture.sol.MergeAlternately(word1, word2);
            Assert.Equal(output, result);
        }

        [Fact]
        public void Example3()
        {
            string word1 = "abcd";
            string word2 = "pq";
            string output = "apbqcd";
            string result = fixture.sol.MergeAlternately(word1, word2);
            Assert.Equal(output, result);
        }
    }
}