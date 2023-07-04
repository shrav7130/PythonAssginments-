# Shravan Surve 

class My_str_exception(Exception):
    pass

class StringOperations:
        def __init__(self,string):
            self.string=string
            
        def str_length(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return len(self.string)
                
        def str_reverse(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return self.string[::-1]
                
        def str_count(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            count = self.string.split()
            return len(count)
                
        def str_upper(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return self.string.upper()
                
        def str_lower(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return self.string.lower()
                
        def str_capitalize(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return self.string.capitalize()
                    
        def is_str_palindrome(self):
            if not self.string:
                raise My_str_exception("You've provided Empty String")
            return self.string==self.string[::-1]
            
            


