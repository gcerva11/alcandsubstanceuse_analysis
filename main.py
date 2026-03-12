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

GROUPS = ["Cis Men", "Cis Women", "TGNC", "Total"]

def print_block(title: str):
    print("\n" + "=" * 5, title, "=" * 5)

def main():
    dataset = build_dataset_from_data(data)

    # Debug checks (VERY helpful)
    print("Total records:", len(dataset.records))
    print("GPA Total rows:", len(dataset.by_qid_and_group("80", "Total")))
    print("Alcohol Total rows:", len(dataset.by_qid_and_group("22B12", "Total")))

    # ----- Alcohol usage (example: 22B12) -----
    print("The response scores were averaged for each group, with the options being: \nNever	0, \nOnce or twice	1, \nMonthly	2, \nWeekly	3, \nDaily or almost daily 4, ")
    print_block("ALCOHOL USAGE (22B12)")
    for g in GROUPS:
        print(f"{g}: {average_frequency_score(dataset, '22B12', g):.2f}")

    # ----- Year in school (72) -----
    print_block("YEAR IN SCHOOL (72)")
    for g in GROUPS:
        p = upper_under_percentages(dataset, "72", g)
        print(f"{g}: Underclass {p['Underclassmen']:.2f}% | Upperclass {p['Upperclassmen']:.2f}%")

    # ----- GPA (80) -----
    print_block("GPA (80)")
    for g in GROUPS:
        print(f"{g}: {average_gpa(dataset, '80', g):.2f}")

    # ----- COMMUNITY HARM (example: 22L1) -----
    print_block("COMMUNITY HARM (22L1)")

    harm_values = {}

    for g in GROUPS:
        harm = community_harm_percent(dataset, "22L1", g)
        harm_values[g] = harm
        print(f"{g}: {harm:.2f}% reported harm")

    print("\nGender Disparity (Harm):",
          f"{disparity_index(harm_values):.2f}% difference")

    # ----- ACADEMIC IMPACT RATIO -----
    print_block("ACADEMIC IMPACT RATIO")

    ratio_values = {}

    for g in GROUPS:
        ratio = academic_impact_ratio(dataset, "22B12", "30B", g)
        ratio_values[g] = ratio
        print(f"{g}: {ratio:.2f} harm-to-risk ratio")

    print("\nGender Disparity (Impact Ratio):",
          f"{disparity_index(ratio_values):.2f}")

    # ----- SLEEP -----
    print_block ("SLEEP HOURS")

if __name__ == "__main__":
    main()