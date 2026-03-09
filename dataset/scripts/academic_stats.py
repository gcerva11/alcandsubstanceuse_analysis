from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
dataframe = pd.read_csv(BASE_DIR / "master_data_cleaned.csv")

#If we have time I think we should do something with grades like you mentioned
#data set includes letter grades, so we have to convert it into 4.0 gpa system
#to convert it
#we first should convert these letter grades into gpa grades and then use that to find the average

GRADE_POINTS = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0,
}

def avg_gpa(dataframe: pd.DataFrame,question_text: str,group: str | None = "Total",) -> float | None:
    #dataframe is reading our cleaned dataset
    #group can be "Total", "Cis Men", "Cis Women", "TGNC", or None for all groups combined

    sub = dataframe[dataframe["QuestionText"] == question_text].copy()

    if group is not None:
        sub = sub[sub["Group"] == group]

    sub["Points"] = sub["Response"].map(GRADE_POINTS)
    sub = sub.dropna(subset=["Points"])

    total_count = sub["Count"].sum()
    if total_count == 0:
        return None

    gpa = (sub["Points"] * sub["Count"]).sum() / total_count
    return round(float(gpa), 3)