impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();

        for i in 0..n {
            for j in 1..n {
                if i != j {
                    if nums.get(i).unwrap() + nums.get(j).unwrap() == target {
                        return vec![i as i32, j as i32];
                    }
                }
            }
        }

        return vec![-1, -1];
    }
}