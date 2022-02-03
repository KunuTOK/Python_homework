import re
import pandas as pd

N = int(input())

ticket_no_df = []
flight_id_df = []
boarding_no_df = []
seat_no_df = []

for i in range(N):
    ticket_no, flight_id, boarding_no, seat_no = input().split(',')
    flight_id = int(flight_id)
    boarding_no = boarding_no.replace('Номер:','')
    seat_no = re.sub(r'\d(?![_\d\W])|[^_\d\W](?!\D)', r'\g<0> ', seat_no, flags = re.UNICODE)
    ticket_no_df.append(ticket_no)
    flight_id_df.append(flight_id)
    boarding_no_df.append(boarding_no)
    seat_no_df.append(seat_no)

slovar = {
    'ticket_no': ticket_no_df,
    'flight_id': flight_id_df,
    'boarding_no':boarding_no_df,
    'seat_no':seat_no_df
}
df = pd.DataFrame(slovar)
df_no_dub = df.drop_duplicates(subset=['ticket_no', 'flight_id'], keep='first')
spisok = df_no_dub.values.tolist()

for a in range(len(spisok)):
    ticket_no, flight_id, boarding_no, seat_no = spisok[a]
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