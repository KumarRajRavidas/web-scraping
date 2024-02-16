import warnings
import pandas as pd
import os
import requests


# Suppress the PyArrow warning
warnings.filterwarnings("ignore")


def download_pdf(row, dest_folder):
    pdf_url = row['pdf_address']
    pdf_title = row["title"]
    pdf_pub_date = row['pub_date']
    pdf_folder = os.path.join(dest_folder, pdf_pub_date)
    os.makedirs(pdf_folder, exist_ok=True)

    try:
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            filename = f'{pdf_title}.pdf'
            with open(os.path.join(pdf_folder, filename), 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f'Successfully downloaded ✅ => {pdf_title}')
        else:
            print(f"Failed to download PDF from ❌: {pdf_url}")
    except Exception as e:
        print(f"An error occurred while processing {pdf_title}: {e}")


def main():
    csv_file = input("Enter the CSV file name (including extension)🔖: ")
    output_dir = csv_file.split('.')[0]
    print("PDF Download initiated 📕...")
    os.makedirs(output_dir, exist_ok=True)

    try:
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            download_pdf(row, output_dir)
    except FileNotFoundError:
        print(f"File {csv_file} not found")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

    print("Download completed successfully 👏")


if __name__ == "__main__":
    main()
