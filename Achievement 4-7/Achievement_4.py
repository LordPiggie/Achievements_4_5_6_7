# This program is a conversion calculator that uses funtions to convert between metric and imperial values.


def temperatureConversion(unitOfMeasurementTwo: str, amount: int): #This function converts from farenheight to metric or metric to farenheight depending on the choice from the user
    
    if unitOfMeasurementTwo == 'F':

       return round(((amount - 32) * (5 / 9)), 2) #This is the conversion from farenheight to celcius

    elif unitOfMeasurementTwo == 'C':
        
        return round(((amount * 1.8) + 32), 2) #This is the conversion from celcius to Farenheight

    else:

        print('Please try again')

def speedConversion(unitOfMeasurementThree: str, amount: int): #This function converts a unit of speed from metric to imperial or vice versa

    if unitOfMeasurementThree == 'KMH':

        return round((amount / 1.609344), 2) #KMH to MPH

    elif unitOfMeasurementThree == 'MPH': 

        return round((amount * 1.609344), 2) #MPH to KMH

    else:

        print('Please try again')



unitOfMeasurement = input('What are you trying to convert? 1. [F\u00b0, C\u00b0,] or 2: [KMH, or MPH]: ').strip() #This determines if we are converting speed or temp

unitOfMeasurement = int(unitOfMeasurement) #This allows me to ensure the input is a numerical value so the future if statements can be initiated.

if unitOfMeasurement == 1: # if the user has selected 1 for temp, they will follow this statement

    unitOfMeasurementTwo = input('Is your starting unit F (for Farenheight) or C (for Celcius)?: ').strip().upper() # This asks the user which unit is to be converted

    amount = input('How much of this unit would you like to convert?: ').strip().upper() #This asks for the amount of the unit the user wishes to convert

    amount = int(amount) #This ensures that nput is a number

    tempratureOutput = temperatureConversion(unitOfMeasurementTwo, amount)

    if unitOfMeasurementTwo == 'F': #This is to segregate the print statements for the output as the function does all of the calculation

        fC = '{} C\u00b0'.format(tempratureOutput)

        print(fC)

    elif unitOfMeasurementTwo == 'C':

        cF = '{} F\u00b0'.format(tempratureOutput)

        print(cF)

elif unitOfMeasurement == 2:

    unitOfMeasurementThree = input('Is your starting unit KMH (for Kilometers per hour) or MPH (for Miles per hour)?: ').strip() #This asks if we are converting from imperial or metric

    amount = input('How much of this unit would you like to convert?: ').strip() #This is the amount of the given unit to convert

    amount = int(amount) #This again is to ensure the unit is a number

    speedOutput = speedConversion(unitOfMeasurementThree, amount)

    if unitOfMeasurementThree == 'KMH': #This if statement and the following one define the output for the conversion.

        kmhMPH = '{} MPH'.format(speedOutput)

        print(kmhMPH)

    elif unitOfMeasurementThree == 'MPH':

        mphKMH = '{} KPH'.format(speedOutput)

        print(mphKMH)
