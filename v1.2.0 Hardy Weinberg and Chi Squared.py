#This is my Hardy-Weinberg + Chi Squared calculator via python script enjoy - Sid Gale

###Install SciPy which allows us to do and modify chi squared
#from scipy.stats import chisquare
##Set mah variables

#'Observed' vars
n = 0 #n is the total population value
p = 0
q = 0
ps = 0
qs = 0
pq = 0
oc = 0 #Obersved combined is same as ec but observed numbers instead. (i work in strange ways ok)

#'Expected' vars
eps = 0
eqs = 0
epq = 0
ec = 0 #Expected combined (ec) is the combination of eqs and epq (Wild/Mutant + Mutant/Mutant genotypes)

##Chi Squared vars
#Difference vars
dps = 0
dqs = 0
dpq = 0
#Chi vars
pschi = 0
cochi = 0
totchi = 0

###########################
print(

"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄                         ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌                       ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌                       ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                       ▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌      ▄▄▄▄▄▄▄▄▄▄▄      ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀      ▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌ ▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌          ▐░▌     ▐░▌                            ▐░▌▐░▌ ▐░▌▐░▌▐░▌               ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌                            ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌                            ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀                              ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                                                                                   
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                   
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                  
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀                   
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌                       
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌                       
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌                       
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀      ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌                       
▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌               ▐░▌▐░▌          ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌                       
▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌      ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░▌               ▐░▌                       
▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌               ▐░▌                       
 ▀                 ▀            ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀                 ▀                        
                                                                                                                                                                                   
 ▄▄▄▄▄▄▄▄▄▄   ▄         ▄                 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄                                           
▐░░░░░░░░░░▌ ▐░▌       ▐░▌               ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌                                          
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌               ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀                                           
▐░▌       ▐░▌▐░▌       ▐░▌               ▐░▌               ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌                                                    
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌               ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌       ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄                                           
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌               ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌                                          
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀                 ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀                                           
▐░▌       ▐░▌     ▐░▌                              ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌                                                    
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌                     ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄                                           
▐░░░░░░░░░░▌      ▐░▌                    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                          
 ▀▀▀▀▀▀▀▀▀▀        ▀                      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                           
"""

)




###########################
## Must define math features wooooo

infoa = 'placeholder'
info_dpoint = "Decimal rounding is only done on the final shown value. Calculations are done in full. \n So as it seems, rounding to significant figures is quite a difficult computational task. You can code a workaround using log10 im just not sure how. So rounding will have to do."
print("Math definitions: ")
print("Would you like more info about the rounding method used?")

#Info checker which took wayyyy longer than it needed for me to get it work.
def info9():
    infoa = input("Type 'Y' or 'N': ").lower()
    infocheck2(infoa)

def info9b():
    infoa = input("Type 'Y' or 'N': ").lower()
    infocheck2(infoa)

def infocheck2(infoa):
    if infoa not in ['y', 'n', 'Y', 'N']:
        print("Please try again. 'Y' or 'N' only.")
        info9b()  # Retry if input is invalid
    elif infoa in ['y', 'Y']:
        print(info_dpoint)
        return
    elif infoa in ['n', 'N']:
        return
info9()

print("#################################################################################################")
dpoint = int(input("What decimal point would you like to round to? (Whole numbers only) : "))
print("Decimal point chosen to round to: ",dpoint)


######################################################################################################
## Attempt 1 on a DoF choosing method lies below

'''dfreedom = '1'

#Info checker which took wayyyy longer than it needed for me to get it work.
def dfreedom9():
    global dfreedom
    dfreedom = str(input("Input degrees of freedom for chi squared. Default = 1. Must be a whole number between and including 1 - 5 or may not work. DDOF: "))
    infocheck2(dfreedom)

def dfreedom9b():
    dfreedom = str(input("Input degrees of freedom for chi squared. Default = 1. Must be a whole number between and including 1 - 5 or may not work. DDOF: "))
    infocheck2(dfreedom)

def infocheck2(dfreedom):
    if dfreedom not in ['1', '2', '3', '4', '5']:
        print("Please try again. Numbers 1 - 5 only.")
        dfreedom9b()  # Retry if input is invalid
    elif dfreedom == '1':
        dfreedom = 1
        print(dfreedom)
        return
    elif dfreedom == '2':
        dfreedom = 2
        print(dfreedom)
        return
    elif dfreedom == '3':
        dfreedom = 3
        print(dfreedom)
        return
    elif dfreedom == '4':
        dfreedom = 4
        print(dfreedom)
        return
    elif dfreedom == '5':
        dfreedom = 5
        print(dfreedom)
        return
dfreedom9()

print("Degrees freedom selected: ",dfreedom)'''

######################################################################################################



print("#################################################################################################")

# Ask for input
n = float(input("Total population size: "))
ps = float(input("Observed P^2: "))
qs = float(input("Observed Q^2: "))
pq = float(input("Observed 2PQ "))

###########################
### Maths time
#Work out P and Q
p = (ps+(pq/2))/n
q = (qs+(pq/2))/n
print("Your P value is: ",round(p, dpoint))
print("Your Q value is: ",round(q, dpoint))
print("#################################################################################################")

#Work out the expected values
eps = (p**2)*n
eqs = (q**2)*n
epq = (2*(p*q))*n
ec = eqs+epq
print("Your expected P^2 is: ",round(eps, dpoint))
print("Your expected Q^2 is: ",round(eqs, dpoint))
print("Your expected 2PQ is: ",round(epq, dpoint))
print("Your Q^2 + 2PQ is: ",round(ec, dpoint))
print("#################################################################################################")

#Work out the differences for chi squared
oc = qs+pq
dps = ps-eps
dqs = qs-eqs
dpq = pq-epq
dc = oc-ec
print("Your P^2 difference is: ",round(dps, dpoint))
print("Your Q^2 difference is: ",round(dqs, dpoint))
print("Your 2PQ difference is: ",round(dpq, dpoint))
print("Your combined (2PQ + Q^2) difference is: ",round(dc, dpoint))
print("#################################################################################################")

#Now do chi squared
pschi = (dps**2)/eps
cochi = (dc**2)/ec
totchi = pschi+cochi
print("The P^2 chi value is: ",round(pschi, dpoint))
print("The combined-genotypes chi value is: ",round(cochi, dpoint))
print("The total chi value is: ",round(totchi, dpoint))
print(totchi)
print("#################################################################################################")


##Chi squared table again?
observed = [ps, oc]
expected = [eps, ec]
def calculate_chi_square(observed, expected):
    chi_square_statistic = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    return chi_square_statistic 

print("Critical values are for a significance value of 0.05")
critical_values = {
    1: 3.841,  # df = 1
    2: 5.991,  # df = 2
    3: 7.815,  # df = 3
    4: 9.488,  # df = 4
    5: 11.070  # df = 5
}

chi_square_statistic = calculate_chi_square(observed, expected)

dof = len(observed) - 1 #This results in DoF being '1', adjust accordingly for now if need a different DoF
critical_value = critical_values.get(dof)
print("The Degrees of Freedom set is currently stuck at 1. You can edit it in the code accordingly if a different DoF is needed.")
print(f"Chi-Square Statistic: {chi_square_statistic}")
print(f"Critical Value (at significance=0.05, df={dof}): {critical_value}")
if critical_value is None:
    print(f"Error: Critical value for degrees of freedom {dof} is not available.")
else:
    if chi_square_statistic > critical_value:
        print("Reject the null hypothesis (significant result).")
    else:
        print("Fail to reject the null hypothesis (not significantly different).")
