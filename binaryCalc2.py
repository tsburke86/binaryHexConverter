

# see how many binary slots it will take
def getSlots(num):
    n = 1
    while True:
        if num < 2**n: return n
        n += 1
        
# translate a regular number to binary
def getBinary(num):
    slots = getSlots(num)
    binary = ''

    while slots >= 1:
        if num >= 2**(slots-1):
            binary += '1'
            num = num % (2 ** (slots-1))        
        else: binary +='0'
        slots -= 1
    # Add leading zeros for hex translation
    newBin = addZeros(binary)
    return newBin
    

# translate binary to regular number
def getNumber(binary):
    binary = removeZeros(binary)
    slots = len(binary)
    number = 0
    for i in range(slots):
        if binary[i] == '1':
            number += 2**(slots-1)
        slots -= 1
    return number
        


# translate binary to hex
def getHex(binary):
    hexDict = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'a',
        '1011': 'b',
        '1100': 'c',
        '1101': 'd',
        '1110': 'e',
        '1111': 'f',
        }
    hexNum = []
    hexString=''
    slots = len(binary)
    while slots > 0:
        d = binary[slots-4:slots]
        hexNum.append(hexDict[d])
        slots -= 4
    while hexNum:
        hexString += hexNum.pop()
    return hexString
    
     
# generate the binaries for translation, just do once and copy to dict
def printHex():
    charList = [
        '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'
        ]
    count = 0
    for i in charList:
        print("'"+getBinary(count)+"'"+": '"+str(i)+"',",)
        count +=1

        
# test function        
def transNum(num):
    a = getBinary(num)
    return getHex(a)

# Add leading zeros for hex translation
def addZeros(binary):
    if len(binary)%4 != 0:
        zeros = ''
        for i in range(4-len(binary)%4):
            zeros+='0'
        binary = zeros+binary
    return binary
    
    
#remove leading zeros
def removeZeros(binary):
    count = 0
    while count < 3:
        if binary[count] == '0':
            count += 1
        else: break
    newBin = binary[count:]
    return newBin

# main function to translate numbers
def main():
    while True:
        print("## TRANSLATE A NUMBER TO HEXADECIMAL ##\n")
        number = input('Enter a number to translate (q to quit): ')
        if number.upper() == 'Q': break
        try: number=abs(int(number))
        except:
            print("must be a whole number")
            continue
        binary = getBinary(number)
        hexNum = getHex(binary)
        print("{} is:\n {} in binary,\n {} in hexadecimal"\
              .format(number, removeZeros(binary), hexNum))
        print()
    print("\nSee you next time")


main()
