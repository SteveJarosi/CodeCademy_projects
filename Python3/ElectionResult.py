#import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for i in survey_responses if i == 'Ceballos'])
print(total_ceballos)
percentage_ceballos = total_ceballos*100/len(survey_responses)
print(percentage_ceballos)
possible_surveys = np.random.binomial(
    len(survey_responses), 0.54, 10000) / float(len(survey_responses))
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)
large_survey = np.random.binomial(7000, 0.54, 10000) / float(7000)
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)
