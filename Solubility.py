
def preguntar(texto):
    pregunta= input(texto)
    while (pregunta != "yes") and (pregunta != "y") and (pregunta != "no") and (pregunta != "yes") and (pregunta != "si") and (pregunta != "n"):
        pregunta= input("\n\nError. Please respond either 'yes' or 'no'.\n"+texto+"\n")
    return pregunta

def isYes(valor):
    return (valor == "yes" or valor == "y" or valor == "si")

def isNo(valor):
    return (valor == "no" or valor == "n")

pregunta1 = preguntar("Is it soluble on water?")

if isYes(pregunta1):
    pregunta2 = preguntar("Is it soluble on ether?")
    print(pregunta2)
    if isYes(pregunta2) :
        print("It is polar and has a short chain, sample belongs to GROUP 1")
    elif isNo(pregunta2) :
        print("It is a salt or polifunctional and belongs to GROUP 2")
elif isNo(pregunta1):
    pregunta3 = preguntar("Is it soluble on NaOH?")
    print(pregunta3)
    if isYes(pregunta3) :
        pregunta4 = preguntar("Is it soluble in NaHCO3?")
        print(pregunta4)
        if isYes(pregunta4) :
            print("The sample is a strong acid and belongs to GROUP IIIA")
        elif isNo(pregunta4) :
            print("The sample is a weak acid and belongs to GROUP IIIB")
    if isNo(pregunta3) :
        pregunta8 = preguntar("Is it soluble in HCl? 5%?")
        if isYes(pregunta8) :
            pregunta9 = preguntar("Is it soluble on buffer AcOH/AcONa pH 5,5?")
            if isYes(pregunta9) :
                print("The sample is a strong base and belongs to GROUP IVA")
            elif isNo(pregunta2) :
                print("The sample is a weak acid and belongs to GROUP IVB")
        elif isNo(pregunta8) :
            pregunta5 = preguntar("Does it have N o S?")
            print(pregunta5)
            if isYes(pregunta5) :
                print("The sample is neutral and belongs to GROUP VII")
            elif isNo(pregunta5) :
                    pregunta6=preguntar("Is it soluble on concentrated sulphuric acid?")
                    print(pregunta6)
                    if isNo(pregunta6) :
                        print("The sample is neutral and does not have N nor S. Belongs to GROUP VI")
                    elif isYes(pregunta6) :
                        pregunta7= preguntar("is it soluble on H3PO4?")
                        print(pregunta7)
                        if isNo(pregunta7) :
                            print("The sample is insaturated and has a high molecular weight it belongs to GROUP VB")
                        elif isYes(pregunta2) :
                            print("The sample is oxigenated and has an intermidiate molecular weight it belongs to GROUP VA")
                                   
g=["group1", "group2", "group3A", "group3B", "group4A", "group4B", "group5A", "group5B", "group6A", "group6B","group7", "Group1", "Group2", "Group3A", "Group3B", "Group4A", "Group4B", "Group5A", "Group5B", "Group6A", "Group6B", "Group7"]
ask = input("What's the samples solubility group?")
while ask not in g:
    ask = input("What's the samples solubility group? Respond in this format: groupnumberA/B")
if ask == "group1":
    print("Sample is polar and of short chain.")
if ask == "group2":
    print("Sample is a salt or polifunctional.")
if ask == "group3A" :
    print("Sample is a strong acid.")
if ask ==  "group3B":
    print("Sample is a weak acid.")
if ask ==  "group4A":
    print("Sample is a strong base.")
if ask == "group4B":
    print("Sample is a weak acid.")
if ask == "group5A":
    print("Sample is oxigenated and has an intermidiate molecular weight.")
if ask == "group5B":
    print("Sample is insaturated and has a high molecular weight.")
if ask == "group6":
    print("Sample is neutral and does not have N or S.")
if ask == "group7":
    print("Sample is neutral compound.")
    

    
    


    

    
        
                
        

    

    

    

    

        