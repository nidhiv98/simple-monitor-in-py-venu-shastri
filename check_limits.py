
def battery_is_ok(temperature, soc, charge_rate):
    temperature_check=check_temp(temperature)
    soc_check=check_soc(soc)
    charge_check=check_charge(charge_rate)
    aggregate_check=aggregate_bat(temperature_check,soc_check,charge_check)
    return aggregate_check
  
  
def aggregate_bat(temperature_check,soc_check,charge_check):
   return temperature_check and soc_check and charge_check
 
def check_temp(temperature):
    if temperature < 0 or temperature > 45:
        return False
    return True
  
def check_soc(soc):
    if  soc < 20 or soc > 80:
        return False
    return True
  
def check_charge(charge_rate):
    if   charge_rate > 0.8:
        return False
    return True
 
  
def print_toConsole(msg):
  print(msg)
  

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
