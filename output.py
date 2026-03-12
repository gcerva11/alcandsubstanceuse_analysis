



#Output text code

def analysis_exec() -> None:
    with open("output.txt", "w") as file:
        file.write("Thank you for running our program! This analysis was made using the Undergraduate Student Reference Group Data Report from "
                "Fall 2025 by the American College Health Association (ACHA) for the CSC 101-21 Final Project in Winter 2026 by Angel Sanchez and "
                "Guadalupe Cervantes.\n\nEverything within this document is made using dataset sourced from the Report and processed using Python. "
                "There may be errors or oversights in any connections made due to the limited time and scope involved in development.\n\n\n"
                   "STUDENT DEMOGRAPHICS\n"
                   ""
                   "ALCOHOL/SUBSTANCE USAGE\n"
                   "The average amount of alcohol usage overall is "f"{avg_alcohol_usage()}"" throughout the survey.\n" #insert into blank
                   ""
                   "The average amount of substance usage overall is "f"{avg_substance_usage()}"" throughout the survey.\n"
                   ""
                   "The difference between average alcohol usage and average substance usage is "f"{alc_substance_diff()}"" [units]\n\n" 
                   #if we want to compare them
                   "ACADEMIC STATS\n"
                   "Underclassmen (1st & 2nd Years) report having an average GPA of "f"{avg_und_class_gpa()}"" in the survey compared to "
                   "Upperclassmen" "(3rd & 4th years) reporting GPA averages of "f"{avg_up_class_gpa()}"""
                   ""
                   "\n\n"
                   "MENTAL HEALTH STATS\n"
                   "The average amount of sleep students have is around "f"{avg_sleep()}"""
                   ""
                   "")
analysis_exec()