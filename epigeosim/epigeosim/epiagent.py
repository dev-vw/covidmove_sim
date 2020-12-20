import random
from math import floor

class EpiAgent:
    """
    An EpiAgent represents an autonomous person within the epidemic simulation.

    ...

    Attributes
    ----------

    origin_fip : str
    curr_fip : str
    covid_status: int
    r_eff : float
    days_sick : int
    immune_status : int
    spread_day : int
    travel_hist : dict
    
    --UNIMPLEMENTED--
    demog_dict : dict
    prob_ot : float

    Methods
    -------
    """

    # class variable defining transmission rate
    # !TODO: This will probably need to change
    def __init__(self, date, origin_fip, covid_status, r_eff=None):
        """Initialize an agent!

        :param date: 
        :param origin_fip: 
        :param covid_status: 
        :param r_eff: 
        :returns: 
        :rtype: 

        """
        self.origin_fip = origin_fip
        self.curr_fip = origin_fip
        self.travel_hist = {date: self.curr_fip}

        self.covid_status = covid_status
        self.r_eff = r_eff

        if covid_status == 1:
            self.days_sick = 0

            # !TODO!: put more weight on spreading during first 4 days
            # of infection
            self.spread_day = random.choice(range(10))
        else:
            self.spread_day = None
            self.days_sick = None

        self.immune_status = 0

    def set_p_covid(self, origin_fip, poc_df):
        """Sets the probability of contracting covid for the EpiAgent

        Keyword arguments:
        origin_fip : str
        """
        p_covid = poc_df.loc[origin_fip, 'poc']

        return p_covid

    
    def set_disease_state(self):
        """FIXME! briefly describe function

        :returns: 
        :rtype: 

        """        
        pass

    
    def set_travel_state(self):
        pass

    def genpop_random(self, n_pop):
        """Generates a population of EpiAgents of size n_pop. Demographic
        parameters are not specified

        :param n_pop: number of EpiAgents to generate
        :type n_pop: int, required
        :returns: a list of :class: 'EpiAgent' objects
        :rtype: list
        """
        
        return agent_lst
        pass

    
    def genpop_spec(self, n_pop, demog_dict):
        """Generates a population of EpiAgents of size n_pop, according to 
        specified population parameters provided by the dictionary, demog_dict
        :param n_pop:
        :param demog_dict:
        :returns: a list of :class: 'EpiAgent' objects
        :rtype: list
        """

        pass


    def set_pop_demog(self, demog_dict):
        pass

# making the agent population
def gen_pop(df):
    sim_pop = {}
    for index, row in df.iterrows():
        # key for dictionary
        fip = row['county_fips']

        # list of agents for a specific county fip
        fip_pop = []

        ncovid = floor(row['ncovid03222020']) + 1

        print('Beginning fip code: ' + fip)
        if ncovid != 0:
            for j in range(1, ncovid):
                agent = EpiAgent('22-Mar-2020', fip, 1, row['reff03222020'])
                fip_pop.append(agent)
            for k in range(1, row['pop2019']-ncovid):
                agent = EpiAgent('22-Mar-2020', fip, 0)
                fip_pop.append(agent)
        else: 
            for k in range(1, row['pop2019']):
                agent = EpiAgent('22-Mar-2020', fip, 0)
                fip_pop.append(agent)

        print(len(fip_pop))
        sim_pop[fip] = fip_pop
    return sim_pop
