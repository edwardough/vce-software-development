def main():
    while True:
        temp = input("Enter a number [0-1,000,000] (Q to quit) >> ")
        if temp == '': # check something is actually there
            print("You didn't enter anything.")
        elif temp == 'Q':
            break
        else:
            try:
                temp = int(temp) # check it's an integer via 'try and except'
                if temp in range(0,1000000):
                    print('Correct input')
                else:
                    print('Number outside specified range.')
            except ValueError:
                print("Integer conversion failed.")

if __name__ == '__main__':
    main()
    input("Enter to end")

# Sometimes, like in SAC1, you'll import python files/libraries.
# When that happens, the code is actually executed.
# The if statement above checks that the file we're using is being run directly.
# So, in case you import this file into another project, the code won't run.
# Find out more by watching Mr Wilson demonstrate.
# If you're not at school, check this out https://www.youtube.com/watch?v=sugvnHA7ElY

        
