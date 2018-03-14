import csv

def missingImages():

    presentImages = []
    allWords = []

    with open('presentimages.csv', 'r') as pfile:

        preader = csv.reader(pfile, delimiter=',')

        for row in preader:

            presentImages.append(row[0])

    with open('ourwords.csv', 'r') as afile:

        areader = csv.reader(afile, delimiter=',')

        for row in areader:

            allWords.append(row[0])

    #print(len(allWords)-len(presentImages))

    with open('missingwords.csv', 'a') as outfile:

        writer = csv.DictWriter(outfile, fieldnames=['Missing'])

        for word in allWords:

            if word in presentImages:

                pass

            else:

                if word[0].isupper() == True:

                    pass

                else:

                    writer.writerow({'Missing': word})




if __name__ == '__main__':

    missingImages()
