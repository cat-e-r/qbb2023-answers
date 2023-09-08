#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Get a starting frequency and a population size
# Input parameters for function


# Make a list to store allele frequencies

# While our allele frequency is between 0 and 1:
#   Get the new allele frequency for next generation
#   by drawing from the binomial distribution
#   convert number of successes into a frequency
#
#   Store our allele frquency in the allele frequency list


# Return a list of allele frequency at each time point
# Number of generations to fixation
# is the length of your list

def my_wf_model(freq, pop):

    allele_freq = []


    while 0 < freq < 1:
        successes = np.random.binomial(2*pop, freq)
        freq = successes/(2*pop)
        allele_freq.append(freq)
    gens = []
    num_gens = len(allele_freq)
    count = 0
    for i in range(num_gens):
        count += 1
        gens.append(count)
    return[gens, allele_freq]



# print("allele_frequencies ", result)
# num_gens = len(result)
# print("number_gens ", num_gens)

#plot allele frequency over time throughout you simulation



fig, (ax1, ax2) = plt.subplots(2)
ax1.set_title( "Allele Frequency Over Generations")
ax1.set_xlabel("Generation")
ax1.set_ylabel("Allele Frequency")

gens_to_fix = []
for iteration in range(1500):
    result = my_wf_model(0.5, 150)
    x = result[0]
    y = result[1]
    ax1.plot(x, y)
    gens_to_fix.append(len(result[0]))

ax2.set_title("Histogram of Generations to Fixation")
ax2.set_xlabel("Gnerations to Fixation")
ax2.set_ylabel("Occurances")
ax2.hist(gens_to_fix)



plt.tight_layout()
figure = fig.savefig( "with_hist_WF_allele_freq_generations.png")
plt.show()














