class Star_Cinema :
    __hall_list = []

    def  entry_hall(self) :
        Star_Cinema.__hall_list.append(self)
    


class Hall(Star_Cinema):
    
    def __init__(self, hall_no, rows, cols) -> None:
        self.__hall_no = hall_no
        self.__rows = rows
        self.__cols = cols
        self.__seats  = {}
        self.__show_list = []
        self.entry_hall()
        # super().__init__()
    
    

    def entry_show(self, id, movie_name, time) :
        sh = (id, movie_name, time)
        self.__show_list.append(sh)
        
        seats = [["F" for _ in range(self.__rows)] for _ in range(self.__cols)]

        self.__seats[id] = seats

        # print(f'{id} \n {self.__seats[id]}')
         
        

    def book_seats(self, id, row, col) :
        if self.__seats.get(id) is not None :
            if not (0 <= row < self.__rows) or not (0 <= col < self.__cols):
                print('\nInvalid seat')
            
            elif self.__seats[id][row][col] == 'B' :
                print('\nYour chosen seat has already been booked !')
            
            # print((self.__seats[id]))
            else :
                
                if self.__seats[id][row][col] == 'F':
                    self.__seats[id][row][col] = 'B'
                    print(f'\nSeat {(row, col)} have been successfully booked for the show {id}')
                    
        else:
            print('\nInvalid Show Id')
                    


    def view_show_list(self) :
        print(f'\n---------------------------SHOW LIST FOR HALL {self.__hall_no}-----------------------------\n')
        for sh in self.__show_list :
            print(f'MOVIE ID : {sh[0]}  MOVIE NAME : {sh[1]}  TIME : {sh[2]}\n')

        print('\n-------------------------------------------------------------------------------------') 

    def view_available_seats(self, show_id) :
        print('\n--------------------AVAILABLE SEATS--------------------\n')

        if show_id in self.__seats:
            print(f'Upadate available seats matrix for Hall {self.__hall_no}\n')
            # print(self.__seats[show_id])
            for i in range(self.__rows) :
                for j in range(self.__cols):
                    print(self.__seats[show_id][i][j],end=' ')
                print()
        else :
            print('Invalid show Id')
        
        print('--------------------------------------------------------\n')




s1 = Hall(101,7,7)
s2 = Hall(102,7,7)
s1.entry_show('#1b','Jawan','2.11.23 at 11.00am')
s1.entry_show('#2n','Spider','2.11.23  at 1.00pm')
s2.entry_show('#3x','Avatar 3','2.11.23 at 11.00am')
s2.entry_show('#4p','A Million Miles Away','2.11.23  at 1.00pm')




while True :
    print("\nOPTIONS:\n")
    print("1: VIEW ALL SHOW TODAY")
    print("2: VIEW AVAILABLE SEATS")
    print("3: BOOK TICKET")
    print("4: EXIT")

    op = int(input("\nENTER OPTION: "))

    if op == 1 :
        hall_no = int(input('ENTER THE HALL NO : '))
        if hall_no == 101 :
            s1.view_show_list()
        elif hall_no == 102 :
            s2.view_show_list()

    elif op == 2 :
        hall_no = int(input('ENTER THE HALL NO : '))
        show_id = input('ENTER SHOW ID : ')
        if hall_no == 101 :
            s1.view_available_seats(show_id)
        elif hall_no == 102 :
            s2.view_available_seats(show_id)
        else :
            print(f'Invalid hall no {hall_no}!!')
        
    elif op == 3 :
        hall_no = int(input('ENTER THE HALL NO : '))
        id = input('ENTER SHOW ID :')
        row = int(input('ENTER SEAT ROW : '))
        col = int(input('ENTER SEAT COLLUM : '))
        if hall_no == 101 :
            s1.book_seats(id, row, col)
        elif hall_no == 102 :
            s2.book_seats(id, row, col)
        else :
            print(f'Invalid hall no {hall_no}!!')

    elif op == 4 :
        break

    else :
        print('Wrong Option!!\n')
        

