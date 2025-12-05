#WELCOME
def wel():
    print("*"*37)
    print("* WELCOME USER TO THE RESUME BUILDER*")
    print("*"*37)
    print ("Let's make your professional resume")

# Personal Information
def name():
    
    x = ''
    while True:
        name = input("Full name: ").title()
        if name == "":
            print("This field is required.Please enter a value")
            continue
        x +=  name 
        break
    return x
def email():
    x=''
    while True:
        Email = input("Email ID: ").lower()
        if Email == "":
            print("This field is required.Please enter a value")
            continue
        x += Email 
        break
    return x
def phone():
    x=''            
    while True:
        phone = input("Enter phone Number: ")
        if phone == "":
            print("This field is required. Please enter a value")
            continue
        x += phone
        break
    return x
def sta_cit():
    x = ''
    while True:
        sc = input("Enter (City,State): ").upper()
        if sc == '':
            print("This field is required.")
            continue
        x += sc
        break
    return x

# User summary
def summary():
    print("=== PERSONAL SUMMARY===")
    store = ''
    while True:
        per_detail = input("Write a brief professional summary (2-3 sentences): ").capitalize()
        if per_detail == '':
            return store
        else:
            store +=  per_detail
            return  store
        

# SKILLS 


def skill():
    print("=== SKILLS ===")
    x = []
    print("Enter your skills: ")
    print("(Enter each skill and press Enter. Type 'done' when finished)")
    i = 1
    while True:
        skl = input(f"Skill {i} : ")
        if skl == '':
            continue
            
        if skl == 'done' or skl == 'Done' or skl == 'DONE':
            break
    
        x.append(skl)


        i += 1
        
    return  ', '.join(x)


#EXPERIENCE


def job():
    x=''
    while True:
        job = input("Job title: ").title()
        if job == '':
            print("This field is required.")
            continue
        if job != '':
            x += job  
        break
    return x

def comp():
    x = ''                
    while True:
        company = input('company: ').title()
        if company == '':
            print("This field is required.")
            continue
        if company != '':
            x += company
            break   
    return x

def location():
    x = ''
    while True:
        location = input('Location: ').title()
        if location == '':
            print("This field is required.")
            continue
        if location != '':
            x += location 
            break   
    return x
def jo() :    
    x=''       
    while True:
        join = input("Start Date (e.g., Jan 2025): ").title()
        if join == '':
            print("This field is required.")
            continue
        if join != '':
            x += join
            break   
    return x
def left():
    x =''
    while True:
        end = input('End Date (or \'present\'): ').title()
        if end == '':
            print("This is the required field.") 
            continue
        if end != '':
            x += end
            break 
    return x

def responsibilities():
    x = ''
    print("\nEnter your Responsibilities/ Achievemnts:")
    print("(enter each responsibility and press enter. Type 'done' when finished.)")
    i = 1
    while True:
        res = input(f'Responsibilities {i}: ').lower()
        if res == '':
            continue
        if res == 'done':
            break
        x += '\n '+'-'+res   #To add an emoji
        i += 1
    return x




def start():
    print("===WORK EXPERIENCE===")
    print("how many work experience would you like to add?")

def experience():
    x = ''

    while True:
        try:
            number = int(input("Number of experiences: "))          
            
            if number == 0 :
                break

            for i in range(number):
                print('\n'+f'---Experience {i+1}---')
                x += '\n'
                x += job()+' | '+ comp()+'\n'
                x += location()+ ' | '+ jo()+'-'+left()+' '+responsibilities()+'\n'
                
            break 
        except Exception as e :
            print("Enter an integer value. If you dont want to mention about enter '0'")
            continue
    
    return x



#Education
def Degree():
    print('===EDUCATION===')
    x=''
    while True:
        deg = input('Degree/Certification: ').title()
        if deg == '':
            print('This field is required')
            continue
        if deg != '':
            x +=  deg   
            break
    return x

def Institute():
    x =''
    while True:
        Ins = input('Institution: ').upper()
        if Ins == '':
            print('This field is required')
            continue
        if Ins != '':
            x +=  Ins  
            break 
    return x

