import random
import string

class password:
    
    def generate_password(self,length):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation  
        all_chars = lower + upper + digits + special_chars
        password = ''.join(random.choices(all_chars, k=length))
        return password
    
    def user_input(self):
        while True:
            try:
                length = int(input("Enter the desired length of the password: "))
                if length <= 0:
                    print("Please enter a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
        password = self.generate_password(length)
        print(f"Generated password of length {length} : {password}")

def main():
    obj=password()
    obj.user_input()
    
if __name__=='__main__':
    main()
