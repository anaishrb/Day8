#Exercice 1 

def get_words_from_file(word_list):
    try:
        with open(word_list, 'r') as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print(f"File '{word_list}' not found.")
        return []

import random

def get_random_sentence(word_list, length):
    if length <= 0:
        return "Please enter a valid sentence length (greater than 0)."

    random_sentence = ' '.join(random.choices(word_list, k=length))
    return random_sentence.capitalize() + '.'

def main():
    file_name = word_list

    word_list = get_words_from_file(word_list)
    sentence_length = int(input("Enter the length of the sentence: "))
    random_sentence = get_random_sentence(word_list, sentence_length)

    print("Randomly generated sentence:")
    print(random_sentence)

if __name__ == "__main__":
    main()

#Exercice 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)

salary_value = json_dict['company']['employee']['payable']['salary']
print(f"The salary value is: {salary_value}")

# Add a key called “birth_date” at the same level as the “name” key
json_dict['company']['employee']['birth_date'] = "1990-05-15"  # Replace with the desired birth date

# Save the updated dictionary as JSON to a file
with open('updated_json_file.json', 'w') as file:
    json.dump(json_dict, file, indent=4)

print("JSON data with birth_date added has been saved to 'updated_json_file.json'")