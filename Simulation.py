
#Step 3: Simulation loop

# set the time range for the simulation
from datetime import timedelta, date
from numpy import random 
'''
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 6, 20)
end_date = date(2020, 11, 10)

# main loop for simulation
import math

for date in daterange(start_date, end_date):
    print('Day of simulation: ' + date.strftime("%Y-%b-%d"))
    
    # for each date, go through entire population list
    for key, value in pop_06007and06009.items():
        for agent in value:
            # 1: determine next county for travel
            # determine where they go next, based on where they are now (curr_county)
            p_dict = move_dat[(move_dat['date_range_start'] == start_date.strftime("%Y-%m-%d")) & (move_dat['county_fip'] == test_agent.curr_fip)].pvisit_dict.reset_index(drop=True)[0]

            county_lst = list(p_dict.keys())
            prob_lst = list(p_dict.values())
            
            next_county = random.choice(county_lst)
            
            # update travel_history to include curr_county
            agent.travel_hist[date] = agent.curr_fip
            agent.fip_county = next_county


            # 2: update agent attributes
            # first check to see if immune_status == 0
            # if immune_status == 1, do nothing
            if agent.immune_status == 0:
                # check to see if covid_status == 1
                if agent.covid_status == 1:
                    # check to see if days_sick == spread_day
                    if agent.days_sick == agent.spread_day:
                        # if yes, update the ncovid count of the curr_county to, ncovid = ncovid + r_eff
                        ca_county_dict[agent.curr_fip].n_covid += agent.r_eff 
                    # check to see days_sick == 10
                    # if yes, make immune_status = 1, covid_status = 0
                    if agent.days_sick == 10:
                        agent.immune_status = 1
                        agent.covid_status = 0
                # if covid_status == 0, use POC of curr_fip to see if the agent gets sick
                else:
                    curr_poc = prob_oc_dat.loc[agent.curr_fip, date.strftime("%d-%b-%Y")]
                    if curr_poc > 0:
                        has_covid = random.binomial(1, curr_poc)
                    else:
                        has_covid = 0
                    # at this point, covid_status may == 1
                    # now, update choose a spread_day
                    # also, begin days_sick, change from None to 0
                    if has_covid == 1:
                        agent.covid_status = 1
                        agent.spread_day = random(range(0,10))
                        agent.days_sick = 0
'''




for key, value in ca_county_dict.items():
    print(value.n_covid)




# death_day = randomly chosen day between 1 and 10 and greater or equal to spread_day
# add self.death_day to epiagent.py as
## self.death_day = random.choice(range(days_sick, 30))
                                
            # 2: update agent attributes
            # first check to see if immune_status == 0
            # if immune_status == 1, do nothing
            if agent.immune_status == 0:
                # check to see if covid_status == 1
                if agent.covid_status == 1: # infected
                    died = random.binomial(1, 0.0164) # death rate in cali is around 0.016399 NYTimes
                if died == 1:
                    population -= 1 # what is popuation?
                        
                


                        
