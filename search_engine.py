"""
Author  : Vivek Shinde
Date    : 09/06/2020
purpose : Practice problem solving
code    : search engine with maximum result found

"""

def same_words(sentence1, sentence2):
    score = 0
    for words1 in sentence1.split():
        for words2 in sentence2.split():
            # print(f'matching {words1} with {words2}')
            if words1.lower() == words2.lower():
                score = score+1
    # it returns how many words matched
    return score

if __name__ == '__main__':
    sentences = ["This is good", "python is good", "python not python snake"]

    user_query = input("Please enter your query :")

    # to store the list of scores in below list
    my_list = []

    for sentence in sentences:
        x = [same_words(user_query, sentence)]
        for i in x:
            my_list.append(i)
    # print(my_list)

    for sent_score in my_list:
        y = sorted(zip(my_list, sentences), reverse=True)
    # print(y)

    # To print total result found, i used this for loop
    result = 0
    for jelly in my_list:
        if jelly !=0:
            result = result+1
    print(f'\n{result} result found!')


    for key, value in y:
        if key != 0:
            print(f"\"{value}\" : with a score of {key}")



