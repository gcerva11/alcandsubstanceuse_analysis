# datacleaner.py
# Cleans the raw master_data.csv file and creates master_data_cleaned.csv
# Made with chatgpt as this was out of the scope of the project
# Now supports both 7-column rows and 6-column (sleep) rows.

import csv
import pandas as pd


def clean_full_dataset(input_path: str, output_path: str) -> pd.DataFrame:
    # 1) Normalize mixed-format rows into a consistent 7-column CSV in-memory
    normalized_rows = []
    header = ["Section", "QuestionID", "QuestionText", "ResponseID", "Response", "Group", "Count"]

    with open(input_path, newline="", encoding="utf-8") as fin:
        reader = csv.reader(fin)

        for row in reader:
            if not row:
                continue

            # Skip header if present
            if row[0].strip().lower() == "section":
                continue

            # --- Handle formats ---
            if len(row) == 7:
                section, qid, qtext, rid, resp, group, count = [x.strip() for x in row]
            elif len(row) == 6:
                # Sleep-style rows: missing ResponseID
                section, qid, qtext, resp, group, count = [x.strip() for x in row]
                rid = "-1"  # placeholder ResponseID
            else:
                # Unknown row shape; skip
                continue

            # Must have count + response + group + question text
            if count == "" or resp == "" or group == "" or qtext == "":
                continue

            # Remove junk responses
            if resp in ("Selected", "Not Selected"):
                continue

            normalized_rows.append([section, qid, qtext, rid, resp, group, count])

    # 2) Load normalized rows into pandas
    df = pd.DataFrame(normalized_rows, columns=header)

    # Convert Count safely
    df["Count"] = pd.to_numeric(df["Count"], errors="coerce")
    df = df.dropna(subset=["Count"])

    # Reset index
    df = df.reset_index(drop=True)

    # Save cleaned file
    df.to_csv(output_path, index=False)

    print(f"\nCleaned dataset saved to: {output_path}! :)\n")
    return df


if __name__ == "__main__":
    clean_full_dataset("master_data.csv", "master_data_cleaned.csv")