import csv
from wiktionaryparser import WiktionaryParser

# -*- coding: utf-8 -*-

parser = WiktionaryParser()

def missing(file):

    with open('finaldef.csv', 'a', newline='') as outfile:

        headers = ['Word',  'Definition']
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()

        with open(file, 'r') as infile:

            reader = csv.reader(infile, delimiter=',')

            for row in reader:

                #print('Defining', reader.line_num)

                try:

                    if row[0][0].isupper() == True:

                        definition = ''

                    else:

                        if len(row[1]) == 0:

                            word = parser.fetch(row[0])
                            definition = word[0]['definitions'][0]['text'].strip().encode('utf-8')


                        else:

                            definition = row[1]

                except:

                    pass

                finally:

                    writer.writerow({'Word':row[0], 'Definition':definition})
                    definition=''

if __name__ == '__main__':

    missing('definition.csv')