class Multiplefunction():
    def Subfields():
        lists =["Sub fields in AI are:","Machine Learning", "Neural Networks" ,"Vision" ,"Robotics" ,"Speech Processing" ,"Natural Language Processing"]
        for field in lists:
            print(field)
    def OddEven():
        num = int(input("Enter a number"))
        if(num % 2 == 0):
            print(num,"is Even number")
            message = "is Even number"
        else:
            print(num,"is Odd number")
            message = "is Odd number"
    def Eligible():
        gender = (input('Your gender:')).lower()
        age = int(input("Your Age:"))
        if(gender == "male") and (age >= 21 ):
            print( "ELIGIBLE")
        elif(gender == "female") and(age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        s1 = int(input("Subject1 = "))
        s2 = int(input("Subject2 = "))
        s3 = int(input("Subject3 = "))
        s4 = int(input("Subject4 = "))
        s5 = int(input("Subject5 = "))
        total = s1+s2+s3+s4+s5
        print("Total : ",total)
        per = total / 5
        print("Percentage :",per)
    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        area = (height * breadth) / 2
        print("Area formula = (height * breadth) / 2")
        print ("Area of triangle = ",area)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth1:"))
        perimeter = height1 + height2 + breadth1
        print("Perimeter = height1 + height2 + breadth1")
        print ("Perimeter of Triangle :",perimeter)