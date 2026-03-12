# alcandsubstanceuse_analysis
What does the program do?

Each file and what it does for out project:
dictionary.py
This file has the purpose of reading the master.data.cleaned.csv and created a global dictionary that we called 
"data", UsageRecord objects, as well as a dataset object that allows the methods to filter and compute properly.
The data gets stored by question id, response, and then group. This was necessary because our data was not formatted 
properly, as well as allows for a easy and
way to acess the data.

The UsageRecord class is necessary as it represents one of the rows of the dataset as an object with
section, question_id, question_text, response_code, response, group, count
This allows the program to use objects instead of using the raw CSV file.
is_year_in_school() checks if a record belongs to question 72 and
class_level() turns lavels into categories of underclassmen, upperclassnmen, and other (which would be like grad 
students)

The Dataset class stores a list of the UsageRcord objects that provide methods like
by_qid(qid) which filters records and by question id
by_qid_and_group(qid, group) which filters by the questions and groups
This is what allows us to compute the upper and underclass percentages, the high-risk percent, and consequence percentages. 

usage_stats.py
This file is used for behavior questions that have frequency-style responses (like alcohol use), where the answers 
are words instead of numbers.
It converts response labels into numeric scores so we can compute weighted averages:

Never = 0
Once or twice = 1
Monthly = 2
Weekly = 3
Daily or almost daily = 4

The main purpose is to calculate average usage frequency by group for a question id (like alcohol usage QID 22B12). 
It uses the Dataset filter functions to get only the relevant records, then does a weighted average using the counts.
This file is important because it turns survey responses into a number that’s easy to compare between groups.

demographic_stats.py
This file focuses on demographic breakdowns, especially Year in School (Question 72).
It groups year-in-school responses into categories:

Underclassmen (1st year, 2nd year)
Upperclassmen (3rd year, 4th year, 5th year or more)
Other (graduate students or anything outside those categories)

Its main job is to calculate the percentage of underclassmen vs upperclassmen for each group (Cis Men, 
Cis Women, TGNC, Total).
This file matters because it gives context about the sample population. For example, if most respondents 
are underclassmen, that can explain patterns in behavior and academic outcomes.

academic_stats.py
Because GPA responses are letter grades (A, A-, B+, etc.), the file uses a grade-point mapping like:

A/A+ = 4.0
A- = 3.7
B+ = 3.3
B = 3.0 
and so on.

The main function calculates a weighted GPA average for each group by:
filtering records for the GPA question id and group
converting each response label to grade points
doing a weighted average based on counts
This file matters because it turns GPA survey responses into an actual numeric GPA average that can be 
compared across groups.

social_impact_stats.py
This file is responsible for connecting our statistical results to broader social impact and responsibility 
themes. While the other files calculate averages and percentages, this file interprets those results in 
ways that highlight inequality, community harm, and academic consequences.
community_harm_percent(dataset, qid, group)

This function calculates the percentage of students in a given group who reported experiencing any harm 
related to substance use.

It filters records by question id and group using dataset.by_qid_and_group()
Counts the total responses
Counts all responses that are NOT “Never”
Returns the percentage of students who experienced harm
This function contributes to the project by turning raw survey data into a community-level harm indicator. 
Instead of just measuring usage, it measures consequences.

Social Responsibility Connection:
This connects directly to social responsibility because harm from substance use affects:
campus health resources
counseling services
academic performance
safety systems
A higher harm percentage suggests greater strain on shared institutional resources. Universities must allocate support 
systems responsibly and equitably.

academic_impact_ratio(dataset, usage_qid, academic_qid, group)
This function measures how much academic harm occurs relative to high-risk usage.

It calls dataset.high_risk_percent() to calculate high-risk behavior.
Calculates the percent of students reporting academic harm (responses containing “negatively” or “delayed”).
Divides academic harm percent by high-risk percent.
This creates a ratio showing how strongly risky behavior translates into academic consequences.
This function contributes to the project by connecting behavior (usage) to outcomes (academic impact).

Social Responsibility Connection:
This ratio reflects educational sustainability:
Academic delay affects graduation timelines.
Delays increase financial cost.
Increased cost affects institutional resource allocation.
Poor academic outcomes reduce long-term student success.
This links substance behavior to educational resource conservation and academic sustainability.

disparity_index(value_dict)
This function calculates inequality across groups.
It takes a dictionary of group → value
Finds the maximum and minimum values
Returns the difference between them
This function contributes by quantifying group inequality.

For example:
Gender Disparity (Harm)
Gender Disparity (Impact Ratio)
Social Responsibility Connection:
This highlights equity concerns.
If one group (ex: TGNC students) experiences significantly higher harm:

That indicates unequal vulnerability.
Universities have a responsibility to provide targeted support.
Equity-focused resource distribution becomes necessary.
This ties directly to fairness, inclusion, and responsible institutional policy.

This project highlights the social responsibility universities have in addressing substance use not just as an 
individual behavior, but as a community issue that affects academic sustainability, equity, and shared institutional 
resources. By analyzing usage patterns, academic impact, and harm percentages across different groups, we are able 
to see how risky behaviors translate into broader consequences such as delayed academic progress and unequal harm 
among gender groups. The disparity measurements, particularly for TGNC students, emphasize the importance of equitable
support systems and targeted prevention efforts. Institutions must responsibly allocate counseling services, health 
resources, and educational interventions in ways that reduce harm and promote long-term student success. Ultimately, 
this project demonstrates that data analysis can inform more ethical, equitable, and sustainable decision-making within
a university community.



