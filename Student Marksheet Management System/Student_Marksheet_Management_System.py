import pickle
import os

def add_record():
    try:
        if os.path.isfile('Student Record'):
            f=open('Student Record', 'ab')
            print("File is present in binary mode")
        else:
            f=open('Student Record', 'wb')
            print('File is create in binary mode')
        
        # Student Roll Number
        while True:
            z=0

            roll= input('Enter your Roll Number : ')
            if not roll.isdigit():
                print ('Roll Number has been numeric')
                input("press enter to continue again")
                z=1
                continue
            
            if not(int(roll)>=100 and int(roll)<999):
                print('Roll number should be under 100 to 999')
                input('press enter to continue again again')
                z=1
                continue

            if not(z==1):
                break

        while True:
             z=0 
             name=input("Enter your Name :")
             if not name.isalpha():
                 print('Name will be write in alphabet')
                 input("press enter to continue again")
                 z=1
                 continue
            
             if not(z==1):
                break

        # Theory of computation Marks
        while True:
            z=0

            toc=input("Enter the Marks of TOC : ")
            if not toc.isdigit():
                print('Marks of TOC should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(toc)>=0 and int(toc)<=100):
                print('Marks of TOC should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break

        # Data Management  system Marks
        while True:
            z=0

            dbms=input("Enter the Marks of DBMS : ")
            if not dbms.isdigit():
                print('Marks of DBMS should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(dbms)>=0 and int(dbms)<=100):
                print('Marks of DBMS should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break

        # Data Analytics Marks
        while True:
            z=0

            da=input("Enter the Marks of DA : ")
            if not da.isdigit():
                print('Marks of DA should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(da)>=0 and int(da)<=100):
                print('Marks of DA should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break

        # Internet & Webtech Marks
        while True:
            z=0

            html_css=input("Enter the Marks of HTML CSS : ")
            if not html_css.isdigit():
                print('Marks of HTML CSS should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(html_css)>=0 and int(html_css)<=100):
                print('Marks of HTML CSS should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break


        # Linux Marks
        while True:
            z=0

            linux=input("Enter the Marks of Linux : ")
            if not linux.isdigit():
                print('Marks of Linux should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(linux)>=0 and int(linux)<=100):
                print('Marks of Linux should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break

        
        # Python Marks
        while True:
            z=0

            python=input("Enter the Marks of Python : ")
            if not python.isdigit():
                print('Marks of Python should be in digit')
                input("press enter to continue again")
                z=1
                continue

            if not (int(python)>=0 and int(python)<=100):
                print('Marks of Python should be under 0 to 100')
                input("press enter to continue again again")
                z=1 
                continue

            if not(z==1):
                break

        total= int(toc) + int(dbms) + int(da) + int(html_css) + int(linux) + int(python)
        print('total', int(total))
        percentage = total/6
        print('percentage', int(percentage))

        if percentage>=90 and percentage<=100 :
            # print('Grade A', percentage)
            Grade="A"
        elif percentage>=80 and percentage<=89 :
            # print('Grade B', percentage)
            Grade = "B"
        elif percentage>=70 and percentage<=79 :
            # print('Grade C', percentage)
            Grade = "C"
        elif percentage>=60 and percentage<=69 :
            # print('Grade D', percentage)
            Grade = "D"
        elif percentage>=50 and percentage<=59 :
            # print('Grade E', percentage)
            Grade = 'E'
        elif percentage>=40 and percentage<=49 :
            # print('Grade F', percentage)
            Grade = 'F'
        else :
            Grade = "FAIL IN EXAMS"

        print( 'total', total, 'percentage ', int(percentage) , 'Grade ', Grade)

        record = [ int(roll), name, int(toc), int(dbms), int(da), int(html_css), int(linux), int(python), int(total), int(percentage), Grade]
        # rec()
        pickle.dump(record, f)


    except EOFError:
        f.close

    

# All Student Record display
def all_record_display():
    try:
        f = open('Student Record', 'rb')
        # print( ' '*33, '='*122)
        print()
        print()

        print( ' '*83, '=======================')
        print("%108s" %" All Student Record Data ")
        print( ' '*83, '=======================')

        print()
        print()
        print()
        print( ' '*33, '='*122)

        print("%40s" % "Roll ","%10s" % "Name","%10s" % "TOC","%10s" % "DBMS","%9s" % "DA","%13s" % "HTML CSS",
        "%10s" % "LINUX","%10s" % "PYTHON","%10s" % "TOTAL","%13s" % "PERCENTAGE","%10s" % "GRADE")

        print( ' '*33, '='*122)

        while True:
            record = pickle.load(f)
            print("% 38s" % record[0], "% 13s" % record[1], "% 8s" % record[2], "% 10s" % record[3], "% 10s" % record[4], "% 10s" % record[5],
            "% 12s" % record[6], "% 9s" % record[7], "% 11s" % record[8], "% 10s" % record[9],"% 12s" % record[10])

    except EOFError:
        f.close()

    except IOError:
        print('unable to open the file')



# Record search by roll number
def search_by_roll_number():
    try:
        # z=0
        f = open('Student Record', 'rb')
        
        
        while True:
            z=0
            sr = input("Enter roll number , then particular student record will be shown : ")
            if not sr.isdigit():
                print ('Roll Number has been numeric')
                input("press enter to continue again")
                z=1
                continue
            if not(int(sr)>=100 and int(sr)<999):
                print('Roll number should be under 100 to 999')
                input('press enter to continue again again')
                z=1
                continue
            if not(z==1):
                break

        print( ' '*33, '='*122)
        print()
        print()
        print()

        print( ' '*84, '================')
        print("%100s" %"Student Record")
        print( ' '*84, '================')

        print()
        print()
        print()
        print( ' '*33, '='*122)

        print("%40s" % "Roll ","%10s" % "Name","%10s" % "TOC","%10s" % "DBMS","%9s" % "DA","%13s" % "HTML CSS",
        "%10s" % "LINUX","%10s" % "PYTHON","%10s" % "TOTAL","%13s" % "PERCENTAGE","%10s" % "GRADE")

        print( ' '*33, '='*122)
        
        while True:
            record = pickle.load(f)
            if record[0]==int(sr):

                print()
                print()

                print("% 38s" % record[0], "% 13s" % record[1], "% 8s" % record[2], "% 10s" % record[3], "% 10s" % record[4], "% 10s" % record[5],
                "% 12s" % record[6], "% 9s" % record[7], "% 11s" % record[8], "% 10s" % record[9],"% 12s" % record[10])

                print()
                print()

                print( ' '*33, '='*122)

    except EOFError:
        f.close()
        if z==0:
            print("Record Not Found")

    except IOError:
        print('unable to open the file')


# Delete by Roll No.
def delete_by_roll():
    try:
        while True:
            z=0
            tr=input("Enter Roll No. to Delete Particular Student Record : ")
            if not tr.isdigit():
                print("Please Enter Correct Roll No. in Digit")
                input("Press Enter to Continue ")
                z=1
                continue

            if not(int(tr)>100 and int(tr)<999):
                print("Please Enter Correct Roll No. (3-digits)")
                input("Press Enter to Continue")
                z=1
                continue
            if not(z==1):
                break
        
        # tr=int(input("Enter Roll No. to Delete Particular Student Record"))
        f=open("Student Record","rb")
        tf=open("temp","wb")
        print( ' '*33, '='*122)
        print()
        print()
        print()

        print( ' '*84, '================')
        print("%100s" %"Student Record")
        print( ' '*84, '================')

        print()
        print()
        print()
        print( ' '*33, '='*122)

        print("%40s" % "Roll ","%10s" % "Name","%10s" % "TOC","%10s" % "DBMS","%9s" % "DA","%13s" % "HTML CSS",
        "%10s" % "LINUX","%10s" % "PYTHON","%10s" % "TOTAL","%13s" % "PERCENTAGE","%10s" % "GRADE")

        print( ' '*33, '='*122)

        z=0
        while True:
            record=pickle.load(f)
            if record[0]==int(tr):

                print()
                print()

                print("% 38s" % record[0], "% 13s" % record[1], "% 8s" % record[2], "% 10s" % record[3], "% 10s" % record[4], "% 10s" % record[5],
                "% 12s" % record[6], "% 9s" % record[7], "% 11s" % record[8], "% 10s" % record[9],"% 12s" % record[10])

                z=1

                print()
                print()

                print( ' '*33, '='*122)
            else:
                pickle.dump(record,tf)

    except EOFError:
        f.close()
        tf.close()
        if z==0:
            print("Record not found")
        else:
            os.remove("Student Record")
            os.rename("temp","Student Record")
            print("Student Record is Delete ")
    except IOError:
        print("unable to open the file")


# Record search by name
def search_by_name():
    try:
        f = open('Student Record', 'rb')

        while True:
            z=0
            sn=input('Enter student name, then particular student record will be shown : ')
            if not sn.isalpha():
                print("Please Enter correct Name , Then Student Record Will be Shown ")
                input("Press Enter To continue ")
                z=1
                continue

            if not(z==1):
                break
            

        print( ' '*33, '='*122)
        print()
        print()
        print()

        print( ' '*84, '================')
        print("%100s" %"Student Record")
        print( ' '*84, '================')

        print()
        print()
        print()
        print( ' '*33, '='*122)

        print("%40s" % "Roll ","%10s" % "Name","%10s" % "TOC","%10s" % "DBMS","%9s" % "DA","%13s" % "HTML CSS",
        "%10s" % "LINUX","%10s" % "PYTHON","%10s" % "TOTAL","%13s" % "PERCENTAGE","%10s" % "GRADE")

        print( ' '*33, '='*122)
        
        while True:
            record = pickle.load(f)
            if record[1]==sn:

                print()
                print()

                print("% 38s" % record[0], "% 13s" % record[1], "% 8s" % record[2], "% 10s" % record[3], "% 10s" % record[4], "% 10s" % record[5],
                "% 12s" % record[6], "% 9s" % record[7], "% 11s" % record[8], "% 10s" % record[9],"% 12s" % record[10])

                print()
                print()
                print( ' '*33, '='*122)

    except EOFError:
        f.close()
        if z==0:
            print("Record Not Found")

    except IOError:
        print('unable to open the file')


#Delete By Name
def delete_by_name():
    try:
        while True:
            z=0
            sn=input('Enter student name, then particular student record will be shown : ')
            if not sn.isalpha():
                print("Please Enter correct Name , Then Student Record Will be Shown ")
                input("Press Enter To continue ")
                z=1
                continue

            if not(z==1):
                break

        f = open('Student Record', 'rb')

        tf=open("temp","wb")
        
        print( ' '*33, '='*122)
        print()
        print()
        print()

        print( ' '*84, '================')
        print("%100s" %"Student Record")
        print( ' '*84, '================')

        print()
        print()
        print()
        print( ' '*33, '='*122)

        print("%40s" % "Roll ","%10s" % "Name","%10s" % "TOC","%10s" % "DBMS","%9s" % "DA","%13s" % "HTML CSS",
        "%10s" % "LINUX","%10s" % "PYTHON","%10s" % "TOTAL","%13s" % "PERCENTAGE","%10s" % "GRADE")

        print( ' '*33, '='*122)
        
        z=0
        while True:
            record = pickle.load(f)
            if record[1]==sn:

                print()
                print()

                print("% 38s" % record[0], "% 13s" % record[1], "% 8s" % record[2], "% 10s" % record[3], "% 10s" % record[4], "% 10s" % record[5],
                "% 12s" % record[6], "% 9s" % record[7], "% 11s" % record[8], "% 10s" % record[9],"% 12s" % record[10])

                print()
                print()
                print( ' '*33, '='*122)

                z=1

            else:
                pickle.dump(record,tf)
    
    except EOFError:
        f.close()
        tf.close()
        if z==0:
            print("Record not found")
        else:
            os.remove("Student Record")
            os.rename("temp","Student Record")
            print("Student Record is Delete ")
    except IOError:
        print("unable to open the file")

            



# MARKS SHEET FOMATE
def mark_sheet():
    try:
        f=open('Student Record', 'rb')
        sn=input("Please enter the student name for find the marksheet : ")
        
        while True:
            record = pickle.load(f)
            if record[1]==sn:
                
                print( ' '*40, '='*100)
                print()
                print()
                
                print( ' '*71, '=============================')
                print("% 101s" %' Marksheet Management System ')
                print( ' '*71, '=============================')
                
                print()
                print()
                print()
                print("% 58s" % 'Roll no : ',record[0], "% 58s" % 'Name : ', record[1])
                print('% 62s'% '==============','% 68s'% '=================' )
                print()
                print()
                
                print( ' '*40, '='*100)
                print("% 55s" % 'S.NO.  ', "% 20s" %  '    SUBJECT NAME           ',  "% 10s" % 'MAX MARKS',  "% 15s" % 'MIN MARKS', "% 20s" %  'MARKS OBTAINED')
                print( ' '*40, '='*100)
                
                print("% 55s" % ' 1.    ', "% 20s" %  'Theory of Computation      ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[2])

                print("% 55s" % ' 2.    ', "% 20s" %  'Database Management System ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[3])

                print("% 55s" % ' 3.    ', "% 20s" %  'Data Analytics             ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[4])

                print("% 55s" % ' 4.    ', "% 20s" %  'Internet & webtech         ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[5])

                print("% 55s" % ' 5.    ', "% 20s" %  'Linux Lab                  ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[6])

                print("% 55s" % ' 6.    ', "% 20s" %  'Python Lab                 ',  "% 10s" % '   100   ',  "% 15s" % '   35    ', "% 15s" %  record[7])


                print()
                print()
                print( ' '*40, '='*100)
                print(' '*110, 'Total Marks :', record[8])
                print(' '*110, 'Percentage : ', record[9])
                print(' '*110, 'Grade :      ', record[10])

            

    except EOFError:
        f.close()

    except IOError:
        print('unable to open the file')







def main():
    while True:
        os.system('cls')
        m='''

                     =======================================================================================================
                                                       STUDENT MARKSHEET MANAGEMENT SYSTEM
                     =======================================================================================================
                                                                               							
                                                            +-----------------------+
                                                            |       Main Menu       |
                                                            |      ===========      |
                                                            +-----------------------+

                       +--------+----------------------------------------------------------------------------------------+
                       | S. NO. |               Name of Working Process                                                  |
                       +--------+----------------------------------------------------------------------------------------+    
                       |   1.   |    Enter the Student Record, if You want to add the Student Record.                    |
                       |   2.   |    You want to See All Records.                                                        |
                       |   3.   |    Particular Student Record Search by Student Roll Number.                            |
                       |   4.   |    Particular Student Record Delete by Student Roll Number .                           |
                       |   5.   |    Particular Student Record Search by Student Name.                                   |
                       |   6.   |    Particular Student Record Delete by Student Name.                                   |
                       |   7.   |    Enter Student Name then Student Marksheet Will Be Shown.                            |
                       |   8.   |    Exit.                                                                               |
                       +--------+----------------------------------------------------------------------------------------+

                     =======================================================================================================
'''
        print(m)
        # print("Main Menu of Student Details")
        # print('1. Enter the Student Record, if You want to add the Student Record')
        # print('2. You want to See All Records')
        # print('3. Particular Student Record Search by Student Roll Number ')
        # print("4. Particular Student Record Delete by Student Roll Number")
        # print('5. Particular Student Record Search by Student Name')
        # print('6. Particular Student Record Delete by Student Name')
        # print('7. Enter Student Name then Student Marksheet Will Be Shown ')
        # print('8. Exit')
        ch= input('                    Enter Your Choice :')
        # print(" "*30, 'Enter Your Choices : ',ch)
        os.system('cls')
        if (ch=='1'):
            add_record()
        elif ch=='2':
            all_record_display()
        elif ch=='3':
            search_by_roll_number()
        elif ch=='4':
            delete_by_roll()
        elif ch=='5':
            search_by_name()
        elif ch=='6':
            delete_by_name()
        elif ch=='7':
            mark_sheet()
        elif  ch=='8':
            print('Your program is end ')
            break
        else:
            print("invalid choice")

        input('Press Enter to Continue')


def login():
    z=0
    while True:
        # z=0
        os.system('cls')
        print()
        print()
        m='''                                                                                               
                                                        *           * * * *     * * * * * *     * * * * *     *        *                   
                                                        *           *     *     *                   *         *  *     *                   
                                                        *           *     *     *   * * * *         *         *     *  *                   
                                                        * * * *     * * * *     * * *     *     * * * * *     *        *                   
                                                        *******************************************************************                 

                                             *            *     * * * * *     *         *     * * * *         * * * *     *             *   
                                              *    *     *          *         *  *      *     *        *     *       *     *     *     *    
                                               *  *  *  *           *         *     *   *     *        *     *       *      *  *   *  *     
                                                *      *        * * * * *     *         *     * * * *         * * * *        *       *      
                                            *********************************************************************************************** 
                                                                                                        

        '''
        print(m)
        # print("% 65s" % '================')
        # print("% 63s" %"login Window")
        # print("% 65s" % '================')
        print()
        username = input("% 55s" %"Enter Username :")
        password = input("% 55s" %"Enter Password :")
        print()
        if (username=='Bharat' and password=='Rathore'):
            print("% 55s" %'Login sucessfull')
            input("Press Enter to Continue in the Menu")
            z=1
            if z==1:
                main()
            else:
                break
            
            # continue
        else:
            print("% 55s" %"Invalid Login Id")
            input("press Enter, You want to Enter again")
            continue
        

        if (z==1):
            break
        #     main()




login()