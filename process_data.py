import pandas as pd
from pathlib import Path

source_directory = Path("data")

csv_list = sorted(source_directory.glob("*.csv"))

processed_data = []

for csv_path in csv_list:
    table = pd.read_csv(csv_path)

    pink_records = table[
        table["product"].str.lower() == "pink morsel"
    ].copy()

    pink_records["price"] = (
        pink_records["price"]
        .str.replace("$", "", regex=False)
        .astype(float)
    )

    pink_records["sales"] = (
        pink_records["quantity"] * pink_records["price"]
    )

    cleaned_table = pink_records.loc[:, ["sales", "date", "region"]]

    processed_data.append(cleaned_table)

final_output = pd.concat(processed_data, ignore_index=True)

output_path = source_directory / "formatted_output.csv"

final_output.to_csv(output_path, index=False)

print("Processing Complete!")