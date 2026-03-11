# datacleaner.py
# Cleans the raw master_data.csv file and creates master_data_cleaned.csv
#made with chatgpt bc outside of project scope

import pandas as pd


def clean_full_dataset(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    # Rename columns by position (in case headers are messy)
    df = df.rename(columns={
        df.columns[0]: "Section",
        df.columns[1]: "QuestionID",
        df.columns[2]: "QuestionText",
        df.columns[3]: "ResponseID",
        df.columns[4]: "Response",
        df.columns[5]: "Group",
        df.columns[6]: "Count"
    })

    # Convert Count to numeric safely
    df["Count"] = pd.to_numeric(df["Count"], errors="coerce")

    # Remove rows with no valid count
    df = df.dropna(subset=["Count"])

    # Remove junk responses
    df = df[~df["Response"].isin(["Selected", "Not Selected"])]

    # Remove empty responses
    df = df[df["Response"].notna()]

    # Clean weird response formatting
    # Keeps only first part before numbers
    df["Response"] = df["Response"].astype(str).str.split().str[0:4].str.join(" ")

    # Reset index
    df = df.reset_index(drop=True)

    # Save cleaned file
    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")

    return df


# Only runs if you manually execute this file
if __name__ == "__main__":
    clean_full_dataset("master_data.csv", "master_data_cleaned.csv")