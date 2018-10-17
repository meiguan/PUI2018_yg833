Jan5,2019
# Homework 6

This was week 6 of the course. There were 2 assignments for the evening session. There were 4 assignments. 

# Assignment 1: Review Classmate Citibike Project Proposal
For this assignment, I reviewed sl4729's Assignment2 from HW4 where my colleague proposed a study using the Dec 2015 Citibikes data set. SL4729's ipynb is included in this repo named "Assignment2_sl4729.ipynb" Below I included my review fo SL4729's work:


### Idea:
The average trip duration of female is lower than that of male.

### Null Hypothesis:
The average trip duration of female is large or equal to that of female. Mean of Duration_female - Mean of Duration_male >= 0

### Alternatice Hypothesis:
The average trip duration of female is lower than that of male. Mean of Duration_female - Mean of Duration_male < 0
I will use a significance level $\alpha=0.05$,which means I want the probability of getting a result at least as significant as mine to be less then 5%


### Null Hypothesis Formulation:

* Seems like there maybe a typo in my colleague's NULL HYPOTHESIS. My colleague wrote: "The average trip duration of female is large or equal to that of female. Mean of Duration_female - Mean of Duration_male >= 0" 

* I think my colleague meant to write "The average trip duration of female is large or equal to that of _male_. Mean of Duration_female - Mean of Duration_male >= 0"

* For the formula at the end, I think my colleague should have written something like the following:

** $H_0: P_0 - P_1 \geq$    0 **
    
** $H_a: P_0 - P_1 $< 0    **
    
    
** $\alpha$ = 0.05    **

** this is a TEST OF PROPORTIONS. we use the Binomial distribution since it is a yes/no (bernulli) test for each subject: the former inmate was or was not ever employed in a CEO transitional job (second row in the table above): **

** $P_0=0.035, P_1=0.701$**

### Data:

* The data has the appropriate features to answer the question.

* Preprocessed data shows the whether the day of the ride was a weekend or a weekday, along with the day of the week.

* Ridership was normalised across weekdays and weekends for comparision on an equalised scale.

### Testing The Hypothesis:

#### Ho: The proportion of people that bike during the weekends is more or the same to the proportion of people that bike on weekdays

#### Data: Citibike data preprocessed to generate samples by weekdays and weekends.

* Since we are comparing two samples from the same population which is the citibike dataset, the two-proportion z-test could be used to test the hypothesis. 

* We can then assess whether there is any statistical difference between the two samples.


### Suggestion(s):

* It would be interesting to see whether the trend holds true across the various boroughs of New York. 

* By capturing the riding habits, citibike can make provision for the bikes according to where the bulk of the riders based on the   day of the week and place.

# Assignment 2

Ross - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057107

# Assignment 3
For this assignment, I worked closely with S. Falk (sjf374) and R. MacWhinney (ram844). We read the directions together and went over each step over google hangout. The hardest part was creating the function for evalChisq and the credit for it goes to sjf374 for testing out the various numpy functions with calculating the sums / products on diagonals in an array.

# Assignment 4
