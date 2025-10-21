

while True:
    print("Please Ask the question")
    question = input(">")
    print("\n Please Enter the questions now")
    Answer1 = input(">")
    Answer2 = input(">")
    Answer3 = input(">")
    Answer4 = input(">")
    print('''Whitch is correct
'''+Answer1+'''
'''+Answer2+'''
'''+Answer3+'''
'''+Answer4+'''
    ''')
    ThatOne = input(">")
    if ThatOne == 1:
        print('''
1. '''+question+'''
    - <span style="color:green; font-weight:bold">'''+Answer1+'''✅</span> 
    
        ''')
        
