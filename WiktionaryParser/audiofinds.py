import csv
from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

def audiofind(file):

    with open('urls.csv', 'a', newline='') as outfile:

        headers = ['URL', 'Category']
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()

        with open(file, 'r') as infile:

            reader = csv.reader(infile, delimiter=',')

            for row in reader:

                print('Fetching', reader.line_num)

                audio = ''
                category = ''

                try:

                    word = parser.fetch(row[0])

                    audio = 'https:' + word[0]['pronunciations']['audio'][0]
                    category = word[0]['definitions'][0]['partOfSpeech']

                except:

                    pass

                finally:

                    writer.writerow({'URL':audio, 'Category': category})

if __name__ == '__main__':

    audiofind('definition.csv')