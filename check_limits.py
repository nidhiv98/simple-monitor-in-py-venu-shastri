
def battery_is_ok(temperature, soc, charge_rate):
  
    t1=check_temp(temperature)
    s1=check_soc(soc)
    c1=check_charge(charge_rate)
    a1=aggregate_bat(t1,s1,c1)
    return a1
  
  
def aggregate_bat(t,s,c):
   return t and s and c:
 
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
