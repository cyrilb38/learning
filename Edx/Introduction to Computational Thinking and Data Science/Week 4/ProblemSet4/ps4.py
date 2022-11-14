# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    f, ax = pylab.subplots(4, 1, sharex=True)
    plot = 0    
    
    for cas in [300,150,75,0]:
            
        virusAtTimeT = [[]]
        for i in range(numTrials):
            viruses = []
            for j in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))
            patou = TreatedPatient(viruses,maxPop)
            for t in range(cas):
                patou.update()
                if len(virusAtTimeT) -1 < t:
                    virusAtTimeT.append([])
                virusAtTimeT[t].append(len(patou.getViruses()))
            
            #ajout du guttagonol
            patou.addPrescription("guttagonol")
        
            for t in range(cas,cas+150):
                patou.update()
                if len(virusAtTimeT) -1 < t:
                    virusAtTimeT.append([])
                virusAtTimeT[t].append(len(patou.getViruses()))

        ax[plot].hist(virusAtTimeT[t])
        plot += 1

    pylab.show


#simulationDelayedTreatment(1000)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False,
                   'grimpex' : False}
    mutProb = 0.005

    f, ax = pylab.subplots(4, 1, sharex=True)
    plot = 0    
    
    for cas in [300,150,75,0]:
            
        virusAtTimeT = [[]]
        
        for i in range(numTrials):            
            viruses = []
            for j in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))
            patou = TreatedPatient(viruses,maxPop)

            for t in range(150):
                patou.update()
                if len(virusAtTimeT) -1 < t:
                    virusAtTimeT.append([])
                virusAtTimeT[t].append(len(patou.getViruses()))     

            #ajout du guttagonol
            patou.addPrescription("guttagonol")                   
            
            for t in range(150, cas + 150):
                patou.update()
                if len(virusAtTimeT) -1 < t:
                    virusAtTimeT.append([])
                virusAtTimeT[t].append(len(patou.getViruses()))
            
            #ajout du guttagonol
            patou.addPrescription("grimpex")
        
            for t in range(cas + 150, cas + 300):
                patou.update()
                if len(virusAtTimeT) -1 < t:
                    virusAtTimeT.append([])
                virusAtTimeT[t].append(len(patou.getViruses()))

        ax[plot].hist(virusAtTimeT[t])
        plot += 1

    pylab.show

simulationTwoDrugsDelayedTreatment(1000)