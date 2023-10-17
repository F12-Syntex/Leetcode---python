import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> cache = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int required = target - nums[i];
            if(cache.containsKey(required)) {
            	return new int[] {cache.get(required), i};
            }
            cache.put(nums[i], i);
        }

        return new int[]{0, 0};
    }
}