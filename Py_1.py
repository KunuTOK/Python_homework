data = int(input())

for i in range(data):
   [book_ref,book_date,total_amount]= input().split(',')
   [rub,cop]=total_amount.split('.')
   print(f'Номер бронирования {book_ref}, забронирован {book_date}. Цена: {rub} руб. {cop} коп.') 