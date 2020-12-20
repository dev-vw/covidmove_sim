#!/usr/bin/env python

class SimMap:
    """
    Attributes
    ----------
    
    Methods
    -------
    """

    def __init__(self, r_eff_lst, prob_oc_lst):
        pass

    def increase_timestep(self, t_unit):
        """increases the timestep of the simulation map by a day or week 
        (specified by t_unit)

        :param t_unit: 'day', or 'week'
        :type t_unit: str, required
        :returns: None
        :rtype: None

        """
        pass

    # EXTENDED SIMULATION
    # def set_adjacency_matrix(self, travel_date):
    #     """Creates an adjacency matrix based on specified destination county FIPs.
    #     Adjacency matrix is created with time in mind. For example, travel paths from 
    #     Marin County to Inyo County cannot pass through Sonora or Tioga Pass during 
    #     winter months (road closures).

    #     :param travel_date: 
    #     :type travel_date: datetime, required
    #     :returns: dict of two adjacency matrices
    #     :rtype: dict

    #     """
    #     pass

    def set_population_prevalence_in_simmap(self, date):
        """FIXME! briefly describe function

        :returns: 
        :rtype: 

        """
        pass
        
class County:
    """
    Attributes
    ----------

    county_fip : str, county FIP code
    population : total number of people living in this county
    n_covid : int, number of people with COVID in this county
    n_healthy : number of people who are healthy in this county
    prob_oc : float, probability of contracting COVID in a given county
    
    Methods
    -------
    """

    # eventually add a county_demog variable to reflect the demographic
    # characteristics of a county
    def __init__(self, date, county_fip, prob_oc, pop, n_covid):
        # set all the initializing variables
        # !TODO!: build a way to check types
        self.date = date
        self.county_fip = county_fip
        self.prob_oc = prob_oc
        self.pop = pop
        self.n_covid = n_covid
        self.n_healthy = pop - n_covid

        # begin the covid case history (covid_dict), 
        self.covid_hist = {date : n_covid}

        # begin the prob_oc dict
        self.prob_oc_hist = {date : prob_oc}

    def change_county_prob_oc(self, date, prob_oc_upt):
        """Given a date, County's new prob_oc attributes are updated. The prob_oc

        :param date: 
        :param prob_oc_upt: 
        :returns: None 
        """
        # update prob_oc_upt
        self.prob_oc = prob_oc_upt

        # update prob_oc_hist
        self.prob_oc_hist[date] = prob_oc_upt
        
    def change_county_n_covid(self, date, n_covid_upt):
        """Given a date, County's new n_covid, n_healthy are updated. The
        covid_history dictionary is also updated.

        :param date: 
        :param prob_oc_upt: 
        :returns: None
        """
        # update n_covid and n_healthy
        self.n_covid = n_covid_upt
        self.n_healthy = self.pop - self.n_covid

        # update covid_hist
        self.covid_hist[date] = n_covid_upt

    def show_county_stats(self):
        print('County FIP code: ' + self.county_fip)
        # print('Number of total COVID cases in county:' + self.n_covid)
        print('Current probability of contracting COVID (POC): ' + str(self.prob_oc))
        print('Total population of the county: ' + str(self.pop))

    # NOT-YET-IMPLEMENTED
    def plot_prob_oc_timeseries():
        pass

    def plot_covid_case_timeseries():
        pass
    
    def set_population_prevalence_in_county(self, date):
        """given a listing of the number of COVID infections in the county on a given 
        day, returns a dictionary showing the (1) prevalence of infection in the 
        county on a given day, (1) the number of people in the simulated
        population who are infected per county on a given day, and (2) the number of 
        people in the simulated population who are not infected in this county on a 
        given day.

        :returns: 
        :rtype: 

        """
        pass
        # call 
