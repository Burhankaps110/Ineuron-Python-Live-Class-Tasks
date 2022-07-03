import logging as lg
try :
    logging.basicConfig(filename = 'Task6.1.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
except Exception as e :
    lg.basicConfig(filename = 'Task6.1.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
    lg.exception(e)

class string_task :
    '''This is a class which contains some string based
    operations within the functions which it holds.'''

    lg.info("This is string_task class.")

    def __init__(self,string) :
        lg.info("This is the init constructor for the string_task class.")
        try :
            self.string1 = string
            lg.info('We have received the data : %s',self.string1)
            if len(self.string1) == 0 :
                raise Exception('empty string')
        except Exception as e :
            lg.exception(e)

    def string_slicing(self) :
        '''We are performing slicing of the input string
        given by the user.'''
        try :
            lg.info('We are slicing the string : %s',self.string1)
            string_slice = self.string1[:300:3]
            lg.info("The sliced string is : %s",string_slice)
            return string_slice
        except Exception as e :
            lg.exception(e)

    def string_reverse(self) :
        '''We are performing reverse of the string given
        by the user through index operation.'''
        try :
            lg.info('We are reversing the string : %s',self.string1)
            string_rev = self.string1[::-1]
            return string_rev
        except Exception as e :
            lg.exception(e)

    def string_operation1(self) :
        '''We are performing case conversion of the string
        and then split.'''
        try :
            lg.info('We are changing the string : %s into upper-case and then performing split operation.')
            string_upper = self.string1.upper()
            lg.info("The upper-case conversion is : %s",string_upper)
            string_spilt = self.string1.split()
            lg.info("The splitted upper-case string is : %s",string_spilt)
            return string_upper, string_spilt
        except Exception as e :
            lg.exception(e)

    def string_operation2(self) :
        '''We are performing lower case conversion of the
        user input string'''
        try :
            lg.info('We are converting the string : %s into lower case')
            string_lower = self.string1.lower()
            lg.info("The lower case string is : %s",string_lower)
            return string_lower
        except Exception as e :
            lg.exception(e)

    def string_operation3(self) :
        '''We are capitalizing the first letter
        of the user input string.'''
        try :
            lg.info('We are Capitalizing the string : %s',self.string1)
            string_capitalize = self.string1.capitalize()
            lg.info("The capitalized string is : %s",string_capitalize)
            return string_capitalize
        except Exception as e :
            lg.exception(e)

string_obj = string_task("this is My first Python programming class and I am learNING python string and its function")
string_obj.string_slicing()
string_obj.string_reverse()
string_obj.string_operation1()
string_obj.string_operation2()
string_obj.string_operation3()