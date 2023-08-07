'''file=open('mail-spam-data','w')     # This code is written to make the file using python only
file.close()
file1=open('mail-checker','w')  # This code is written so that another file for mail data entry could be entered
file1.close'''


def long_streak(a,b):
    '''This is a function which will determine the longest streak of similar strings, and will append it in a list'''
    A=[]  # An empty list which will contain all the similar strings, in which longest will be the first element of the list
    for i in range(1, len(a) + 1):  # This will be the range of j in next iteration
        for j in range(i):  # This will be the index of string from where the common part starts
            if a[j:len(a) - i + j + 1] in b:  # It will check that whether the string from j to the ending, and then for reduced ending, is the string same or not
                A.append(a[j:len(a) - i + j + 1])  # It will append all the possible similar strings in a and b
                break  # Break so that for one matching string, it do not append subparts of that string
    # print(len(A[0]),len(a))
    # print(A)
    if len(A[0])==len(a)-3:  # as per our database the elements are stored with '0, ' type format which is not to be checked so we check if length of it is 3- the original
        # print(A,a)
        return 1      # It gives 1 as output which is used as indication to start or not
    elif A[0]=='.':
        return 1      # It gives 1 as output which is used as indication to start or not
    else:
        return 0      # If no common string is found, 0 is taken as output

def spam_or_ham_check(filename):
    '''This is the main function which is used to run the given file for the spam or ham check'''
    file = open('mail-spam-data.csv', 'r')   # This is used to access our database which contains the information for spam or ham mail
    f = file.readlines()    # Each line is read by this for the check
    file1 = open(filename, 'r')   # It is used to access the file which is to be checked
    f1 = file1.read()     # reads and stores the text inside that file
    c = f1.split()    # each line is stored as text in a list as an element
    s = ''    # Empty string which is used to store the complete mail as a single line(string)
    for i in c:  # Iteration going over each element of list c
        s = s + ' ' + i   # adding each element with space in last for next element
    s = s.lower()    # Taking the mail body as lowercase string as database contains all input in lower case
    for i in range(len(f)):    # Goes for each element in the database list
        if long_streak(f[i], s) == 1:    # If common part is there the function defined above will pass 1
            if f[i][0] == '1':    # As according to our database, if the starting element is 1 then the mail is a ham mail
                print('ham')
                break    # break is used so that once it is recognised that mail is ham then it do not go further to check for other cases
            elif f[i][0] == '0':   # Database contains spam mail starting with 0, so this case
                print('spam')
                break    # similar reason for break case here
            else:    # as if nothing is common then a fullstop must be there which is common, so there it procedds as further,
                # this case is given so that our mail spam checker do not fail in any case, whatsoever is the mail
                print('might be spam or ham')
        else:
            pass
spam_or_ham_check('[students] Academic calendar event(s) alert.eml')