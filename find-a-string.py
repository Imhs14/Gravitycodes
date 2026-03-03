def count_substring(string, sub_string):
    count = 0
    # Looping through the string and stopping , when we cannot fit the substring anymore in string 
    # 10 str , 3 sstr so u have to stop at 7 index , if you go further there will be no characters to search in the str.
    for i in range(len(string) - len(sub_string) + 1):
        # Slice the string from the current index 'i' to 'i + length of substring'
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    """
    ABCDCDC
    CDC
    2
    """

    
    """
    Loop Turn (i) | Slice Calculation [i : i+3] |  Resulting Chunk	 |  Is it "CDC"?
        0	            string[0:3]	                 "ABC"	             No
        1	            string[1:4]	                 "BCD"	             No
        2	            string[2:5]	                 "CDC"	             YES! (Count +1)
        3	            string[3:6]	                 "DCD"      	     No
        4	            string[4:7]	                 "CDC"	             YES! (Count +1)
    """