

def main_event():
    with open('rapport.txt' ,'r',encoding='utf-8' ) as f:
        main_line = []
        for ligne in f :
            if 'WARNING' in ligne or 'ERROR' in ligne :
                main_line.append(ligne)
    main_rapport = 'main event : \n'
    for i in main_line :
        main_rapport += i
    return main_rapport 
