#Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes..
#then add this number to the amount of seconds in 45 minutes and 15 seconds.

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(4000)
print(hours, minutes, seconds)