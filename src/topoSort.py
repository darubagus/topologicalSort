# Nama          : Daru Bagus Dananjaya
# NIM           : 13519080
# Kelas         : K02
# Description   : 


import roman as bm

def readFile(testcase):
    # I.S -
    # F.S Mengembalikan listOfCourse sesuai dengan bentuk yang diinginkan
    listOfCourse = []
    line = inString.readlines()

    i = 0
    while (i < len(line)):
        cleanString = line[i].replace(" ","")
        cleanString = cleanString.replace(".","")
        cleanString = cleanString.replace("\n","")
        listOfCourse.append(cleanString)
        i+=1

    for i in range(len(listOfCourse)):
        listOfCourse[i] = listOfCourse[i].split(',')
    
    # Bentuk List Of Course : [["C1","C3"], ["C2","C1","C4"], ["C3"], ["C4","C1","C3"], ["C5","C2","C4"]]
    return listOfCourse

def printPersoalan(testcase) :

    line = inString.readlines()
    print("Problem :")
    i = 0
    while (i < len(line)):
        cleanString = line[i].replace("\n","")
        cleanString = cleanString.replace(".","")
        cleanString = cleanString.split(',')
        if (len(cleanString)==1):
            print("Course "+cleanString[0]+" has no prerequisite.")
        else :
            print("Course "+cleanString[0]+"'s prerequisite(s) are ", end="")
            for j in range(1,len(cleanString)):
                if (j != len(cleanString)-1) :
                    print(" "+cleanString[j]+",", end='')
                else :
                    print(" "+cleanString[j])
        i+=1

def topologicalSKRT(listOfCourse):
    courseSemester = []
    
    # Selama masih ada course di listOfCourse, maka loop penghapusan akan berjalan
    while (len(listOfCourse) != 0) :
        noPrereq = []

        # Mencari course yang tidak memiliki prerequisite
        for i in range(len(listOfCourse)):
            '''Jika course tidak memiliki prerequisite, maka tambahkan ke list course
            yang tidak memiliki prerequisite'''
            if (len(listOfCourse[i]) == 1):
                noPrereq.append(listOfCourse[i][0])

        # Menghapus course yang tidak memiliki prerequisite dari seluruh listOfCourse (yang ada di dalam array course lain)
        for i in range(len(noPrereq)):
            for j in range(len(listOfCourse)):
                '''Kalo course yang gapunya prerequisite ada di dalam list prerequisite course lain, maka dia dihapus
                tapi kalo gaada, yaudah lanjut aja'''
                if (noPrereq[i] in listOfCourse[j]) :
                    k = 0
                    status = False
                    while ((not status) and k < len(listOfCourse)):
                        if (noPrereq[i] == listOfCourse[j][k]) :
                            # hapus course yang tidak memiliki prerequisite dari list prerequisite course lain
                            del listOfCourse[j][k]
                            status = True
                        else :
                            k+=1
        
        # Menghapus course yang tidak memiliki prerequisite dari listOfCourse
        i = 0
        while (i < len(listOfCourse)):
            # Kalo dia gapunya prerequisite, dia pasti udah diapus di langkah sebelumnya, makanya disini kosong terus diapus deh
            if (len(listOfCourse[i]) == 0) :
                del listOfCourse[i]
            else :
                i+=1

        # Masukkan seluruh course yang tidak memiliki prerequisite ke dalam array courseSemester
        courseSemester.append(noPrereq)
    
    printSemester(courseSemester)
    

def printSemester(courseSemester) :
    #Mencetak data course per semester
    for i in range(len(courseSemester)) :
        print("Semester ", bm.toRoman(i+1), " :", end='')
        # Mencetak data course yang ada di semester yang bersangkutan
        for j in range(len(courseSemester[i])):
            if (j != len(courseSemester[i])-1) :
                print(" "+courseSemester[i][j]+",", end='')
            else :
                print(" "+courseSemester[i][j])

# Main Program
fileName = input("Masukkan nama file : ")
testCase = "../test/"+fileName

inString = open(testCase, "r")
printPersoalan(inString)
inString.close()

inString = open(testCase, "r")
listOfCourse = readFile(inString)
inString.close()
print()
print("Solusi :")
topologicalSKRT(listOfCourse)

                  
                    

