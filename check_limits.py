def print_to_console(out):
  return out
  
def validating_temp(temp):
   if temp < 0 or temp > 45:
    return False
  else:
    return True
  

def validating_soc(soc):
  if soc < 20 or soc > 80:
    return False
  else:
    return True
  
  
def validating_charge(chrate)
  if charge_rate > 0.8:
    return False
    else:
    return True

def battery_is_ok(temp, soc, chrate):
 validating_temp(temp) and validating_soc(soc) and validating_charge(chrate):
  
  
 
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is False)
  assert(battery_is_ok(50, 85, 0) is True)
