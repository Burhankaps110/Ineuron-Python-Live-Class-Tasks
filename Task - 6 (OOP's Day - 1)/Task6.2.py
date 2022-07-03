import logging as lg
try :
    logging.basicConfig(filename = 'Task6.2.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
except Exception as e :
    lg.basicConfig(filename = 'Task6.2.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
    lg.exception(e)

lg.info ("We are now starting with list task")

class list_task :
    '''This is a class which contains some list based
    operations within the functions which it holds.'''

    lg.info("This is list_task class.")

    def __init__(self,li) :
        lg.info("This is the init constructor for the list_task class.")
        try :
            self.li1 = li
            lg.info('We have received the data : %s',self.li1)
            if len(self.li1) == 0 :
                raise Exception('empty list')
        except Exception as e :
            lg.exception(e)

    def list_reverse(self) :
        '''We are performing reverse of the list given
        by the user through index operation.''''
        try:
            lg.info('We are reversing the list : %s', self.li1)
            list_rev = self.li1[::-1]
            lg.info("The list after reversing is : %s",list_rev)
            return list_rev
        except Exception as e:
            lg.exception(e)

    def extract_234(self) :
        '''We are extracting 234 value within the list by this
        function.'''
        try :
            list3 = []
            for i in self.li1 :
                if type(i) == tuple :
                    lg.info("We are looking for 234 from tuple inside the list : %s", self.li1)
                    for j in i :
                        if j == 234 :
                            lg.info(j)
                            list3.append(j)
                elif type(i) == dict :
                    lg.info("We are looking for 234 from dictionary inside the list : %s", self.li1)
                    for k,v in i.items() :
                        if k == 234 :
                            lg.info(k)
                            list3.append(k)
                        if v == 234 :
                            lg.info(v)
                            list3.append(v)
                elif i == 234 :
                    lg.info(i)
                    list3.append(i)
            return list3
        except Exception as e :
            lg.exception(e)

    def extract_456(self) :
        '''We are extracting 456 within the list by this
        function.'''
        try :
            list4 = []
            lg.info('We are looking for an 456 inside list : %s', self.li1)
            for i in self.li1 :
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if j == 456 :
                            lg.info(j)
                            list4.append(j)
                elif type(i) == dict :
                    lg.info("We are looking for 456 from dictionary inside the list : %s", self.li1)
                    for k,v in i.items() :
                        if k == 456 :
                            lg.info(k)
                            list4.append(k)
                        if v == 456 :
                            lg.info(v)
                            list4.append(v)
                elif i == 456 :
                    lg.info(i)
                    list4.append(i)
            return list4
        except Exception as e :
            lg.exception(e)

    def extract_list_in_list(self) :
        '''We are extracting nested list from the list in
        this function.'''
        try :
            list2 = []
            lg.info('We are finding list within a list : %s',self.li1)
            for i in self.li1 :
                if type(i) == list or type(i) == tuple :
                    for j in i :
                        if type(j) == list :
                            lg.info(j)
                            list2.append(j)
                    lg.info(i)
                    list2.append(i)
                elif type(i) == dict :
                    for j in i :
                        if type(i[j]) == list :
                            lg.info(i[j])
                            list2.append(i[j])
            return list2
        except Exception as e :
            lg.exception(e)

    def extract_sudh(self) :
        '''We are extracting string : 'sudh' from the list
        in this function.'''
        try :
            list5 = []
            lg.info('We are looking for sudh inside list : %s', self.li1)
            for i in self.li1 :
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if j == 'sudh' :
                            lg.info(j)
                            list5.append(j)
                elif type(i) == dict :
                    lg.info("We are looking for sudh from dictionary inside the list : %s", self.li1)
                    for k,v in i.items() :
                        if k == 'sudh' :
                            lg.info(k)
                            list4.append(k)
                        if v == 'sudh' :
                            lg.info(v)
                            list5.append(v)
                elif i == 'sudh' :
                    lg.info(i)
                    list5.append(i)
            return list5
        except Exception as e :
            lg.exception(e)

    def extract_keys(self) :
        '''We are extracting all the keys from all the
        dictionaries from the list in this function.'''
        try :
            lg.info("We are trying to extract all keys in a dictionary from list : %s",self.li1)
            list6 = []
            for i in self.li1 :
                if type(i) == dict :
                    for j in i :
                        lg.info(j)
                        list6.append(j)
            return list6
        except Exception as e :
            lg.exception(e)

    def extract_values(self) :
        '''We are extracting all the values from all the
        dictionaries from the list in this function.'''
        try :
            lg.info("We are trying to extract all values in a dictionary from list : %s",self.li1)
            list7 = []
            for i in self.li1 :
                if type(i) == dict :
                    for j in i :
                        lg.info(i[j])
                        list7.append(i[j])
            return list7
        except Exception as e :
            lg.exception(e)

list_obj = list_task([3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6),{"key1" :"sudh",234:[23,45,656]}])
list_obj.list_reverse()
list_obj.extract_234()
list_obj.extract_456()
list_obj.extract_list_in_list()
list_obj.extract_sudh()
list_obj.extract_keys()
list_obj.extract_values()