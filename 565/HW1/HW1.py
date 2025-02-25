import hashlib
import itertools
import time
#i am importing string to streamline the character sets (A-Z, a-z,0-9)
import string







def Bruteforce_1():
    complete_char_set = string.ascii_letters + string.digits #this basically does the work for me. rather than writing everything out :)
    pass_len = 14 #given 
    target = "94d9e03c11395841301a7aee967864ec" #given
    start_time = time.time()

    #i am generating all the possible combos now with itertools
    for password in itertools.product(complete_char_set, repeat=pass_len):
        final_pass = "".join(password)

    #now i am going to check the password 
        if Check(final_pass, target):
            elapsed_time = time.time() - start_time
            print("time taken to find password :", elapsed_time)
            return
        
        #conditioning that if the time taken is too much then 
        if time.time() - start_time > 60:
            print("took more than 100 seconds. Stopped program")
            return
        
    #now if theres nothign to be found then i am returning a message
    print("Out of combinations or ran outta time")

'''
Task2: The hash value of her password by MD5 is f593def02f37f3a6d57bcbc9480a3316.
You know the specific password format: <4-UPPER CASE LETTER><3-DIGIT-
NUMBER><4-SMALLER CASE LETTER>
'''

def Bruteforce_2():
    #for second bruteforce 
    #i am implementing same logic but adding in the given format
    target_2 = "f593def02f37f3a6d57bcbc9480a3316"
    UC_length = 4
    LC_length = 4
    Digi_length = 3
    #this time i cannot join all three because we need to use it seperately
    UC = string.ascii_uppercase
    LC = string.ascii_lowercase
    digi = string.digits

    start_time = time.time()

    #this time i will need to create nested for loops to follow the format
    for upper in itertools.product(UC, repeat=UC_length-1):#since we know that the password starts with A, i am reducing the length by 1.
        for num in itertools.product(digi, repeat=Digi_length):
            for lower in itertools.product(LC, repeat=LC_length):
                # now just need to join all three
                final_pass_2 = 'A'+"".join(upper) + "".join(num) + "".join(lower)
                    
                if Check(final_pass_2, target_2):
                    elapsed_time = time.time() - start_time
                    print("time taken to find 2nd password :", elapsed_time)
                    return
                
    #outta combos
    print("Out of combination")

'''
Task3: The hash value of her password by MD5 is bfb2c12706757b8324368de6a365338b.
You know the specific password format: the length is 11 and it includes 7 upper case letters
and the number “1234”. But you don’t know the position of “1234”
'''


def Bruteforce_3():
    target_3 = "bfb2c12706757b8324368de6a365338b"
    UC = string.ascii_uppercase
    UC_length = 7
    digits = "1234"


    start_time = time.time()


    for upper in itertools.product(UC, repeat=UC_length-1):
        #since we know that the password starts with A 
        #i am going to reduce the length and 
        # as there would only be 8
        for i in range(8):
            #this time i will need to create nested for loops to follow the format
            final_pass_3 = 'A'+ "".join(upper)[:i] + digits + "".join(upper)[i:]

            if Check(final_pass_3, target_3):
                elapsed_time = time.time() - start_time
                print("time taken to find 3rd password :", elapsed_time)
                return
            
    print("out of combinations")

'''
Task4: Please compare the attacking time of above task2 and task3 and discuss the difficulty
level to attack them (which one is the easiest and which one is the hardest and reason). Hint:
the analysis can include the theoretical search space and empirical attacking time of task2 and
task3
'''
def Compare():
    # to compare tasks 2 and 3 we will simply compare the time taken for each task.
    second = Bruteforce_2()
    third = Bruteforce_3()
    print("time taken for task 2 is", second)
    print("time taken for task 3 is", third)

    if third < second:
        print("task 2 is easier by time taken: " , second)
    else:
        print("task 3 is easier by time taken", third)

''' 
The dificulties of both the tasks can be compared by the time. I can see that 2nd is taking
less time than 3rd.

there is a reason to it. 

As we see in the 2nd task, the hash value convertes to AAAA123dddd, which does not take as many iterations
because the value that is found is concerring till the 4th character. After the digits, 
the value 'd' is concerred until the end of string, which takes less iteration since the other possibilities 
are eliminate.

same goes for 3rd since there are 7 upper case with a random position fixed number, it takes a wee bit
longer to reach to value that matches the hash. as it starts with A, it also 
tries different posiiton before exploring the correct one, that takes iterations and consumes time.

'''




def DictionaryAttack():
    target_5 = "94d9e03c11395841301a7aee967864ec"
    dic_file = "dictionary.txt" 
    words = file.readlines()

    start_time = time.time()


    #for this task i am goint to use try and catch to handle the file reading.
    try:
        #opening the file in read mode
        with open(dic_file, "r") as file:
            #reading the file
            for i in words:
                i = i.strip()#stripping to remove news lines
                #removing the new line character to go through the next line
                #checking the password 
                if Check(i, target_5):
                    elapsed_time = time.time() - start_time
                    print("time taken to find 5th password :", elapsed_time)
                    print("password is", i)
                    return
    except FileNotFoundError:
        print("file not found")
        return




def Check(string, hash_target):  # Change the hash value for different tasks
    #changed the variable. hexdigesting the guessed password right away
    guessed_pwd = hashlib.md5(string.encode()).hexdigest()
    
    #changing the if condition
    if guessed_pwd== hash_target:
        # for each task, you need to change the hash value of password
        print("You succeed and password is", string)
        return True
    else:
        return False

#Bruteforce_1()
# Bruteforce_2()
Bruteforce_3()
# Compare()
# DictionaryAttack()
