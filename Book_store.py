import sqlite3
db=sqlite3.connect('Lib.db')
dd=sqlite3.connect('Student.db')

print("\n\t\t*******************Library Management System***********************\n")
ma=0
print('''\n\t\t 1. ADD BOOKS 
\t\t 2. ISSUE BOOKS
\t\t 3. EDIT BOOKS DATA
\t\t 4. DELETE BOOKS DATA
\t\t 5. RETURN BOOKS
\t\t 6. EXIT''')

while True:
   choice=int(input("\n\t\tEnter your choice : "))
          # BOOK DATA SRORED
   if choice==1:
       print("\n\t\t*************ADD BOOKS**************")
       while True:
          b_id=input("\n\t\tEnter Book ID : ")
          b_ttl=input("\t\tEnter Title of Book : ")
          b_aut=input("\t\tEnter Author of Book : ")
          b_ed=input("\t\tEnter Edition of Book : ")
          b_pr=input("\t\tEnter Price of Book : ")
          try:
              cursor=db.cursor()
              cursor.execute('INSERT INTO Libr(Book_ID,Title,Author,Edition,Price) values(?,?,?,?,?)',(b_id,b_ttl,
                                                                                                       b_aut,b_ed,b_pr))
              db.commit()
          except:
             print("\n\t\t-----------------> DATA NOT STORED !")

          ch=input("\n\t\tADD MORE BOOKS (Y/N) : ")
          if ch=='Y' or ch=='y':
              continue
          else:
             print("\n\t\t------------------> DATA STORED !")
             break
       db.close()

       # ISSUE BOOK
   elif choice==2:
      print('\n\t\t********FIND STUDENTS DATA***********')

      id=input("\n\t\tEnter ERP ID : ")
      cursor=dd.cursor()
      cursor.execute("SELECT * FROM Stu WHERE ERP_ID='"+id+"'")
      var=cursor.fetchone()
      if var!=None:
         print('\t\t-----------------------')
         print('\t\tName : ',var[1])
         print('\t\tCourse : ',var[2])
         print('\t\tRoll-no : ',var[3])
         print('\t\tCollege-Name : ',var[5])

         # search book in the databases

         print("\n\t\t******ISSUE BOOKS********")

         while True:

              id=input("\n\t\tEnter Book ID : ")
              ttl = input("\n\t\tEnter Title of Books : ")
              cursor=db.cursor()
              cursor.execute("SELECT * FROM Libr WHERE Book_ID='"+id+"' and  Title='"+ttl+"'")
              var1=cursor.fetchone()
              if var1!=None:
                  print('\t\t----------------------')
                  print("\t\tTitle : ",var1[1])
                  print("\t\tAuthor : ",var1[2])
                  print("\t\tEdition : ",var1[3])


              else:
                  print("\n\t\t-----------> YOUR DATA IS NOT MATCHED !")
                  continue

              ch=input("\n\t\tADD MORE BOOKS (Y/N) : ")
              if ch=="Y" or ch=="y" and max<=3:
                    max+=1
                    continue

              else:
                  break

         date=int(input("\n\t\tEnter days books of purchased : "))
         cursor=db.cursor()
         cursor.execute("UPDATE Libr SET Issue_book='Issued' WHERE Book_ID='"+id+"'")
         db.commit()

         print("\n\t\t------------> BOOKS ISSUE !")

      else:
        print("\t\t---------------> YOUR DATA NOT FOUND !")

   elif choice==3:

       #Edit book data

       print("\n\t\t**********EDIT BOOKS DATA**********")
       nm=input("\n\t\tEnter Name Change of Data(Book_ID,Title,Author,Edition,Price) : ")
       bid=input("\t\tEnter set data : ")
       id=input("\t\tEnter Book ID : ")
       cursor=db.cursor()
       cursor.execute("UPDATE Libr SET '"+nm+"'='"+bid+"' WHERE Book_ID='"+id+"'")
       db.commit()
       print("\n\t\t--------------> YOUR DATA IS UPDATED !")

   elif choice==4:
       # Delete books data

       print("\n\t\t**************DELETE BOOKS DATA***********")
       var=input("\n\t\tEnter Book ID : ")
       cursor=db.cursor()
       cursor.execute("DELETE FROM Libr WHERE Book_ID='"+var+"'")
       db.commit()
       print("\n\t\t----------------> YOUR DATA IS DELETED !")

   elif choice==5:
        # Return books data

       print("\n\t\t***************RETURN BOOKS***************")
       id=input("\n\t\tEnter Book ID : ")
       cursor=db.cursor()
       cursor.execute("UPDATE Libr SET Issue_book='' WHERE Book_ID='"+id+"'")
       db.commit()
       print("\n\t\t---------------------> YOUR BOOK IS RETURN !")


   elif choice==6:
       print("\n\t\t-----------------> YOUR APPLICATION IS CLOSED !")
       break

   else:
      print("\n\t\t-----------------> PLEASE ! YOU CORRECT CHOICE YOUR OPTION")
      continue