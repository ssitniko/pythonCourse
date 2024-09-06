# Birthday program

birthday = int(input('Enter your Birthday(integers only!): '))

birthmonth = int(input('Enter your Birthmonth (integers only!): '))


if birthday >= 21 and birthday < 32 and birthmonth == 3 or birthday <= 20 and birthday > 0 and birthmonth == 4:
    print('March-April birth')

elif birthday >= 21 and birthday < 31 and birthmonth == 4 or birthday <= 21 and birthday > 0 and birthmonth == 5:
    print('April-May birth')

elif birthday >= 22 and birthday < 32 and birthmonth == 5 or birthday <= 21 and birthday > 0 and birthmonth == 6:
    print('May-June birth')

elif birthday >= 22 and birthday < 31 and birthmonth == 6 or birthday <= 22 and birthday > 0 and birthmonth == 7:
    print('June-July birth')

elif birthday >= 23 and birthday < 32 and birthmonth == 7 or birthday <= 21 and birthday > 0 and birthmonth == 8:
    print('July-August birth')

elif birthday >= 22 and birthday < 32 and birthmonth == 8 or birthday <= 23 and birthday > 0 and birthmonth == 9:
    print('August-September birth')

elif birthday >= 24 and birthday < 31 and birthmonth == 9 or birthday <= 23 and birthday > 0 and birthmonth == 10:
    print('September-October birth')

elif birthday >= 24 and birthday < 32 and birthmonth == 10 or birthday <= 22 and birthday > 0 and birthmonth == 11:
    print('October-November birth')

elif birthday >= 23 and birthday < 31 and birthmonth == 11 or birthday <= 22 and birthday > 0 and birthmonth == 12:
    print('November-December birth')

elif birthday >= 23 and birthday < 32 and birthmonth == 12 or birthday <= 20 and birthday > 0 and birthmonth == 1:
    print('December-January birth')

elif birthday >= 21 and birthday < 32 and birthmonth == 1 or birthday <= 19 and birthday > 0 and birthmonth == 2:
    print('January-February birth')

elif birthday >= 20 and birthday < 30 and birthmonth == 2 or birthday <= 20 and birthday > 0 and birthmonth == 3:
    print('February-March birth')
else:
    print('Please enter correct Birthday or Birthmonth')
