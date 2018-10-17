# Homework 6

This was week 6 of the course. There were 4 assignments for the evening session.

# Assignment 1: Review Classmate Citibike Project Proposal
(individual) For this assignment, I reviewed sl4729's Assignment2 from HW4 where my colleague proposed a study using the Dec 2015 Citibikes data set. SL4729's ipynb is included in this repo named "Assignment2_sl4729.ipynb". The assignment was pulled from https://github.com/sl4729/PUI2018_sl4729/tree/master/HW4_sl4729

Below I included my review of SL4729's work:

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

 H_0: P_f - P_m => 0 
    
 H_a: P_f - P_m < 0    
    
 alpha = 0.05  
 
### Data:

* Looking at the rendered notebook from my colleague, in general it appears that the appropriate features are present to answer the question.

* The trimmed down data set shows tripduration, gender, and date. So perhaps the date timestamp column is not actually needed for this analysis considering the idea only is about average trip duration for female vs male. There isn't a date or time of week element.

### Testing The Hypothesis:

Ho: The average trip duration of _female_ is large or equal to that of _male_

Data: Citibike data preprocessed for Dec 2015 with only the tripduration and gender variable.

* As both genders were sampled from the same population (dec 2015 citibikes), the two-proportion _z_ test could be used. 

* Additionally, we can also understand male and females are different populations, then use the 2 groups unpaired _t_ test.

### Additional Thoughts:

* Perhaps, there could be a revisit of the idea and H0 to accommodate for a day of week element. Something along the lines of are female riders during each day of the week slower that male riders. This may add an additional flavor to the analysis where weekdays could look different than weekends.

* For the tripduration variable, I think my colleague should use units. Looking at the rendered data, it looks like the unit maybe seconds.


# Assignment 2

##ANOVA:
The paper  "[How accurate are runners’ prospective predictions of their race times?](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0200744) " aimed to better understand prospective evaluations --being able to make an accurate prospective assessment of how one will perform on the annual half marathon race. The study looked at a variety of categorical variables such as demographics, gender, and prediction whilst controlling for experience levels via a categorical variable of running club membership. 

| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:-------------------------:|:------------|:----------------|:------------|:-----------------|:-----------------|:--------------------- |:----------------------------|:--------:|:---------:|:-----------------|
|ANOVA	| 3, running club membership, gender, age | categorical | 1, interaction with prediction times| categorical | 1, experience measured via running club membership | categorical | How accurate are runner's prospective predictions of their finish running times?| Inexperienced runners predict as accurately as experienced runners. | 0.05 | [How accurate are runners’ prospective predictions of their race times?](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0200744) |

![ANOVA](../HW6_yg833/HW6_pics/assignment2_anova_pic.PNG)

##
| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:-------------------------:|:------------|:----------------|:------------|:-----------------|:-----------------|:--------------------- |:----------------------------|:--------:|:---------:|:-----------------|
|Multiple Regression|2+|continuous|||||[The Relationship between National-Level Carbon Dioxide Emissions and Population Size: An Assessment of Regional and Temporal Variation, 1960–2005](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057107)|


##
| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:-------------------------:|:------------|:----------------|:------------|:-----------------|:-----------------|:--------------------- |:----------------------------|:--------:|:---------:|:-----------------|
|||||||||

# Assignment 3
For this assignment, I worked closely with S. Falk (sjf374) and R. MacWhinney (ram844). We read the directions together and went over each step over google hangout. The hardest part was creating the function for evalChisq and the credit for it goes to sjf374 for testing out the various numpy functions with calculating the sums / products on diagonals in an array.

# Assignment 4
