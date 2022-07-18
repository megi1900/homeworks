


def books(library,book_name):

    new_list=[]
    for name in range(len(library)):
        if book_name in library[name]:
            new_list.append(library[name])
    return new_list


print(books(["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "The Adventures of Sherlock Holmes", "The Chamber"], "Harry Potter"))



    
