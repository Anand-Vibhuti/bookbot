def number_of_words(string):
    
    words=string.split()
    return len(words)
def character_count(string):
            
    return_dictionary={}
    for char in string:
        char=char.lower()
        if char in return_dictionary:
            return_dictionary[char]=return_dictionary[char]+1
        else:
            return_dictionary[char]=1
    return return_dictionary
def sorted_dictionary(dictionary):
    array_of_dictionaries=[]
    for key in dictionary:
        array_of_dictionaries.append({"char":key,"count":dictionary[key]})
    def sort_on(dictionary):
        return dictionary["count"]
    array_of_dictionaries.sort(reverse=True,key=sort_on)
    return array_of_dictionaries 