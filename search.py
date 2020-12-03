import sys

def main(argv):
  search_string = argv[0]
  file_name = argv[1]

  with open(file_name) as file:
    line = file.readline()
    while line:
      if search_string in line:
        print(line.strip())
      line = file.readline()

if __name__ == "__main__":
  main(sys.argv[1:])