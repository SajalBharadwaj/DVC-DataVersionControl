# Prerequisites and Installation Guide

Before running this project, make sure that Python, pip, Git, and DVC are installed on your system.

## Step 1: Install Python

1. Download Python from the official website:

   https://www.python.org/downloads/

2. Run the installer.

3. During installation, make sure to enable:

   ```text
   ✔ Add Python to PATH
   ```

4. After installation, verify it:

   ```bash
   python --version
   ```

   Example output:

   ```bash
   Python 3.14.6
   ```

---

## Step 2: Verify pip Installation

Check whether pip is installed:

```bash
python -m pip --version
```

Example output:

```bash
pip 25.x from ...
```

If pip is not available, install it:

```bash
python -m ensurepip --upgrade
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

## Step 3: Install Required Libraries

Install Pandas:

```bash
python -m pip install pandas
```

Verify installation:

```bash
python -m pip show pandas
```

---

## Step 4: Install Git

Download Git from:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

Example:

```bash
git version 2.x.x
```

---

## Step 5: Install DVC

Install DVC using pip:

```bash
python -m pip install dvc
```

Verify DVC installation:

```bash
python -m dvc version
```

Example output:

```bash
DVC version: 3.x.x
```

If the `dvc` command is not recognized, use:

```bash
python -m dvc init
```

instead of:

```bash
dvc init
```

---

## Step 6: Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

Example:

```bash
git clone https://github.com/username/DVC-DataVersionControl.git
cd DVC-DataVersionControl
```

---

## Step 7: Run the Python Script

Execute the script:

```bash
python mycode.py
```

Expected output:

```bash
Dataset successfully saved at: data/sample_data.csv
```

---

## Step 8: Initialize DVC

Initialize DVC inside the project:

```bash
python -m dvc init
```

---

## Step 9: Configure Local DVC Remote Storage

Create a local directory to simulate remote storage:

```bash
mkdir S3
```

Add it as the default DVC remote:

```bash
python -m dvc remote add -d myremote S3
```

---

## Step 10: Track Dataset with DVC

```bash
python -m dvc add data/
```

If Git is already tracking the `data/` directory, remove it from Git tracking:

```bash
git rm -r --cached data
git commit -m "Stop tracking data with Git"
```

Track the dataset again:

```bash
python -m dvc add data/
```

Commit DVC metadata:

```bash
git add .gitignore data.dvc
git commit -m "Track dataset using DVC"
```

---

## Step 11: Push Data to DVC Remote

```bash
python -m dvc commit
python -m dvc push
```

---

## Step 12: Save Metadata to Git

```bash
git add .
git commit -m "Dataset Version 1"
git push
```

The project is now ready for dataset versioning using DVC.
