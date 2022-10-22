# Samar Ali
# Date 10/22/2022

bookings = [
    {
        "visitorName": "John Doe",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 5
    },
    {
        "visitorName": "John Doe",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 2
    },
    {
        "visitorName": "Williams Smith",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 4
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 8
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 2
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 20
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 19
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 18
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 17
    },
]

maxParkingSpace = 20
continueProgram = True


def getRequestedDay():
    requestedDay = int(input('Enter the day between (1 - 14): \n'))

    while requestedDay < 0 or requestedDay > 14:
        print('Invalid Day! Kindly enter valid Day')
        requestedDay = int(input('Enter the day between (1 - 14): \n'))

    return requestedDay


def getCarLicence():
    carLicence = input('Enter the licence number: \n')

    while not carLicence.isalnum():
        print('Invalid Licence! Special character are not allowed')
        carLicence = input('Enter the licence number: \n')

    return carLicence


def getVisitorName():
    visitorName = input('Enter the visitor name: \n')

    while not all(name.isalpha() or name.isspace() for name in visitorName):
        print('Invalid Name! Name should contain only alphabets')
        visitorName = input('Enter the visitor name: \n')

    return visitorName


def checkSpaceAvailability(requestedDay):
    spaces_occupied_at_requestedDay = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay:
            spaces_occupied_at_requestedDay += 1

    if spaces_occupied_at_requestedDay >= maxParkingSpace:
        return -1

    return spaces_occupied_at_requestedDay


def isAccessibleParking():
    parkingType = input('Do you want accessible parking spaces? (yes/no): \n')

    if parkingType == 'yes':
        return True
    else:
        return False


def assignGeneralSpace(visitorName, licence, requestedDay):
    generalSpaceNumber = 20

    for booking in bookings:
        if booking['requestedDay'] == requestedDay and booking['parkingNumber'] != generalSpaceNumber:
            generalSpaceNumber = maxParkingSpace
        else:
            generalSpaceNumber = generalSpaceNumber - 1

    createBooking(visitorName, licence, requestedDay, generalSpaceNumber)


def assignAccessibleSpace(visitorName, licence, requestedDay):
    accessibleSpaceNumber = checkSpaceAvailability(requestedDay)

    createBooking(visitorName, licence, requestedDay,
                  accessibleSpaceNumber + 1)


def showStats():
    userInput = input('1) Add Booking \n2) Show Stats: \n')

    if userInput == '2':
        return True
    elif userInput == '1':
        return False


def showStatsOptions():
    print('Choose the stats you want to see \n')
    print('1) See numbers of accessible spaces used any of the 14 days \n')
    print('2) See numbers of general spaces used any of the 14 days \n')
    print('3) See Total numbers of spaces on any of the 14 days \n')
    print('4) See Total numbers of accessible spaces on whole period (14 Days) \n')
    print('5) See Total numbers of general spaces on whole period (14 Days) \n')
    print('6) See Total numbers of spaces on whole period (14 Days) \n')

    userInput = input()

    if userInput == '1':
        showSingleDayAccessibleStats()
    elif userInput == '2':
        showSingleDayGeneralStats()
    elif userInput == '3':
        totalSpacesOnRequestedDay()
    elif userInput == '4':
        wholePeriodAccessibleSpaces()
    elif userInput == '5':
        wholePeriodGeneralSpaces()
    elif userInput == '6':
        wholePeriodTotalSpaces()


def showSingleDayAccessibleStats():
    requestedDay = int(input(
        'Enter the day you want to See the accessible stats: \n'))

    accessibleSpacesOnRequestedDay = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay and booking['parkingNumber'] <= 5:
            accessibleSpacesOnRequestedDay += 1

    print('Total Accessible spaces used: ' +
          str(accessibleSpacesOnRequestedDay))


def showSingleDayGeneralStats():
    requestedDay = int(input(
        'Enter the day you want to See the general Stats: \n'))

    generalSpacesOnRequestedDay = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay and booking["parkingNumber"] >= 6:
            generalSpacesOnRequestedDay += 1

    print('Total General spaces used: ' +
          str(generalSpacesOnRequestedDay))


def totalSpacesOnRequestedDay():
    requestedDay = int(input(
        'Enter the day you want to See the total space Stats: \n'))

    totalSpacesOccupied = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay:
            totalSpacesOccupied += 1

    print('Total spaces used: ' +
          str(totalSpacesOccupied))


def wholePeriodAccessibleSpaces():
    totalAccessibleSpaces = 0

    for booking in bookings:
        if booking["parkingNumber"] <= 5:
            totalAccessibleSpaces += 1

    print('Total accessible spaces used (in 14 days): ' +
          str(totalAccessibleSpaces))


def wholePeriodGeneralSpaces():
    totalGeneralSpaces = 0

    for booking in bookings:
        if booking["parkingNumber"] >= 6:
            totalGeneralSpaces += 1

    print('Total general spaces used (in 14 days): ' +
          str(totalGeneralSpaces))


def wholePeriodTotalSpaces():
    totalSpaces = 0

    for booking in bookings:
        totalSpaces += 1

    print('Total spaces used (in 14 days): ' +
          str(totalSpaces))


def createBooking(visitorName, licence, requestedDay, parkingNumber):
    newBooking = {}
    newBooking['visitorName'] = visitorName
    newBooking['licence'] = licence
    newBooking['requestedDay'] = requestedDay
    newBooking['parkingNumber'] = parkingNumber

    bookings.append(newBooking)


while continueProgram:

    isShowStats = showStats()

    if not isShowStats:
        requestedDay = getRequestedDay()
        parkingSpace = checkSpaceAvailability(requestedDay)

        if parkingSpace != -1:
            accessibleParking = isAccessibleParking()
            visitorName = getVisitorName()
            carLicence = getCarLicence()

            if accessibleParking:
                assignAccessibleSpace(visitorName, carLicence, requestedDay)
            else:
                assignGeneralSpace(visitorName, carLicence, requestedDay)

            print(bookings)

            # print('Parking has been reserved! \nDay ' + str(requestedDay) +
            #       '\nParking number: ' + str(parkingSpace + 1))

            continueProgram = input('Continue (yes/no): \n')
            continueProgram = False if continueProgram == 'no' else continueProgram
    else:
        showStatsOptions()