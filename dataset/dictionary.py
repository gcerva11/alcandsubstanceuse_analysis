import csv
import os
import dataset.scripts.demographic_stats
import dataset.scripts.academic_stats
import dataset.scripts.usage_stats
import dataset.scripts.wellbeing_stats

data = {}

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row if your CSV has one
    next(reader, None)

    for row in reader:
        # Skip incomplete rows
        if len(row) < 7 or row[3].strip() == "" or row[6].strip() == "":
            continue

        section = row[0]
        qid = row[1].strip()
        question_text = row[2].strip()
        response_code = int(row[3])
        response = row[4].strip()
        group = row[5].strip()
        count = int(row[6])

        # Create question level
        if qid not in data:
            data[qid] = {
                "section": section,
                "question_text": question_text,
                "responses": {}
            }

        # Create response level
        if response_code not in data[qid]["responses"]:
            data[qid]["responses"][response_code] = {
                "response": response,
                "counts": {}
            }

        # Store count by group
        data[qid]["responses"][response_code]["counts"][group] = count


#*************
# Helper Functions
#*************

#this function makes sure we can get the diction without the program crashing
def question(qid:str)-> str:
    return data.get(str(qid), {})

#this one is going to loop the response in order to get the information for specifc questions
def responces_loop(qid:str)-> str:
    question = question(qid)
    responces = question.get("responces", {})
    return responces.items() #should return like (responce #, informaton)

#this one is going to get a count
def getcount(qid, response_code, group="total")
