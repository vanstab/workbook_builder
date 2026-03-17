# Workbook Generator

Create PDF workbooks for your kids in a friendly UI. You can print or open them up in a note app for your kids to practice tracing on over and over again.

---

## 🚀 Quick Start (For Complete Beginners)

**Want to get started in 3 steps?**

1. **Install Python** from [python.org/downloads](https://www.python.org/downloads/) (if not already installed)
2. **Install packages:** Open terminal in this folder and run:
   ```bash
   # Optional but recommended: Create virtual environment first
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate   # Windows

   # Install dependencies
   pip3 install -r requirements.txt
   ```
3. **Double-click** `start_ui.sh` (Mac/Linux) or `start_ui.bat` (Windows) - Done! 🎉

Your browser will open with a simple interface where you can:
- ✅ Check boxes for activities
- ✅ Choose themes and colors
- ✅ Add numbers and letters
- ✅ Click "Generate" and download your PDF!

---

## What Does This Do?

This tool creates PDF worksheets with fun activities to help kids practice:
- **Tracing lines** (straight, wavy, zigzag, waves, loops, etc.)
- **Drawing shapes** (circles, squares, triangles, spirals)
- **Writing numbers** (0-9)
- **Writing letters** (A-Z uppercase and a-z lowercase)
- **And more**

Each worksheet includes:
- Colorful themes
- Encouraging messages
- Dashed lines that are easy for little hands to trace
### Example page
<img width="945" height="1051" alt="Screenshot 2026-03-16 222413" src="https://github.com/user-attachments/assets/f7ca4bb4-c796-4e86-94b9-0debc52f8ef4" />

### The UI
<img width="1128" height="1240" alt="Screenshot 2026-03-16 222233" src="https://github.com/user-attachments/assets/05e17eed-fd94-4d9f-a7f7-c232fa0a5930" />

 <img width="790" height="952" alt="Screenshot 2026-03-16 222356" src="https://github.com/user-attachments/assets/bfb70968-5773-4618-bd2d-f490951488c1" />


---

## Getting Started

### Step 1: Install Python

If you don't have Python installed:
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.10 or newer
3. Run the installer (make sure to check "Add Python to PATH")

### Step 2: (Optional but Recommended) Set Up Virtual Environment

Using a virtual environment keeps your project dependencies isolated and clean:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You'll see `(venv)` in your terminal prompt when it's active. To deactivate later, just type `deactivate`.

### Step 3: Install Required Packages

**Option 1: Quick install (recommended):**
```bash
pip3 install -r requirements.txt
```

**Option 2: Manual install:**
```bash
pip3 install reportlab Hershey-Fonts streamlit
```

**Note:** If you're using a virtual environment, you can use `pip` instead of `pip3`:
```bash
pip install -r requirements.txt
```

### Step 4: You're Ready!

Navigate to this folder in your terminal and start creating worksheets!

---

## 🎨 Easy Way: Use the Web Interface (Recommended for Non-Technical Users)

The **easiest way** to create worksheets is using our simple web interface - no command line knowledge needed!

### Launch the Web UI

**Super Easy Method (Double-Click):**
- **Mac/Linux:** Double-click `start_ui.sh`
- **Windows:** Double-click `start_ui.bat`

**Or use the terminal:**
1. Open your terminal in this folder
2. Type this command:

```bash
streamlit run app.py
```

3. Your web browser will automatically open with the worksheet generator!

### Network Access

The app is configured to be accessible from other devices on your network by default:
- **This computer:** http://localhost:8501
- **Other devices:** http://YOUR_IP_ADDRESS:8501

To change network settings or make it local-only, see [NETWORK_CONFIG.md](NETWORK_CONFIG.md).

---

## Troubleshooting

### "command not found: python3"

Try using `python` instead:
```bash
python -m workbook_builder --activities straight
```

### "No module named 'reportlab'"

Install the required packages using the requirements file:
```bash
pip3 install -r requirements.txt
```

Or install manually:
```bash
pip3 install reportlab Hershey-Fonts streamlit
```

Or try without the "3":
```bash
pip install -r requirements.txt
```

### "Permission denied"

You might need to add `sudo` on Mac/Linux:
```bash
sudo pip3 install reportlab Hershey-Fonts
```

### Numbers or letters look wrong

Make sure you installed the Hershey-Fonts package:
```bash
pip3 install Hershey-Fonts
```

### Want to see all options?

Run the help command:
```bash
python3 -m workbook_builder --help
```

### Using Virtual Environment

If you set up a virtual environment (recommended), remember to activate it each time you want to use the tool:

```bash
# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You'll see `(venv)` in your terminal prompt when active. Then run your commands as normal.

**To deactivate when done:**
```bash
deactivate
```

**Forgot if venv is active?** Look for `(venv)` at the start of your terminal prompt.

---

## Need Help?

If you encounter any issues or have questions, please check:
1. Make sure Python 3.10+ is installed
2. Make sure reportlab and Hershey-Fonts are installed
3. Run `python3 -m workbook_builder --help` to see all options

---

## Have Fun!

I wanted to make a free and easy way to make workbooks for kids. Was motivated because mine loves them so much!

If you have suggestions feel free to add an issue.


Happy tracing! ✏️

PS: AI was used to make this project, I was curious to see how it would do and wasn't disappointed by the results.
