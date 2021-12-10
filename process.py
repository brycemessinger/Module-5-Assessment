log_file = open("um-server-01.txt")
#above code opens the "um-server-01.txt" file allowing us to later interact with it through the variable name "log file"

def sales_reports(log_file):
    #'def' defines 'sales_reports' as a function that is invoking the um_server document through 'log_file' 
    for line in log_file:
        #line 6 starts a for loop naming it 'line'
        line = line.rstrip()
        #line 8 removes trailing characters after what is declared in line 10
        day = line[0:3]
        #line 10 sets new vairable 'day' only to values between index at 0 and index at 5
        if day == "Tue":
            print(line)
            #lines 12 and 13 print the current index in the loop only if the day is = to "Tue"


sales_reports(log_file)
# above code runs function sales_report with log_file passed in as the argument.
