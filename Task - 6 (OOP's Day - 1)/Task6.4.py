import logging as lg
try :
    logging.basicConfig(filename = 'Task6.4.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
except Exception as e :
    lg.basicConfig(filename = 'Task6.4.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
    lg.exception(e)

class function_task :
    '''This is a class which contains some function based
    operations within the functions which it holds'''

    lg.info("WE ARE STATING THE 'function_task' CLASS.")

    def prime_number(self) :
        '''This is a function that gets prime number
        between range of 1 and 1000'''
        try :
            lg.info("We are starting the prime_number function.")
            a = []
            b = []
            for i in range(1,1001) :
                a.append(i)
            for j in range(len(a)) :
                for k in range(2,a[j]) :
                    if a[j] % k == 0 :
                        break
                    else :
                        if a[j] == 1 :
                            continue
                        lg.info('%s\t',a[j])
                        b.append(a[j])
            lg.info('\n')
            lg.info("All the above numbers are prime numbers.")
        except Exception as e :
            lg.exception(e)

    def list_append_replica(self,*a) :
        '''This is a function replica of append function in Python core.'''
        try :
            lg.info("We are starting the list_append_replica function.")
            le = [i for i in a]
            lg.info(le)
            return le
        except Exception as e :
            lg.exception(e)

    def list_extend_replica(self,*a) :
        '''This is a function replica of extend function in Python core.'''
        try :
            lg.info("We are starting the list_extend_replica function.")
            le1 = [j for i in a for j in i if type(i) == str or
            type(i) == tuple or type(i) == list or type(i) == set
            or type(i) == dict]
            lg.info(le1)
            return le1
        except Exception as e :
            lg.exception(e)

    def list_pop_replica(self,*a) :
        '''This is a function replica of pop function in Python core.'''
        try :
            lg.info("We are starting the list_pop_replica function.")
            le2 = [i for i in a]
            lg.info("The list before poping is : %s",le2)
            remove_element = int(input("Enter the index of the element to be removed : "))
            le3 = [le2[i] for i in range(len(le2)) if i != remove_element]
            lg.info("The list after poping is : %s",le3)
            return le3
        except Exception as e :
            lg.exception(e)

    def reading_text_file(self) :
        '''This is a function for reading a sample file.'''
        try :
            f = open('Task6.4_text.txt','r+')
        except Exception as e :
            lg.exception(e)
        finally :
            f = open('Task6.4_text.txt','w+')
            f.write("This is my file creation while applying OOP's concept.")
            f.seek(0)
            lg.info(f.read())
            return f.read()

function_task_obj = function_task()
function_task_obj.prime_number()
function_task_obj.list_append_replica(1,2,34,{'a' : 'Burhan','b' : 'Kapadia'},[1,2,3,4],4 + 6j,True,3.44,False,(1,2,3),{4,5,4,6,7,5})
function_task_obj.list_extend_replica([1,2,3,4],(4,5,6,7),'Burhan',{5,6,7,8,5,4,6},{'a' : 'Burhan','b' : 'Kapadia'})
function_task_obj.list_pop_replica(1,2,34,{'a' : 'Burhan','b' : 'Kapadia'},[1,2,3,4],4 + 6j,True,3.44,False,(1,2,3),{4,5,4,6,7,5})
function_task_obj.reading_text_file()