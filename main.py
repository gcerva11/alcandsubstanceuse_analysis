from dataset.dictionary import data, count
from avg_alcohol_usage import average_frequency_score
from avg_substance_usage import average_frequency_score
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




def test_output(f: float) -> float:
    return f + 2


#Output text code

def analysis_exec() -> None:
    with open("output.txt", "w") as file:
        file.write("Thank you for running our program! This analysis was made using the Undergraduate Student Reference Group Data Report from "
                "Fall 2025 by the American College Health Association (ACHA) for the CSC 101-21 Final Project in Winter 2026 by Angel Sanchez and "
                "Guadalupe Cervantes.\n\nEverything within this document is made using dataset sourced from the Report and processed using Python. "
                "There may be errors or oversights in any connections made due to the limited time and scope involved in development.\n\n\n"
                   ""
                   "there may be a "f"{test_output(3.0)}"" somewhere in this text file but it does not exist anywhere else in the project.")
analysis_exec()