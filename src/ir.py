from lirc import RawConnection

# return the IR command, or None
def get_IR_command():
  try:
    keypress = conn.readline(.0001)
  except:
    keypress=""
            
  if (keypress != "" and keypress != None):
    # keypress format: (hexcode, repeat_num, command_key, remote_id)
    data = keypress.split()
    sequence = data[1]
    command = data[2]
    
    # ignore command repeats
    if (sequence != "00"):
      return None
    
    return command
  return None

# Initialize IR receiver connection
conn = RawConnection()
print("IR receiver ready")
