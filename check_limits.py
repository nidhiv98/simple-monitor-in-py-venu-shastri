
def battery_is_ok(temperature, soc, charge_rate):
  '''if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  elif soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
   return True'''
    t1=check_temp(temperature)
    s1=check_soc(soc)
    c1=check_charge(charge_rate)
    aggregate_bat(t1,s1,c1)
  
  def aggregate_bat(t,s,c)
    if t and s and c:
      return True
    return False
  
  


def check_temp(t):
  if temperature < 0 or temperature > 45:
    return False
   return True
  
def check_soc(s):
  if  soc < 20 or soc > 80:
    return False
   return True
  
def check_charge(c):
  if   charge_rate > 0.8:
    return False
   return True
 
  
def print_toConsole(msg):
  print(msg)
  

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
