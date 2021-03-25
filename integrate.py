#!/usr/bin/python

import xlrd, datetime
import sys
import os

codes_raw = str(sys.argv[1])
checkMonth = str(sys.argv[2])
codes = codes_raw.split(',')

loc = "sharepoint_"+checkMonth+".xls"
sapLoc = "sheetsap_"+checkMonth+".xls"

sharePoint = xlrd.open_workbook(loc)
sheet = sharePoint.sheet_by_index(0)

sap = xlrd.open_workbook(sapLoc)
sapSheet = sap.sheet_by_index(0)

#users = ["Prabhat Singh","Ankur Sawhney","Anurag Gulati","Chetan Sharma","Kushagra Sharma","Shagun Arora","Kartik","Aditya Semwal"]
#codes = ['T002','T006','T017','T007','multi']

#print(sheet.cell_value(1, 0))

#sheet.cell_value(0, 0)

#for i in range(sheet.nrows):
#  for j in range(sheet.ncols):
#    print(sheet.cell_value(i, j))
#  print('\r')

#for i in range(sheet.nrows):

def normalHours(users,a,b):
  sheet.cell_value(a, b)
  for i in range(0,10):
    #print sheet.row_values(i)
    if sheet.row_values(i)[0] in users:
      for j in range(sheet.ncols):
        print(sheet.row_values(0)[j],sheet.row_values(i)[j])

print('lets start')
#normalHours(users,a=0,b=0)

#print(sheet.cell_value(0, 0))
#print xlrd.xldate_as_tuple(sheet.cell_value(0, 0), sharePoint.datemode)

#check Year and Month for Sharepoint sheet
sharePointMonth = xlrd.xldate_as_tuple(sheet.cell_value(0, 0), sharePoint.datemode)[1]
sharePointYear = xlrd.xldate_as_tuple(sheet.cell_value(0, 0), sharePoint.datemode)[0]
print "SharePoint Month: ",sharePointMonth,"\n", "SharePoint Year: ",sharePointYear

#check Year and Month for SAP sheet
SAPmonth = sapSheet.cell_value(10,1)[4]+sapSheet.cell_value(10,1)[5]
print "SAP sheet Month:",int(SAPmonth)

if int(sharePointMonth) == int(SAPmonth):
  print "Month Matches in Both Sheets"
else:
  print "Month in Both Sheets do NOT MATCH"
  exit(1)

def checkCode(codes):
  for row in range(sheet.nrows):
    if sheet.cell_value(row,1) != "" and sheet.cell_value(row,1) in codes:
      print(sheet.cell_value(row,0),sheet.cell_value(row,1))

#checkCode(codes)

def numOfDays():
  max = 0
  for column in range(4,sheet.ncols):
    #print(sheet.cell_value(0,column))
    if type(sheet.cell_value(0,column)) is float:
      if sheet.cell_value(0,column) > max:
        max = sheet.cell_value(0,column)
  return(max)

days = numOfDays()
print "this month has:",int(days),"days"

def checkSapHours(shareDate,shareHours,shareCode,shareName):
  sapSheet = sap.sheet_by_index(0)
  sapHours = 0  #initializing sap hours to 0
  printName = "none"
  printDate = 0
  printCode = "none"
  #multiCode = ["T012","T013","T014"]
  for row in range(0,sapSheet.nrows):
    if str(sapSheet.cell_value(row,0)) == "Engmnt Project ID"
      startRow = row + 1
  for column in range(0,sapSheet.ncolumn):
    if str(sapSheet.cell_value(startRow-1,column)) == "Activity Type":
      activityCell = column
      print "ACTIVITY CELL =",activityCell
    if str(sapSheet.cell_value(startRow-1,column)) == "Full Name":
      nameCell = column
      print "NAME CELL =",nameCell
    if str(sapSheet.cell_value(startRow-1,column)) == "Date":
      dateCell = column
      print "DATE CELL = ",dateCell
    if str(sapSheet.cell_value(startRow-1,column)) == "Hours":
      hourCell = cloumn
      print "HOUR CELL =",hourCell

  for row in range(startRow,sapSheet.nrows):
    sapCode = str(sapSheet.cell_value(row,activityCell))
    if sapCode in shareCode:
      sapDate = int(sapSheet.cell_value(row,dateCell).split('.')[0])
      sapName = str(sapSheet.cell_value(row,nameCell))
      if sapDate == shareDate and sapName == shareName:
        sapHours = sapHours + int(sapSheet.cell_value(row,hourCell))
        printName = sapName
        printDate = sapDate
        printCode = sapCode
  return(printName,printDate,printCode,sapHours)
"""
    if sapCode == shareCode and sapDate == shareDate and sapName == shareName and sapHours == shareHours:
    print "Name:",shareName,printName
    print "Hours Match:",shareHours,sapHours
    print "Date:",shareDate,printDate
    print "Code:",shareCode,printCode
    print "*"*10
  elif sapCode == shareCode and sapDate == shareDate and sapName == shareName and sapHours != shareHours:
    print "Unmached Data Found !!"
    print "**Name**:",shareName,printName
    print "**Hours Match**:",shareHours,sapHours
    print "**Date**:",shareDate,printDate
    print "**Code**:",shareCode,printCode
    print "*"*20
    */
"""


def checkHours(days):
  days = int(days)
  for row in range(sheet.nrows):
    shareCode = [str(sheet.cell_value(row,1))]
    if shareCode != [] and shareCode[0] in codes:
      if 'multi' in shareCode:
        shareCode = ["T012","T013","T014"]
      #else:
        #shareCode = [str(sheet.cell_value(row,1))]
    #if shareCode != "" and shareCode in codes:
      #print sheet.cell_value(row,0)
      for column in range(4,days+4):
        if sheet.cell_value(row,column) == "":
          shareHours = 0
        else:
          shareHours = int(sheet.cell_value(row,column))
        shareDate = column-3
        #shareHours = int(sheet.cell_value(row,column))
        shareName = str(sheet.cell_value(row,0))
        #print "share date:",shareDate,"share Hours:",shareHours,"share Name:",shareName,"share Code:",shareCode
        sapSheet = sap.sheet_by_index(0)
        printName,printDate,printCode,sapHours = checkSapHours(shareDate,shareHours,shareCode,shareName)
        if sapHours != shareHours:
          print "Mismatch in Data:"
          print "Share:",shareName,"Date:",shareDate,"Activity_ID:",' '.join(shareCode),"HoursLogged:",shareHours
          print "SAP  :",printName,"Date:",printDate,"Activity_ID:",printCode,"HoursLogged:",sapHours
          print "*"*20
"""
          if sapHours == shareHours:
            print "match for "
            print shareName,shareDate,shareCode,shareHours
            print "and"
            print printName,printDate,printCode,sapHours
            print "*"*10
"""


checkHours(days)
