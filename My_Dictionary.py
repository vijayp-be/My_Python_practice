'''Dictionary of words
Create a program that manages a dictionary of word meanings. The program 
should allow users to perform the following actions:
1. Add a Word: Allow users to add new words along with their meanings to the 
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the 
dictionary.
3. Display All Words: Provide an option to display all words and their meanings 
currently stored in the dictionary.
4. Update Meaning: Implement a feature to update the meaning of an existing 
word in the dictionary. After updating, display the updated meaning.
5. Delete Word: Implement a feature to delete a word and its meaning from the 
dictionary. Confirm the deletion and handle cases where the word doesn't 
exist.
Ensure the program handles invalid inputs gracefully. Use a while loop to keep the 
program running until the user chooses to exit.'''

dictionary = {}
while True:
    print("welcome to My Dictionary...")
    print("1. Add a word")
    print("2. search for a meaning")
    print("3. display all words")
    print("4. update Meaning")
    print("5. Delete word")
    print("6. Exit")
    
    choice = input('Enter your choice: ')
    
    if choice == "1":
        word = input("Enter a word: ").lower()
        meaning= input("Enter a meaning: ").lower()
        dictionary[word] = meaning
        print('\nword added sucessfully.. \n')
        
    elif choice == "2":
        word = input('enter a word to search: ').lower()
        if word in dictionary:
            print('Meaning: ', dictionary.get(word), '\n')
        else:
            print("sorry..! word is not present in the dictionary..\n")
    
    elif choice == "3":
        if dictionary:
            print('words and their meanings')
            for word, meaning in dictionary.items():
                print(f"{word} : {meaning}")
        else:
            print("the dictionalry is empty \n")
            
    elif choice == "4":
        word = input("Enter a word to update the meaning: ").lower()
        if word in dictionary:
            new_meaning = input("enter a meaning to update: ")
            dictionary[word] = new_meaning
            print("meaning updated sucessfull")
            print("updated meaning", dictionary[word], '\n')
        else:
            print("the word you entered is not present in dictionary \n")
            
    elif choice == "5":
        word = input("enter the word you want to delete from the dictionary: ")
        if word in dictionary:
            dictionary.pop(word)
            print(f"the word {word} is deleted sucessfully \n")
        else:
            print("the word is not present in the dictionary \n")
    
    elif choice == "6":
        print("Exiting program..")
        break
    
        
            
            