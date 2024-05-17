def grade_predict(co_max, co1,co2,co3,co4,co5,assign):
    
    #calculating the internal marks
    co_avg = (co1+co2+co3+co4+co5)/5
    internal = (co_avg/co_max)*30 + assign
    
    #creating a lambda function that calculates the mark needed to get variable 'a' marks
    #if the marks needed to get is impossible then it returns None
    predictor = lambda i,a : 'ALREADY' if ((a-i)<=0) else ((a-i)/60)*100 if ((a-i)<=60) else 'IMPOSSIBLE'
    
    #Returning a list of predicted marks. [C, B, B+, A, A+, O]
    return [predictor(internal,x) for x in (50,51,61,71,81,91)]


def grade_calc(co_max, co1,co2,co3,co4,co5,assign,final):
    
    #calculating total  40(internal) + 60(final)
    co_avg = (co1+co2+co3+co4+co5)/5
    internal = (co_avg/co_max)*30 + assign
    total = internal + (final/100)*60
    
    #Assingining appropriate grades for the calculated total marks
    if(total<50):
        grade = 'RA'
    elif(total<51):
        grade = 'C'
    elif(total<61):
        grade = 'B'
    elif(total<71):
        grade = 'B+'
    elif(total<81):
        grade = 'A'
    elif(total<91):
        grade = 'A+'
    else:
        grade = 'O'
    
    #returning the calculated total and grade.
    return (total,grade)


def main():
    
    while True:
        
        #Printing a menu
        print("\n\nGrade-Predictor\n\nMain Menu\n1) Predict Grade\n2) Calculate Grade\n3) Exit\n")
        ch = input("Enter your choice (1-3): ")
        
        #Executing functions according to the choice.
        if(ch == '1'):
            try:
                
                co_max = int(input("Enter the Course Outcome Maximum Marks: "))
                co1 =    float(input("Enter the Course Outcome 1 Marks      : "))
                co2 =    float(input("Enter the Course Outcome 2 Marks      : "))
                co3 =    float(input("Enter the Course Outcome 3 Marks      : "))
                co4 =    float(input("Enter the Course Outcome 4 Marks      : "))
                co5 =    float(input("Enter the Course Outcome 5 Marks      : "))
                assign = float(input("Enter the Assignment Marks            : "))
                
                res = grade_predict(co_max,co1,co2,co3,co4,co5,assign)
                
                print("\nPredicted Scores to get in Final Exam:")
                for i in range(6):
                    try:
                        print(['PASS','B','B+','A','A+','O'][i],f": {res[i]:.2f}")
                    except ValueError:
                        print(['PASS','B','B+','A','A+','O'][i],f": {res[i]}")
            except ValueError:
                print("Invalid Input")
                
        elif(ch == '2'):
            try:
                
                co_max = int(input("Enter the Course Outcome Maximum Marks: "))
                co1 =    float(input("Enter the Course Outcome 1 Marks      : "))
                co2 =    float(input("Enter the Course Outcome 2 Marks      : "))
                co3 =    float(input("Enter the Course Outcome 3 Marks      : "))
                co4 =    float(input("Enter the Course Outcome 4 Marks      : "))
                co5 =    float(input("Enter the Course Outcome 5 Marks      : "))
                assign = float(input("Enter the Assignment Marks            : "))
                final =  float(input("Enter the Final Exam Marks            : "))
                
                res = grade_calc(co_max,co1,co2,co3,co4,co5,assign,final)
                print("\nTotal marks:",res[0])
                print("Grade       :", res[1])
                
            except ValueError:
                print('Invalid Input')
            
        elif(ch == '3'):
            print("Exiting the program")
            break
        else:
            print('Invalid Choice')

if(__name__ == '__main__'):
    main()
                    
                