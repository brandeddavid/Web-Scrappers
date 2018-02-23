from wiktionaryparser import WiktionaryParser
import csv, wget

parser = WiktionaryParser()

with open('audio.csv', 'a') as outfile:

    headers = ['Word', 'Audio', 'Category']
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    with open('words.csv', 'r') as infile:

        reader = csv.reader(infile, delimiter=',')

        for row in reader:

            print('Downloading', reader.line_num)

            try:

                if row[0][0].isupper() == True:

                    audio = ''
                    category = ''

                else:

                    word = parser.fetch(row[0])

                    audio = 'https:' + word[0]['pronunciations']['audio'][0]
                    wget.download(audio, './audio/'+row[0]+'.mp3')
                    category = word[0]['definitions'][0]['partOfSpeech']

            except Exception as e:

                #print(e)
                pass

            finally:

                writer.writerow({'Word':row[0], 'Audio': audio, 'Category': category})
                audio = ''
                category = ''