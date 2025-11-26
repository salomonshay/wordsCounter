import sys
import string

def words_from_file(file_name):
        with open(file_name, "r") as file:
            text = file.read()

        text = text.lower()
        words_list = text.split()

        clean_list = []

        for word in words_list:
            clean_list.append(word.strip(string.punctuation))

        return clean_list

def main(file_name , top_words):
    words = words_from_file(file_name)
    word_dict = dict()

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] =1
    sorted_words = sorted(word_dict.items(),key=lambda x:x[1] , reverse=True )

    for i in range (0,top_words):
        print(sorted_words[i])



if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        try:
            top_words = int(sys.argv[2])
            if top_words > 0:
                main(file_name,top_words)
            else:
                print("Error: top_words has to be positive.")
        except:
            if not sys.argv[2].isdigit():
                print("Error: top_words has to be a num.")
            else:
                print("Error: The file- " + file_name + " does not exist!")
    else:
        print("Usage: python {0} <file_name> <top_words>".format(sys.argv[0]))