import csv, inflect

inflect = inflect.engine()

def refineWordlist():

    toChuck = []

    with open('refined.csv', 'a') as outfile:

        writer = csv.DictWriter(outfile, fieldnames=['Refined'])

        with open('missingwords.csv', 'r') as file:

            reader = csv.reader(file, delimiter=',')

            for row in reader:

                # if inflect.singular_noun(row[0]) is False:
                #
                #     writer.writerow({'Refined': row[0]})

                if row[0][-1] == 'd' and row[0][-2] == 'e':

                    toChuck.append(row[0])
                    print(row[0])

                else:
                    pass
                    writer.writerow({'Refined': row[0]})
                    # toChuck.append(row[0])
                    # print(row[0])

        print(len(toChuck))


def wordsLost():

    notRefined = []
    refined = []

    with open('missingwords.csv', 'r') as file1:

        reader1 = csv.reader(file1, delimiter=',')

        for row in reader1:

            notRefined.append(row[0])

    with open('refined.csv', 'r') as file2:

        reader2 = csv.reader(file2, delimiter=',')

        for row in reader2:

            refined.append(row[0])

    with open('wordslost.csv', 'a') as outfile:

        writer = csv.DictWriter(outfile, fieldnames=['Words Lost'])

        writer.writeheader()

        for word in notRefined:

            if word in refined:

                pass

            else:

                writer.writerow({'Words Lost': word})

    return len(notRefined)-len(refined)



if __name__ == '__main__':

    print(wordsLost())
