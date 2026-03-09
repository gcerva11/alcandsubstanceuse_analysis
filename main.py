from dataset.scripts.usage_stats import avg_alcohol_usage
from dataset.scripts.usage_stats import avg_substance_usage
#from dataset.scripts.demographic_stats import ___
import dataset.scripts.usage_stats
from classdefinitions import UsageRecord

#inside the main class lets only havbe the fucntions that were going to use for analysis
#i have the functions ive made so far for dataset reorganization insdie the dictionary.py

#for out analysis, i think we could do

#upper vs underclassmen percentage of use frequency, and what are their implications

#upper vs under high_risk frequency

#usage diferences of different substances

#idk what else

#and then question 22L1-12 is like about consequences, we could analys a litle bit og that
#it wuld be a but dufferbet tho bc its not explicitly saying if they are upper or underclassmen

#average alcohol

def main():
    qid = "22B12"   # replace with your alcohol frequency question id

    groups = ["Cis Men", "Cis Women", "TGNC", "Total"]

    print("\nAverage Alcohol Frequency Score")
    print("--------------------------------")

    for g in groups:
        avg = average_frequency_score(qid, g)
        print(f"{g}: {avg:.2f}")

if __name__ == "__main__":
    main()

#Output text code

def analysis_exec() -> None:
    with open("output.txt", "w") as file:
        file.write("Thank you for running our program! This analysis was made using the Undergraduate Student Reference Group Data Report from "
                "Fall 2025 by the American College Health Association (ACHA) for the CSC 101-21 Final Project in Winter 2026 by Angel Sanchez and "
                "Guadalupe Cervantes.\n\nEverything within this document is made using dataset sourced from the Report and processed using Python. "
                "There may be errors or oversights in any connections made due to the limited time and scope involved in development.\n\n\n"
                   "STUDENT DEMOGRAPHICS\n"
                   ""
                   "ALCOHOL/SUBSTANCE USAGE \n"
                   "The average amount of alcohol usage overall is "f"{avg_alcohol_usage()}"" throughout the survey.\n" #insert into blank
                   ""
                   "The average amount of substance usage overall is "f"{avg_substance_usage()}"" throughout the survey.\n"
                   ""
                   "The difference between average alcohol usage and average substance usage is "f"{}"" between ___\n\n" #if we want to compare them
                   "ACADEMIC STATS"
                   ""
                   "\n\n"
                   "MENTAL HEALTH STATS")
analysis_exec()