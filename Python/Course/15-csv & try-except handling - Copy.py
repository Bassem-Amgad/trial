import csv #comma seperated values
with open('examplefile.csv')as csvfile: # read everthing as string
    readcsv = csv.reader (csvfile,delimiter=',')
    dates=[]
    colors=[]
    for row in readcsv:
        print(row)
        print(row[0],row[3])
        date =row[0]
        dates.append(date)
        color =row[3]
        colors.append(color)

    print(dates)
    print(colors)
    try:
    ''' if whatcolor in colors:'''
        whatcolor = input ('what color do u wish to know date of ? ')
        colindex=colors.index(whatcolor.lower())
        # lower means handling capital letter as they were small
        print(dates[colindex])
    except Exception as e:
   ''' else:
        print('value not in list') '''
        print(e)
