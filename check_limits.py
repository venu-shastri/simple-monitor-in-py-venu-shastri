def print_to_console(out):
  print out
  
def validating_temp(temp):
   if temp < 0 or temp > 45:
    #print('Temperature is out of range !')
    return False
  

def validating_soc(soc):
  if soc < 20 or soc > 80:
    #print('State of Charge is out of range!')
    return False
  
def validating_charge(chrate)
  if charge_rate > 0.8:
    #print('Charge rate is out of range!')
    return False

def battery_is_ok(temp, soc, chrate):
 if validating_temp(temp) and validating_soc(soc) and validating_charge(chrate):
  return true
  else
  return false
  
 
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
