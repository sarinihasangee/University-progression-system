# Date: 21.04.2023



# Intialize the variables
total=120
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
total_count = 0
progress_list = []
trailer_list =[]
retriever_list =[]
exclude_list=[]

# Credit input
while True:
    try:

        # pass credit input
        pass_credit = int(input("Enter the number of credits at pass: "))

        if pass_credit not in range (0,121,20):
            print ("Out of range.")
            continue

        # defer credit input
        defer_credit = int(input("Enter the number of credits at defer: "))

        if defer_credit not in range (0,121,20):
            print ("Out of range.")
            continue

        # fail credit input
        fail_credit = int(input("Enter the number of credits at fail: "))
    
        if fail_credit not in range (0,121,20):
            print ("Out of range.")
            continue

    # ValueError message
    except ValueError:
        print ("Integer required")
        continue

    # Calculating the total of credits
    total_credit = pass_credit + defer_credit + fail_credit

    
    # total check
    if total != total_credit:
         print ("Total incorrect")
         continue

    
    # Prompt for credits
    # progess check
    if pass_credit == 120:
        progress_count += 1
        outcome = "Progress" 
        print ("Progress")
        # append list
        progress_list.append([pass_credit,defer_credit,fail_credit])

    # Progress (module trailer) check
    elif pass_credit == 100:
        trailer_count += 1
        outcome = "Progress (module trailer)" 
        print ("Progress (module trailer)")
        # append list
        trailer_list.append([pass_credit,defer_credit,fail_credit])

     # Do not progress - module retriever check
    elif fail_credit <= 60:
        retriever_count += 1
        outcome = "Module retriever" 
        print ("Do not progress - module retriever")
        # append list
        retriever_list.append([pass_credit,defer_credit,fail_credit])

     # Exclude check
    elif fail_credit >= 80:
        excluded_count += 1
        outcome = "Exclude"
        print ("Exclude")
        # append list
        exclude_list.append([pass_credit,defer_credit,fail_credit])

    print("\n")
    
    # Ask user want to enter another set of data
    user_choice = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    choice_lower = user_choice.lower()

    print("\n")

    # if user want to continue
    if choice_lower == 'y':
        continue

    # if user want to quit
    elif choice_lower == 'q':
        print ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

        # Histogram
        print ("Histogram \nProgress ", progress_count, "  :", "*"*progress_count, "\nTrailer ", trailer_count, "   :", "*"*trailer_count, "\nRetriever ", retriever_count, " :", "*"*retriever_count, "\nExcluded ", excluded_count, "  :", "*"*excluded_count)
        total_count = progress_count + trailer_count + retriever_count + excluded_count 
        print (total_count, " outcomes in total.")
        print ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

        print("\n")

        # print list
        for progress_outcome in progress_list:
            print("Progress  -", ','.join(map(str,progress_outcome)))
            
        for trailer_outcome in trailer_list:    
            print("Progress (module trailer) - ",','.join(map(str,trailer_outcome)))
            
        for retriever_outcome in retriever_list:  
            print("Module retriever - ",','.join(map(str,retriever_outcome)))
            
        for exclude_outcome in exclude_list:    
            print("Exclude   - ",','.join(map(str,exclude_outcome)))

            
        break

    # if enter want a wrong input
    else:
        print ("Incorrect input")
        print("\n")
        user_choice = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        choice_lower = user_choice.lower()

        print("\n")
        continue

    
