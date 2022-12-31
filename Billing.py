# Reading file data
# function defination for Takeing input and printing input
def readFile(fileinput):
    # print(fileinput)
    # opening a file with read permission and storing it into variable file
    file = open(fileinput, "r")
    # reading the file and storing it in line variable
    lines = file.read()
    # printing line
    print(lines)
    # closeing file
    file.close()
    # retrning file value
    return lines


# Storing file data into Array
# function is defined with readFile name,
def convertArray(fileName):
    # opens the file in read mode
    fileObj = open(fileName, "r")
    # puts the file into an array
    words = fileObj.read().splitlines()
    # closing the file
    fileObj.close()
    # Returning the words
    return words


# Take user input and storing in Inovice file
def takeInput(file):
    # opening the Inovice file and storing it in variable called file
    file = open("inovice.csv", "a")
    # for i in range(n):
    # Taking input from user for(name , Phone , Quantity)
    name = input("User Name")
    # moving to next line
    file.write("\n" + name)
    file.write(",")
    phoneNumber = input("Enter your Phone Number")
    file.write(phoneNumber)
    file.write(",")
    # initilize i =0
    i = 0
    # while loop till I is false
    while i <= 10:
        # adding value
        i = i+1
        # asking user to give input
        print("Press Yes to add new else exit")
        # if user response yes the loop will insert
        response = input("Yes or no")
        if (response == "yes"):
            i = 1
            productId = input("Enter your product ID")
            file.write(productId)
            file.write(",")
            quantity = input("Enter the number of Iteams")
            file.write(quantity)
            # else the loop will exit
        else:
            n = 0
            break

        # closing file
        file.close()


def total(productID, qty):
    # opening the Inovice file with append permission
    inovice = open("inovice.csv", "a")
    # opening the Product file with read permission
    product = open("product.csv", "r")
    # totalItem=0
    # finalPrice=0
    # reading product.csv and storing it in variable called filestring
    fileString = product.read()
    # breaking the string for next line using \n and storing in fileString Array
    fileSTringArray = fileString.split("\n")
    # iterating throu the FileString Array
    for x in fileSTringArray:
        # spliting the filestring Array value with "," and strong it in filewordString
        fileWordString = x.split(",")
        # iterating the filewordstring
        for y in fileWordString:
            # spliting the fileWordString with "," and storing it in fileWordSubString
            fileWordSubString = y.split(",")
            # Checking the condition if productId matches with filewordstring value
            if (productID == fileWordSubString[0]):
                # totalitem = qty*the string place holder 2
                totalItem = int(qty)*int(fileWordString[2])
                # finalPrice= Final+ total Item
                finalPrice = finalPrice+totalItem
                # writing the output in final inovice class.
                inovice.write(finalPrice)
                break


def convertListToString(word):
    str = ""
    for ele in word:
        str = str+ele
        return str


# calling a function (readFile) and passing a parameter/argument
# storing the return value in variable called ProductFile
# productFile = readFile("product.csv")
# # Printing file
# print(productFile)

# inoviceFile=readFile("inovice.csv")
# print(inoviceFile)

readFile("product.csv")

# print ("chose ")
takeInput("inovice.csv")
# converting data into Array and storing it into variable called word
word = convertArray("inovice.csv")
value = convertListToString(word)
print(word)
a = value.find("Ammar")
print(a)

# show product
# quanitity * Unit price = total
# matching the product Id and take 3rd element of the list
