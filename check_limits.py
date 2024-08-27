def battery_is_ok(temperature, soc, ch_rate):
  Checking_temperature(temperature)
  Checking_soc(soc)
  Checking_Chargerate(ch_rate)
  
def Checking_temperature(temperature):
  if temperature < 0 or temperature > 45:
    high_low_temperature(temperature)
    print('Temperature is out of range!')
    return False
  else:
    Checking_temperature(temperature)
def high_low_temperature(temperature):
  if temperature >0:
    print('Temperature is High!')
  else:
    print('Temperature is Low.')

def Checking_temperature(temperature):
  if temperature <=2.25 or temperature >42.75:
    Warning_Checking_temperature(temperature)
  else:
    print('Temperature is NORMAL.')
def Warning_Checking_temperature(temperature):
  if temperature <=2.25:
    print('State of Charge is Low Warning!')
  else:
    print('State of Charge is High Warning!')
def Checking_soc(soc):
  if soc <=20 or soc > 80:
    high_low_soc(soc)
  else:
    Checking_soc(soc)
def high_low_soc(soc):
  if soc>20:
    print('State of Charge is High breach!')
  else:
    print('State of Charge is low breach!')
def Checking_soc(soc):
  if soc <25 or soc >75:
    WarningCheck_soc(soc)
  else:
    print('State of Charge is NORMAL.')
def WarningCheck_soc(soc):
  if soc <25:
    print('State of Charge is Low Warning!')
  else:
    print('State of Charge is High Warning!')
def Checking_Chargerate(ch_rate):
  if ch_rate > 0.8:
    print('Charge rate is out of range!')
  else:
    Warning_charge_rate(ch_rate)

def Warning_charge_rate(ch_rate):
  if ch_rate> 0.6:
    print('Charge rate is High Warning!')
  else:
    print('Charge rate is Normal.')
    
if __name__ == '__main__':
  battery_is_ok(25, 70, 0.7)
  battery_is_ok(50, 85, 0)
