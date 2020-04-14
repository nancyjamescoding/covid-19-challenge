import math


def estimator(data):
    time_to_elapse = data['timeToElapse']
    period_type = data['periodType']
    if period_type == 'weeks':
        time_to_elapse = time_to_elapse * 7
    elif period_type == 'months':
        time_to_elapse = time_to_elapse * 30
    else:
        pass

    currently_infected = data['reportedCases'] * 10
    severe_currently_infected = data['reportedCases'] * 50
    power_factor = time_to_elapse // 3
    infections_by_requested_time = currently_infected * 2 ** power_factor
    severe_infections_by_requested_time = severe_currently_infected * 2 ** power_factor

    severe_cases_by_requested_time = infections_by_requested_time * 0.15
    severe_severe_cases_by_requested_time = severe_infections_by_requested_time * 0.15
    total_hospital_beds = data['totalHospitalBeds']
    number_of_available_beds = total_hospital_beds * \
        0.35 - severe_cases_by_requested_time
    severe_number_of_beds_available = total_hospital_beds * \
        0.35 - severe_severe_cases_by_requested_time

    cases_for_icu_by_requested_time = infections_by_requested_time * 0.05
    severe_cases_for_icu_by_requested_time = severe_infections_by_requested_time * 0.05
    cases_for_ventilators_by_requested_time = infections_by_requested_time * 0.02
    severe_cases_for_ventilators_by_requested_time = severe_infections_by_requested_time * 0.02

    average_daily_income_population = data['region']['avgDailyIncomePopulation']
    average_daily_income_in_usd = data['region']['avgDailyIncomeInUSD']
    dollars_in_flight = infections_by_requested_time * average_daily_income_population * \
        average_daily_income_in_usd * time_to_elapse
    severe_dollars_in_flight = severe_infections_by_requested_time * average_daily_income_population * \
        average_daily_income_in_usd * time_to_elapse

    return {
        "data": data,
        "impact": {"currentlyInfected": currently_infected,
                   "infectionsByRequestedTime": infections_by_requested_time,
                   "severeCasesByRequestedTime": math.trunc(severe_cases_by_requested_time),
                   "hospitalBedsByRequestedTime": math.trunc(number_of_available_beds),
                   "casesForICUByRequestedTime": math.trunc(cases_for_icu_by_requested_time),
                   "casesForVentilatorsByRequestedTime": math.trunc(cases_for_ventilators_by_requested_time),
                   "dollarsInFlight": math.trunc(dollars_in_flight)
                   },
        "severeImpact": {"currentlyInfected": severe_currently_infected,
                         "infectionsByRequestedTime": severe_infections_by_requested_time,
                         "severeCasesByRequestedTime": math.trunc(severe_severe_cases_by_requested_time),
                         "hospitalBedsByRequestedTime": math.trunc(severe_number_of_beds_available),
                         "casesForICUByRequestedTime": math.trunc(severe_cases_for_icu_by_requested_time),
                         "casesForVentilatorsByRequestedTime": math.trunc(severe_cases_for_ventilators_by_requested_time),
                         "dollarsInFlight": math.trunc(severe_dollars_in_flight)
                         }
    }
