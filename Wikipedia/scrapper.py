import wikipedia, csv

def fetch():


    coops = wikipedia.WikipediaPage('list of utility cooperatives')

    with open('coops.txt', 'w') as file:

        file.writelines(str(coops.section('Electric').encode('utf-8')))

def read(file):

    with open('coops.csv', 'a', newline='') as outfile:

        writer = csv.DictWriter(outfile, fieldnames=['Name'])
        writer.writeheader()

        with open(file, 'r') as file:

            for line in file.readlines():

                writer.writerow({'Name':line.strip()})

if __name__ == '__main__':

    read('coops.txt')