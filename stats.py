def get_num_words(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return len(file_content.split())

def character_counter(file_path):
    with open(file_path) as f:
        file_content = f.read()
    character_count = dict()
    

    for c in file_content:
        letter = c.lower()
        if letter.isalpha():
            character_count[letter] = character_count.get(letter, 0) + 1
    
    character_count_list = []
    for key, value in character_count.items():
        new_item = {"char":key,"num":value}
        character_count_list.append(new_item)
    
    def sort_on(items):
        return items["num"]
    character_count_list.sort(reverse=True,key=sort_on)


    for key in character_count_list:
        print(f"{key["char"]}: {key["num"]}")

    


