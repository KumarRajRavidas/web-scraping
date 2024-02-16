## Python Script for Scraping Articles from Nature.com

### Running the project locally

- Git clone the project below by running the command below

```bash
git clone git@github.com:seniorvw/mdpi-scraper.git
```

- `cd` into the root of the directory and run

```bash
pip3 install -r requirements.txt
```

- Running the above command will install all dependencies for the project
- Now within the project structure run

### Generatiing CSV

- Run the command below and enter prompts for generating content based off search

```zsh
  python3 script.py
```

### Downloading PDF files

- Run the below command in terminal

```zsh
python3 downloader.py
```

- You will be ask to provide the name of the csv file from which download will be initiated
  `e.g 1_education.csv`
