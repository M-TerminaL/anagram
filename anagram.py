# This function checks whether two strings are anagrams of each other.

def is_anagram(str1, str2):  
    # بررسی نوع ورودی  
    if not isinstance(str1, str) or not isinstance(str2, str):  
        raise TypeError("ورودی‌ها باید از نوع رشته باشند")  

    # تبدیل به حروف کوچک و حذف فاصله‌ها (اختیاری)  
    str1 = str1.lower().replace(" ", "")  
    str2 = str2.lower().replace(" ", "")  

    # بررسی طول رشته‌ها  
    if len(str1) != len(str2):  
        return False  

    # ایجاد دیکشنری برای شمارش کاراکترها در رشته اول  
    char_counts = {}  
    for char in str1:  
        char_counts[char] = char_counts.get(char, 0) + 1  

    # بررسی و کاهش شمارش کاراکترها در رشته دوم  
    for char in str2:  
        if char in char_counts:  
            char_counts[char] -= 1  
            if char_counts[char] == 0:  
                del char_counts[char]  
        else:  
            return False  

    # اگر دیکشنری خالی باشه، دو رشته آناگرام هستند  
    return not char_counts  
    
