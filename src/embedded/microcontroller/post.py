import serial 
import time
from supabase import create_client, Client
from dotenv import load_dotenv
from os import environ

ser = serial.Serial('COM8', 9600)
load_dotenv()

SUPABASE_URL = environ.get('SUPABASE_URL')
SUPABASE_KEY = environ.get('SUPABASE_KEY')

while True:
    time.sleep(10)
    data = ser.readline()
    data = data.decode()
    analog_value_gas = data.split(',')[0]
    digi_value_gas = data.split(',')[1]
    analog_value_umi = data.split(',')[2]
    analog_value_temp = data.split(',')[3]
    print('Analog Gas: ', analog_value_gas)
    print('Digital Gas: ', digi_value_gas)
    print('Analog Umi: ', analog_value_umi)
    print('Analog Temp: ', analog_value_temp)
    create_client(SUPABASE_URL, SUPABASE_KEY)
    client = Client(SUPABASE_URL, SUPABASE_KEY)
    client.table('Relatorio').insert([{'max_gas': analog_value_gas, 'min_gas': digi_value_gas, 'max_umi': analog_value_umi, 'max_temp': analog_value_temp}]).execute()



