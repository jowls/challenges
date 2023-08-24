namespace csharp.tests
{
    public class Solution242Fixture
    {
        public Solution242Fixture()
        {
            sol = new Solution242();
        }

        public Solution242 sol { get; private set; }
    }

    public class Solution242Tests : IClassFixture<Solution242Fixture>
    {
        private readonly Solution242Fixture fixture;

        public Solution242Tests(Solution242Fixture fixture)
        {
            this.fixture = fixture;
        }

        [Fact]
        public void Example1()
        {
            string s = "anagram";
            string t = "nagaram";
            bool result = fixture.sol.IsAnagram(s, t);
            Assert.True(result);
        }

        [Fact]
        public void Example2()
        {
            string s = "rat";
            string t = "car";
            bool result = fixture.sol.IsAnagram(s, t);
            Assert.False(result);
        }
    }
}