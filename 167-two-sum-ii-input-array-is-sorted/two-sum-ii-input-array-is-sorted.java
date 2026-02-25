class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int I=0;I<numbers.length;I++){
            for(int j=I+1;j<numbers.length;j++){
                if(numbers[I]+numbers[j]==target)
                {
                    return new int[]{I+1, j+1};
                }
            }
        }
        return new int[]{};
    }
}