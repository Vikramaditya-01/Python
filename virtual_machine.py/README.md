```markdown
# Virtual Environment Setup in Python (Windows)

## 1. Create a Virtual Environment

```bash
python -m venv virtual_machine_name
```
> Create a virtual environment with the name **"virtual_machine_name"**

```bash
python -m venv .venv
```
> Create a virtual environment in the current directory with the name **".venv"**

---

## 2. Activate the Virtual Environment

### 2.1 Bypass the Execution Policy in PowerShell (Temporarily)

```powershell
Set-ExecutionPolicy Bypass -Scope Process
```
> Allow script execution in the current PowerShell session by bypassing the execution policy for the current process.

### 2.2 Activate the Virtual Environment

```powershell
.\Virtual_Machine_name\Scripts\Activate.ps1
```
> Activate the virtual environment in PowerShell.

---

## 3. Installing Packages in the Virtual Environment

```bash
pip install package_name
```
> Install a package in the virtual environment.

---

## 4. Installing Multiple Packages in the Virtual Environment

```bash
pip install -r requirements.txt
```
> Install all packages listed in the `requirements.txt` file in the virtual environment.

---

## 5. List All Installed Packages in the Virtual Environment

```bash
pip list
```
> List all installed packages in the virtual environment.

---

## 6. Save Installed Packages to Requirements File

```bash
pip list > requirements.txt
```
> Save the list of installed packages in the `requirements.txt` file. After adding more packages to the virtual environment, run this command again to update the file.

---

## 7. Uninstalling Packages in the Virtual Environment

```bash
pip uninstall package_name
```
> Uninstall a package from the virtual environment.

---

## 8. Deactivate the Virtual Environment

```bash
deactivate
```
> Deactivate the virtual environment and return to the global Python environment.

---
```