def Location():
    x=''
    while True:
        loc = input('Location: ').title()
        if loc == '':
            break
        if loc != '':
            x += loc   
            break 
    return x

def Graduated():
    x=''
    while True:
        gr_date = input('Graduation Date (e.g., May 2020): ').title()
        if gr_date == '':
            print('This field is required')
            continue
        if gr_date != '':
            x += gr_date   
            break
    return x

def GPA():
    x = ''
    while True:
                    
        gpa = input('GPA (optional,press enter to skip):')
        if gpa == "":
            break
        if gpa != '':
            x +=  gpa
            break
    return x


# EDUCATION INFORMATION


def education():
    x = ''


    print('===Education===')
    print('How many degree/certifications would you like to add?')
    while True:
        try:
            degree = int(input('Number of entries: '))
            if degree == 0:
                break

            for i in range(degree):
                print(f"\n---Education {i+1}---")

                x += Degree()+' | '+Institute()+'\n'
                x += Location()+ ' | ' +Graduated()+ ' | '+GPA()+'\n\n'


            break
        except Exception as e :
            print("Invalid input.Try again or type '0' to skip")
            continue

    return x  



#Projects
def Pro():
    i=1
    y = ''
    while True:
        prjt = input(f"\nProject {i}: ").capitalize()
        if prjt == '':
            continue
        if prjt == 'Done':
            break
        y += ' -'+prjt+'\n'
        i +=1
    return y





def project():
    x = ''
    

    print('===PROJECTs (optional)===')
    while True:
        like = input('Would you like to add projects? (yes/no): ').capitalize()
        if like != 'Yes' and like != 'No':
            print("Enter either 'yes' or 'no'")
            continue
        

        if like == 'No':
            return x
        
        if like == 'Yes':
            print('Enter your projects:')
            print("(Enter each project and press Enter. Type 'done' when finished)")

            x += Pro()
        break
    
    return x



import textwrap

#welcome
wel()


N = name()
E = email()
P = phone()
S = sta_cit()
print('\n')
s = summary()
print('\n')
L = skill()
print('\n')
start()
e = experience()
print('\n')
G = education()
print('\n')
PP = project()
print('\n')
#Adding TO FILE


while True:
    save = input('Do you want to save the Resume? (yes/no): ').lower()
    if save == '':
        continue
    if save != 'yes' and save != 'no':
        print("Enter either 'yes' or 'no'.")
        continue
    if save == 'yes':
        print('\n')
        y  = input('Enter the name of the file you want to save your resume into.(eg.Resume.txt etc)')
        if y == '':
            y = 'Resume.txt'
        
        f = open(y,'w')
        f.write('='*80+'\n')
        f.write(N.center(80)+'\n')
        f.write('='*80+'\n')
        f.write((E+' | '+P+' | '+S).center(80))
        f.write('\n\n')
        f.close()
        print('\n')
#SUMMARY

        if s :
            f = open(y,'a')
            f.write("PROFESSIONAL SUMMARY\n")
            f.write('-'*80+'\n')
            wrap = textwrap.fill(s, width = 80)
            f.write(wrap)
            f.write('\n\n')
            f.close()

            print('\n')
#skill

        if L:
            f = open(y,'a')
            f.write('SKILLS\n')
            f.write('-'*80+'\n')
            wrp = textwrap.fill(L, width = 80)
            f.write(wrp)
            f.write('\n\n')
            f.close()
            print('\n')
#Experience

        if e:
            f = open(y,'a')
            f.write('WORK EXPERIENCE\n')
            f.write('-'*80+'\n')
            f.write(e)
            f.write('\n\n')
            f.close()



            print('\n')

#education

        if G:
            f = open(y,'a')
            f.write('EDUCATION\n')
            f.write('-'*80+'\n\n')
            f.write(G)
            f.write('\n\n')
            f.close()


            print('\n')
#PROJECT

        if PP:
            f = open(y,'a')
            f.write('PROJECT\n')
            f.write('-'*80+'\n\n')
            f.write(PP)
            f.write('\n\n')
            f.close()
        print(f" ✅ File saved successfully to the {y} ")
        break
    if save == 'no':
        print("Resume didn't save")
        break







