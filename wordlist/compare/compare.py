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

with open('wordlistout.csv', 'a', newline='') as outfile:

    writer = csv.DictWriter(outfile, fieldnames=['wordlist', 'list', 'our words', 'missing words'])
    writer.writeheader()

    with open('wordlist.csv', 'r') as infile:

        reader = csv.reader(infile, delimiter=',')

        for row in reader:

            try:

                print(row[1].split('\n'))

                for word in row[1].split('\n'):

                    if word.lower() in ourWords:

                        presentWords.append(word)

                    else:

                        missingWords.append(word)

            except:

                pass

            finally:

                writer.writerow({'wordlist': row[0], 'list': row[1], 'our words': [word for word in presentWords], 'missing words': missingWords})
                presentWords = []
                missingWords = []