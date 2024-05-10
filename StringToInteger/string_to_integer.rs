impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut result = 0;
        let mut sign = 1;
        let mut i = 0;
        let n = s.len();

        // Skip leading whitespace
        while i < n && s.chars().nth(i).unwrap() == ' ' {
            i += 1;
        }

        // Check for sign
        if i < n && (s.chars().nth(i).unwrap() == '-' || s.chars().nth(i).unwrap() == '+') {
            sign = if s.chars().nth(i).unwrap() == '-' { -1 } else { 1 };
            i += 1;
        }

        // Read digits
        while i < n && s.chars().nth(i).unwrap().is_digit(10) {
            let digit = s.chars().nth(i).unwrap() as i32 - '0' as i32;
            // Check for overflow
            if result > (i32::MAX - digit) / 10 {
                return if sign == 1 { i32::MAX } else { i32::MIN };
            }
            result = result * 10 + digit;
            i += 1;
        }

        sign * result
    }
}
