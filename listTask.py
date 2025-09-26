myListOfStrings = ["abc5def6", "ghi8jkl9", "mno1pqr0", "stu1vwx1", "yza1bcd2"]

def largest_digit_sum(myListOfStrings):
    largest_sum = 0

    for s in myListOfStrings:

        digit_sum = sum(int(char) for char in s if char.isdigit())
        largest_sum = max(largest_sum, digit_sum)
        return largest_sum
        
   result  = largest_digit_sum(myListOfStrings)
   print(result)
