import sys


def main():
    
    #Read in line arguments
    word = sys.argv[1]
    txt_file = sys.argv[2]

    #Open file 
    with open(txt_file, 'r') as f:

        #Print line if word is in line    
        for line in f:
            if 'cat' in line:
                 print(line)

if __name__ == "__main__":
    main()



