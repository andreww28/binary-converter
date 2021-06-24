import os


def main():
    display = Display()
    convert = Convert()

    display.title()
    convert.get_input()


class Display:      #this class is for displaying the text on the  screen

    def title(self):
        title = "TEXT --> BINARY --> TEXT"

        print("*" * 50 + "\n")
        print("*" * 40)
        print(title)
        print("*" * 40 + "\n")
        print("*" * 50 + "\n")

        print("Type [clear] to clear the window")
        print("*" * 40 + "\n")

    def binary_result(self, raw):       #It will display on the screen the binary  from convert class
        print("*" * 30 + "\n")
        print("Binary: \n\t{}".format(raw))
        print("\n" + "*" * 30)
        print()

    def text_result(self, raw):      #It will display on the screen the  text from convert class
        print("*" * 30 + "\n")
        print("Text: \n\t{}".format(raw))
        print("\n" + "*" * 30)
        print()


class Convert:          #This class if for converting the text to binary or binary to text

    display = Display()

    def get_input(self):         
        user_input  = input("Input: ")

        self.check_user_input(user_input)

    def check_user_input(self, user_input):
        valid_chr_for_binary = ['0','1']
        not_valid_letter_count_for_binary = 0
        no_white_line_input = "".join(user_input.split())           #Remove all the whiteline in user input

        if user_input.upper().strip() == "CLEAR":
            os.system('cls')
            self.display.title()
            self.get_input()
        

        for letter in user_input:           #check all the character in user input if it's contain 0 or 1 only or not.
            if letter != " ":               #space or white space is not counted to 'not_valid_letter_count_for_binary'
                if letter not in valid_chr_for_binary:      #if the letter is not 1 or 0, it will increase the 'not_valid_letter_count_for_binary' , it means the it contains letter.
                    not_valid_letter_count_for_binary += 1


        if not_valid_letter_count_for_binary == 0 and len(no_white_line_input) % 8 == 0:        #if the user input is contain 1 and 0 only ,it will convert to text      
            self.To_text(user_input)

        elif not_valid_letter_count_for_binary > 0 or len(no_white_line_input) % 8 != 0:        #if the user input is contain a letter, it will convert to binary
            self.To_binary(user_input)

        
    def binary_text(self, s = " "):         #it will help to convert the user input to binary
    	return [bin(ord(x)) [2:].zfill(8) for x in s]       # it will return the list of converted text to binary, each element is contains 8 bits.

        
    def To_binary(self,input):
        output = ""

        for i in range(len(self.binary_text(input))):       #loop over the list of converted text to binary
            output += self.binary_text(input)[i] + " "      #this will add spaces every element and convert the list into 1 string  

        self.display.binary_result(output)              #it will display the output 
        self.get_input()                        #then ask the user again 


    def To_text(self, input):    
        ascii_sentence = ""
        input = input.strip()       #remove the extra spaces from the start and after the user input
        input = input.split(" ")    #it will make a list of binary ,contains of 8 bits every element.

        for bins in input:
            _chr = int(bins,2)      #convert to ascii
            ascii_chr = chr(_chr)   #convert to letter or character that can human read
            ascii_sentence += ascii_chr         #add all letter

        self.display.text_result(ascii_sentence)
        self.get_input()



if __name__ == '__main__':
    main()
