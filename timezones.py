from datetime import datetime
import pytz



colombia = datetime.now(pytz.timezone('America/Bogota'))
spain = datetime.now(pytz.timezone('Europe/Madrid'))

print(f'Tiempo en colombia: {colombia.strftime("%Y/%m/%d, %H:%M:%S")}')
print(f'Tiempo en España: {spain.strftime("%Y/%m/%d, %H:%M:%S")}')
