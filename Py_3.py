import re
N = int(input())
  
for i in range(N):
    ticket_no, flight_id, boarding_no, seat_no = input().split(',')
    flight_id = int(flight_id)
    boarding_no = boarding_no.replace('Номер:','')
    seat_no = seat_no.replace(';','')
    seat_no = re.sub(r'\d(?![_\d\W])|[^_\d\W](?!\D)', r'\g<0> ', seat_no, flags = re.UNICODE)
    mesto, ryad = seat_no.split()
    mesto = int(mesto)
    if mesto<0:
        continue
    if mesto>300:
        continue
    print(f'{ticket_no},{flight_id},{boarding_no},{mesto};{ryad}')