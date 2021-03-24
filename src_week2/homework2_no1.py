list_transaction=[]


def fnc_insert_data(param_id):
    print("=============================================")
    print("██╗███╗░░██╗░██████╗███████╗██████╗░████████╗")
    print("██║████╗░██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝")
    print("██║██╔██╗██║╚█████╗░█████╗░░██████╔╝░░░██║░░░")
    print("██║██║╚████║░╚═══██╗██╔══╝░░██╔══██╗░░░██║░░░")
    print("██║██║░╚███║██████╔╝███████╗██║░░██║░░░██║░░░")
    print("╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░")
    print("=============================================")
    dict_transaction={}
    dict_transaction['id_transaction']=param_id
    dict_transaction['title']=input(str("Title : "))
    dict_transaction['price']=input(str("Ticket Price : "))
    dict_transaction['transaction']=input(str("Total Transaction : "))
    inp_cities=input(str("Cities (Separated by comma(,)): "))
    list_city=[]
    for city in range(len(str.split(inp_cities,","))):
        list_city.append(str.split(inp_cities,",")[city])
    dict_transaction['cities']=list_city
    list_transaction.append(dict_transaction)

def fnc_check_transaction():
    # print("check transaction")
    print("================================================")
    print("▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█")
    print("░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ ░█░ █ █▄█ █░▀█")
    print("================================================")
    for transact in list_transaction:
            print("Tiket film {} terjual sebanyak {} dengan total pendapatan {} di kota {}"
            .format(transact['title'],transact['transaction'],int(transact['transaction'])*int(transact['price']),tuple(transact['cities'])))
        
choose_menu = 9
id_movie=0

while(choose_menu != 3):
    try:
        print("=====================================")
        print("███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
        print("████╗░████║██╔════╝████╗░██║██║░░░██║")
        print("██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
        print("██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
        print("██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
        print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░")
        print("=====================================")
        print("1. Insert Movie Data")
        print("2. Check Transaction")
        print("3. Exit")
        inp_menu=input(str("Choose Menu : "))
        choose_menu=int(inp_menu)
        if(choose_menu >= 1 and choose_menu<=3):
            if(choose_menu==1):
                id_movie = id_movie+1
                fnc_insert_data(id_movie)
            elif(choose_menu==2):
                fnc_check_transaction()
            else:
                break
        else:
            print("Menu only 1,2,3")
            choose_menu=9
    except ValueError:
        print("Please input valid number")
        choose_menu=9