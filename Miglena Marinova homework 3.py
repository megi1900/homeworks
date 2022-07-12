print("zad.1")

def is_anagram(fst_word,snd_word):

    fst_word=fst_word.lower()
    snd_word=snd_word.lower()

    if(len(fst_word)==len(snd_word)):
        fst_sorted=sorted(fst_word)
        snd_sorted=sorted(snd_word)


        if (fst_sorted==snd_sorted):
            return True
        else:
            return False
print(is_anagram("BEARD","BeaRD"))  
print(is_anagram("TOP_CORDER","COTO_PRODE"))                
print(is_anagram("LISTEN","silent"))



print("\n zad.2")

def count_words(arr):

    words_list=dict()

    for word in arr:
        if word not in words_list:
            words_list[word]=1
        else:
            words_list[word]+=1
    return words_list
print(count_words(["apple", "banana", "apple", "pie"])) 



print("\n zad.3")

def nan_expand(num):

    word=" "
    if num==0:
        return ' " " '
    for i in range(num):
      
        word+="Not a "
    word+="Nan"
    return word

print(nan_expand(0)) 
print(nan_expand(3)) 




print("\n zad.5")


def sum_of_numbers(st):
    num = 0
    sum = 0
    for i in st:
        if i.isdigit():
            num = num*10+int(i)
        else:
            sum = sum+num
            num = 0
    return sum+num
print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))




