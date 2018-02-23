from simplewiktionary import SimpleWiktionary
import csv

parser = SimpleWiktionary()

with open('definition.csv', 'a') as outfile:

    headers = ['Word', 'Definition']
    writer = csv.DictWriter(outfile, fieldnames=headers)

    writer.writeheader()

    with open('words.csv', 'r') as infile:

        reader = csv.reader(infile, delimiter=',')

        for row in reader:

            print('Defining', reader.line_num)

            try:

                if row[0][0].isupper():

                    definition = ''

                else:

                    definition = parser.define(row[0])[0]

            except:

                pass

            finally:

                writer.writerow({'Word': row[0], 'Definition': definition.strip()})
                definition = ''

