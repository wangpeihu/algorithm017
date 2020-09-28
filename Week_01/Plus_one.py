class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        本人自己解法
        len_digits = len(digits)
        real_digit = 0
        new_digits = []

        for i in range(len_digits):
            real_digit += digits[i] * 10 ** (len_digits - i - 1)   #得到实际数值

        plus_digit = real_digit + 1
        len_new_digits = len(str(plus_digit))
        
        for i in range(len_new_digits):
            new_digits.append(plus_digit // (10 ** (len_new_digits - i - 1)))
            plus_digit -= new_digits[i] * 10 ** (len_new_digits - i - 1)
        
        return new_digits
        '''

        len_digits = len(digits)
        for i in range(len_digits):
            digits[len_digits - 1 - i] += 1
            digits[len_digits - 1 - i] = digits[len_digits - 1 - i] % 10
            if (digits[len_digits - 1 - i] != 0):
                return digits

        digits.append(0)
        digits[0] = 1
        return digits
