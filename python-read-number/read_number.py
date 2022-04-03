
number_list=[1234,1235,1234,5234]
new_number_list=[]
dict_numberList={}


def read_number():
    for n in  number_list:
        for index,num_unique in enumerate(str(n)):
            index+=1
            if num_unique not in new_number_list:
                new_number_list.append((str(index),int(num_unique)))
            

    # print(new_number_list)
    mydict = {key: [key] for key in new_number_list}
    print(mydict)
    # dict_numberList=dict.fromkeys(new_number_list,[])
    # print(dict_numberList)


# a_dictionary = {"a": [1, 2], "b": [3, 4]}
# a_dictionary["b"].append(5)
    






read_number()