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
    return(allele_freq)


result = my_wf_model(0.5, 10)
print("allele_frequencies ", result)
num_gens = len(result)
print("number_gens ", num_gens)

#plot allele frequency over time throughout you simulation
gens = []
count = 0
for i in range(num_gens):
        count += 1
        gens.append(count)


x = gens
y = result

fig, ax = plt.subplots()
ax.set_title( "Allele Frequency Over Generations")
ax.plot(x, y, c = "pink")
ax.set_xlabel("Generation")
ax.set_ylabel("Allele Frequency")
plt.tight_layout()
figure = fig.savefig( "WF_allele_freq_generations.png")
plt.show()















