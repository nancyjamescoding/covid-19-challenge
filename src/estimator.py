import math

def estimator(data):
  time_to_elapse = data.timeToElapse
  period_type = data.periodType 
  if period_type == 'weeks':
    time_to_elapse = time_to_elapse * 7
  elif period_type == 'months':
    time_to_elapse = time_to_elapse * 30
  else:
    pass 

  currently_infected = data.reportedCases * 10 
  severe_currently_infected = data.reportedCases * 50 
  power_factor = time_to_elapse // 3
  infections_by_requested_time = currently_infected * 2 ** power_factor
  severe_infections_by_requested_time = severe_currently_infected * 2 ** power_factor

    
  return data
