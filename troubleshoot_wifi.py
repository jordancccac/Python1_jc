#Jordan Exercise 17 Troubleshooting a Bad Wi-Fi Connection
#Lead the user through the steps of troubleshooting their Wi-Fi connection



#Display step 1 and get the result
print("Reboot the computer and try to connect.")


answer_1=str(input('Did that fix the problem? '))

if answer_1 == 'yes': 
    print('Congratulations! The connection is fixed.')
    
 #Display step 2 and get the result 
else:
    print('Reboot the router and try to connect.')
    answer_2=str(input('Did that fix the problem? '))
    
    if answer_2 == 'yes':
        print('Congratulations! The connection is fixed.')
        
 #Display step 3 and get the result 
    else:                     
        print('Make sure the cables between the router & modem are plugged \
in firmly.')
        answer_3=str(input('Did that fix the problem? '))
        
        if answer_3 == 'yes':
                print('Congratulations! The connection is fixed.')
                
   #Display step 4 and get the result 
        else:     
                print('Move the router to a new location and try to connect.')
                answer_4=str(input('Did that fix the problem? '))
                
                if answer_4 == 'yes':
                    print('Congratulations! The connection is fixed.')
                    
                #Display step 5
                else:   
                    print('Get a new router.')
                    
                    

   
