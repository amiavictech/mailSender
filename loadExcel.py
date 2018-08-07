from openpyxl import load_workbook

def get_user_details():
    wb = load_workbook('MemberData.xlsx')
    sheet = wb['Sheet1']
    email_column = sheet['E']
    userName_column = sheet['D']
    adlCnt_column = sheet['G']
    kdCnt_column = sheet['H']
    user_details = []
    # Print the contents
    for x in xrange(len(email_column)): 
        if x > 0:
            user_details.append({
                'email': email_column[x].value,
                'userName': userName_column[x].value,
                'adlCnt': adlCnt_column[x].value,
                'kdCnt': kdCnt_column[x].value
            })
    print (user_details)
    return user_details