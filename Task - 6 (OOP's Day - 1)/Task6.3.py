import logging as lg
try :
    logging.basicConfig(filename = 'Task6.3.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
except Exception as e :
    lg.basicConfig(filename = 'Task6.3.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
    lg.exception(e)

class dict_set_tuple_list_task :
    '''This is a class which contains some list,tuples,
     sets and dictionary based operations within the
     functions which it holds.'''

    lg.info("This is start of dict_set_tuple_list class.")

    def __init__(self,li2) :
        try :
            lg.info("This is the init constructor for the dict_set_tuple_task class.")
            self.li3 = li2
            lg.info("We have recieved the data as a list  :%s",self.li3)
            if len(self.li3) == 0 :
                raise Exception('Empty list!')
        except Exception as e :
            lg.exception(e)

    def extract_list_in_list(self) :
        '''This functions extract list from the user
        based input.'''
        try :
            list2 = []
            lg.info('We are finding list within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == list :
                    lg.info(i)
                    list2.append(i)
                elif type(i) == tuple or type(i) == set :
                    for j in i:
                        if type(j) == list:
                            lg.info(j)
                            list2.append(j)
                elif type(i) == dict :
                    for j in i :
                        if type(i[j]) == list :
                            lg.info(i[j])
                            list2.append(i[j])
            return list2
        except Exception as e :
            lg.exception(e)

    def extract_dictionary(self) :
        '''This function extracts dictionary from
        the user based input.'''
        try :
            list3 = []
            lg.info('We are finding all the dictionaries within a list : %s', self.li3)
            for i in self.li3 :
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if type(j) == dict :
                            lg.info(j)
                            list3.append(j)
                elif type(i) == dict :
                    lg.info(i)
                    list3.append(i)
            return list3
        except Exception as e :
            lg.exception(e)

    def extract_tuples(self) :
        '''This function extracts tuples from user
        based input.'''
        try :
            list4 = []
            lg.info('We are finding tuples within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == tuple :
                    lg.info(i)
                    list4.append(i)
                elif type(i) == list or type(i) == set :
                    for j in i :
                        if type(j) == tuple :
                            lg.info(j)
                            list4.append(j)
                elif type(i) == dict :
                    for k,v in i.items() :
                        if type(k) == tuple :
                            lg.info(k)
                            list4.append(k)
                        if type(v) == tuple :
                            lg.info(v)
                            list4.append(v)
            return list4
        except Exception as e :
            lg.exception(e)

    def int_in_list_and_sum(self) :
        '''This function extracts all the integer values
        and perform sum of it from the user based input.'''
        try :
            list5 = []
            sum = 0
            lg.info('We are finding numerical values within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == int:
                    lg.info(i)
                    sum = sum + i
                    list5.append(i)
                elif type(i) == list or type(i) == set or type(i) == tuple :
                    for j in i:
                        if type(j) == int:
                            lg.info(j)
                            sum = sum + j
                            list5.append(j)
                elif type(i) == dict :
                    for k,v in i.items():
                        if type(k) == int:
                            lg.info(k)
                            sum = sum + k
                            list5.append(k)
                        if type(v) == int:
                            lg.info(v)
                            sum = sum + v
                            list5.append(v)
            lg.info(sum)
            return list5,sum
        except Exception as e:
            lg.exception(e)

    def odd_int_in_list(self) :
        '''This function extracts all the odd integer
        values from the user based input.'''
        try :
            list6 = []
            lg.info('We are finding odd numerical values within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == int and i % 2 != 0 :
                    lg.info(i)
                    list6.append(i)
                elif type(i) == list or type(i) == set or type(i) == tuple :
                    for j in i:
                        if type(j) == int and j % 2 != 0 :
                            lg.info(j)
                            list6.append(j)
                elif type(i) == dict :
                    for k,v in i.items():
                        if type(k) == int and k % 2 != 0 :
                            lg.info(k)
                            list6.append(k)
                        if type(v) == int and v % 2 != 0 :
                            lg.info(v)
                            list6.append(v)
            return list6
        except Exception as e:
            lg.exception(e)

    def extract_ineuron(self) :
        '''This is function extracts string : 'ineuron'
        from the user based input.'''
        try :
            list7 = []
            lg.info('We are finding out ineuron within a list : %s', self.li3)
            for i in self.li3:
                if i == 'ineuron' :
                    lg.info(i)
                    list7.append(i)
                elif type(i) == list or type(i) == set or type(i) == tuple :
                    for j in i:
                        if j == 'ineuron' :
                            lg.info(j)
                            list7.append(j)
                elif type(i) == dict :
                    for k,v in i.items():
                        if k == 'inueron' :
                            lg.info(k)
                            list7.append(k)
                        if v == 'ineuron' :
                            lg.info(v)
                            list7.append(v)
            return list7
        except Exception as e:
            lg.exception(e)

    def count_of_elements(self) :
        '''This function calculates count of each
        element entered by the user.'''
        try :
            list8 = []
            lg.info('We are finding out count of elements within a list : %s', self.li3)
            for i in self.li3 :
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if type(j) == int or type(j) == str :
                            list8.append(j)
                elif i == int or i == str :
                    list8.append(i)
                elif type(i) == dict :
                    for k,v in i.items() :
                        if type(k) == int or type(k) == str :
                            list8.append(k)
                        if type(v) == int or type(v) == str :
                            list8.append(v)
            for n in set(list8) :
                lg.info('%s : %s',n,list8.count(n))
            return n,list8.count(n)
        except Exception as e :
            lg.exception(e)

    def count_of_keys_dict(self) :
        '''This function calculates the count of
        keys present in the dictionary given by
        the user.'''
        try :
            list9 = []
            lg.info("We are finding out count of keys for dictionary within a list : %s",self.li3)
            for i in self.li3 :
               if type(i) == dict :
                    lg.info(len(i.keys()))
                    list9.append(len(i.keys()))
            return list9
        except Exception as e :
            lg.exception(e)

    def string_data_list(self) :
        '''This fucntion extracts all the string given
        by the user as an input.'''
        try :
            list10 = []
            lg.info('We are finding string data within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == str :
                    lg.info(i)
                    list10.append(i)
                elif type(i) == list or type(i) == set or type(i) == tuple :
                    for j in i:
                        if type(j) == str :
                            lg.info(j)
                            list10.append(j)
                elif type(i) == dict :
                    for k,v in i.items():
                        if type(k) == str :
                            lg.info(k)
                            list10.append(k)
                        if type(v) == str :
                            lg.info(v)
                            list10.append(v)
            return list10
        except Exception as e:
            lg.exception(e)

    def alphanumeric_list(self) :
        '''This function extracts alphanumeric data
        given by user as an input.'''
        try :
            list11 = []
            lg.info('We are finding alphanumeric data within a list : %s', self.li3)
            for i in self.li3:
                if type(i) == str and i.isalnum() :
                    lg.info(i)
                    list11.append(i)
                elif type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == str and j.isalnum() :
                            lg.info(j)
                            list11.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str and k.isalnum() :
                            lg.info(k)
                            list11.append(k)
                        if type(v) == str and v.isalnum() :
                            lg.info(v)
                            list11.append(v)
            return list11
        except Exception as e:
            lg.exception(e)

    def multiply_elements_list(self) :
        '''This functions give product of all the
        integer elements entered by the user as an
        input.'''
        try :
            list12 = []
            m1 = 1
            m2 = 1
            m3 = 1
            m4 = 1
            lg.info('We are finding multiplication of numeric data  within a list : %s', self.li3)
            for i in self.li3:
                m1 = 1
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if type(j) == int :
                            m1 = m1 * j
                    list12.append(m1)
                    lg.info(m1)
                elif type(i) == dict :
                    for k, v in i.items():
                        if type(k) == int :
                            m2 = m2 * k
                        if type(v) == int :
                            m3 = m3 * v
                    list12.append(m2)
                    list12.append(m3)
                    lg.info(m2)
                    lg.info(m3)
                else :
                    if type(i) == int :
                        m4 = m4 * i
                    list12.append(m4)
                    lg.info(m4)
            return list12
        except Exception as e:
            lg.exception(e)

    def unwrape_list(self) :
        '''This function unwrap the given collection
        given by the user as an input.'''
        try :
            list13 = []
            lg.info("We are unwrapping the list : %s",self.li3)
            for i in self.li3 :
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        lg.info(j)
                        list13.append(j)
                elif type(i) == dict :
                    for k,v in i.items() :
                        lg.info(k)
                        lg.info(v)
                        list13.append(k)
                        list13.append(v)
                else :
                    list13.append(i)
                    lg.info(i)
            return list13
        except Exception as e :
            lg.exception(e)

list_tuple_dict_set_obj = dict_set_tuple_list_task([[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : 'sudh','k2' : 'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']])
list_tuple_dict_set_obj.extract_list_in_list()
list_tuple_dict_set_obj.extract_tuples()
list_tuple_dict_set_obj.extract_dictionary()
list_tuple_dict_set_obj.int_in_list_and_sum()
list_tuple_dict_set_obj.alphanumeric_list()
list_tuple_dict_set_obj.count_of_elements()
list_tuple_dict_set_obj.count_of_keys_dict()
list_tuple_dict_set_obj.extract_ineuron()
list_tuple_dict_set_obj.multiply_elements_list()
list_tuple_dict_set_obj.odd_int_in_list()
list_tuple_dict_set_obj.string_data_list()
list_tuple_dict_set_obj.unwrape_list()