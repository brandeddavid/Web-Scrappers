import csv

ourWords = []
missingWords = []
presentWords = []

with open('ourwords.csv', 'r') as ourfile:

    reader = csv.reader(ourfile, delimiter=',')

    for row in reader:

        try:

            ourWords.append(row[0].lower())

        except:

            pass

print(len(ourWords))

with open('spellzoneout.csv', 'a', newline='') as outfile:

    writer = csv.DictWriter(outfile, fieldnames=['our words', 'missing words'])
    writer.writeheader()

    with open('spellzone.csv', 'r') as infile:

        reader = csv.reader(infile, delimiter=',')

        for row in reader:

            try:

                #print(row[2].split('\n'))

                for word in row[2].split('\n'):

                    if word.split()[0].lower() in ourWords:

                        presentWords.append(word.split()[0])

                    else:

                        missingWords.append(word)

            except:

                pass

            finally:

                writer.writerow({'our words': str(presentWords).replace('[', '').replace(']', ''), 'missing words': str(missingWords).replace('[', '').replace(']', '')})
                presentWords = []
                missingWords = []
