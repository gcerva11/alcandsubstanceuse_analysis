#Made with CHATGPT as cleaning the data was out of the scope of this project

import pandas as pd

def clean_full_dataset(input_path, output_path):
    df = pd.read_csv(input_path)

    # Rename columns based on position (since headers are messy)
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

    # Remove rows with no counts
    df = df.dropna(subset=["Count"])

    # Remove obvious junk responses
    df = df[~df["Response"].isin(["Selected", "Not Selected"])]

    # Remove empty responses
    df = df[df["Response"].notna()]

    # Reset index
    df = df.reset_index(drop=True)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")

    return df


# Run it
clean_full_dataset("master_data.csv", "master_data_cleaned.csv")