from data.dictionary import data, count
from avg_alcohol_usage import average_frequency_score

#inside the main class lets only havbe the fucntions that were going to use for analysis
#i have the functions ive made so far for data reorganization insdie the dictionary.py

#for out analusis, i think we could do

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