from dataset.dictionary import data, build_dataset_from_data
from dataset.scripts.academic_stats import average_gpa
from dataset.scripts.demographic_stats import upper_under_percentages
from dataset.scripts.usage_stats import average_frequency_score
from dataset.scripts.wellbeing_stats import avg_sleep_hours
from dataset.scripts.social_impact_stats import (
    community_harm_percent,
    academic_impact_ratio,
    disparity_index
)

#Output txt code
GROUPS = ["Cis Men", "Cis Women", "TGNC", "Total"]

def print_block(title: str):
    print("\n" + "=" * 5, title, "=" * 5)

def analysis_exec() -> None:
    dataset = build_dataset_from_data(data)

    with open("output.txt", "w") as file:

        file.write(
            "Thank you for running our program! This analysis was made using the Undergraduate "
            "Student Reference Group Data Report from Fall 2025 by the American College "
            "Health Association (ACHA) for the CSC 101-21 Final Project in Winter 2026 "
            "by Angel Sanchez and Guadalupe Cervantes.\n\n"
            "Everything within this document is made using dataset sourced from the Report "
            "and processed using Python. There may be errors or oversights in any "
            "connections made due to the limited time and scope involved in development.\n\n"
        )

        file.write("ALCOHOL USAGE (22B12)\n")

        for g in GROUPS:
            file.write(f"{g}: {average_frequency_score(dataset, '22B12', g):.2f}\n")

        file.write("\nYEAR IN SCHOOL (72)\n")

        for g in GROUPS:
            p = upper_under_percentages(dataset, "72", g)
            file.write(
                f"{g}: Underclass {p['Underclassmen']:.2f}% | "
                f"Upperclass {p['Upperclassmen']:.2f}%\n"
            )

        file.write("\nGPA (80)\n")

        for g in GROUPS:
            file.write(f"{g}: {average_gpa(dataset, '80', g):.2f}\n")

        file.write("\nCOMMUNITY HARM (22L1)\n")

        harm_values = {}
        for g in GROUPS:
            harm = community_harm_percent(dataset, "22L1", g)
            harm_values[g] = harm
            file.write(f"{g}: {harm:.2f}% reported harm\n")

        file.write(
            f"\nGender Disparity (Harm): "
            f"{disparity_index(harm_values):.2f}% difference\n"
        )

        file.write("\nACADEMIC IMPACT RATIO\n")

        ratio_values = {}
        for g in GROUPS:
            ratio = academic_impact_ratio(dataset, "22B12", "30B", g)
            ratio_values[g] = ratio
            file.write(f"{g}: {ratio:.2f} harm-to-risk ratio\n")

        file.write(
            f"\nGender Disparity (Impact Ratio): "
            f"{disparity_index(ratio_values):.2f}\n"
        )

        file.write("\nSLEEP HOURS\n")
        file.write(
            f"Average Sleep on Weekdays (Total): "
            f"{round(avg_sleep_hours(dataset, 'Q14', 'Total'), 2)}\n"
        )
        file.write(
            f"Average Sleep on Weekends: "
            f"{round(avg_sleep_hours(dataset, 'Q15', 'Total'), 2)}\n"
        )
    print("\nAnalysis Completed!\n")

analysis_exec()