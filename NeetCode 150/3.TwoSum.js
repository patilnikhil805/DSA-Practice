/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        const curr = nums[i];
        const need = target - curr

        if (seen.has(need)) {
            return [seen.get(need),i]
        }
        seen.set(curr, i);
    }

    return [-1.-1]
};