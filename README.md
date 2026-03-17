# Workbook Generator

Create beautiful, customizable tracing worksheets for young children (ages 2-5) with just one command!

---

## 🚀 Quick Start (For Complete Beginners)

**Want to get started in 3 steps?**

1. **Install Python** from [python.org/downloads](https://www.python.org/downloads/) (if not already installed)
2. **Install packages:** Open terminal in this folder and run:
   ```bash
   # Optional but recommended: Create virtual environment first
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # venv\Scripts\activate   # Windows

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

Each worksheet includes:
- Colorful themed decorations (animals, ocean, space, garden, or food)
- Encouraging messages
- Guide lines to help with proper letter formation
- Dashed lines that are easy for little hands to trace

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

### Using the Web Interface

The interface has three main sections:

**Left Side - Activities:**
- Check boxes for activities you want (straight lines, circles, etc.)
- Click "Select All Activities" for a complete workbook

**Right Side - Numbers & Letters:**
- Check "Include numbers" to add number tracing (0-9)
- Check "Include letters" to add letter tracing (A-Z)
- Choose "All" or select specific ones

**Sidebar - Settings:**
- **Theme:** Choose decorations (animals, ocean, space, garden, food)
- **Rows per page:** 3-6 (more = more practice)
- **Line thickness:** 2.0-5.0 (thicker = easier to see)
- **Guide style:** Dashed, dotted, or solid lines
- **Filename:** Name your PDF

**Generate:**
- Click the big "Generate Worksheet" button
- Download your PDF when it's ready!

### Tips for the Web UI:
- Start simple: Try straight + wavy lines with animals theme
- For younger kids: Use 3-4 rows and thicker lines (4.0+)
- For older kids: Use 5-6 rows with all activities
- The interface saves you from typing commands!

---

## 💻 Advanced Way: Use the Command Line

For users comfortable with the terminal, you can also create worksheets using commands directly.

### Basic Command Line Usage

Open your terminal in this folder and type:

```bash
python3 -m workbook_builder
```

This creates a worksheet with **all activities** using the **animals theme**.

---

## Customization Options

### Choose Activities

Pick which activities you want on your worksheet:

```bash
python3 -m workbook_builder --activities straight wavy circles
```

**Available activities:**
- `straight` - Horizontal straight lines
- `wavy` - Wavy lines
- `zigzag` - Zigzag lines
- `diagonals` - Diagonal lines
- `waves` - Wave patterns (sine waves)
- `loops` - Loop patterns (great for cursive writing practice)
- `circles` - Circle shapes
- `squares` - Square shapes
- `triangles` - Triangle shapes
- `spirals` - Spiral patterns
- `addition` - Addition math problems
- `subtraction` - Subtraction math problems
- `numbers` - Number tracing (combine with `--numbers`)
- `letters` - Letter tracing (combine with `--letters`)
- `all` - Everything! (all line/shape activities)

### Choose a Theme

Make it fun with themed decorations:

```bash
python3 -m workbook_builder --theme ocean
```

**Available themes:**
- `animals` - Bees, fish, butterflies, caterpillars
- `ocean` - Whales, turtles, starfish, shells
- `space` - Rockets, aliens, UFOs, planets
- `garden` - Ladybugs, snails, mushrooms, leaves
- `food` - Apples, cupcakes, ice cream, cookies

### Add Numbers

Create number tracing pages:

```bash
# Trace specific numbers
python3 -m workbook_builder --numbers 1 2 3

# Trace all numbers (0-9)
python3 -m workbook_builder --numbers all

# Mix with other activities
python3 -m workbook_builder --activities straight wavy numbers --numbers 0 1 2
```

### Add Letters

Create letter tracing pages (uppercase, lowercase, or both):

```bash
# Trace specific uppercase letters
python3 -m workbook_builder --letters A B C

# Trace specific lowercase letters
python3 -m workbook_builder --letters a b c

# Trace all uppercase letters (A-Z)
python3 -m workbook_builder --letters all

# Trace all lowercase letters (a-z)
python3 -m workbook_builder --letters all-lower

# Trace both uppercase AND lowercase (A-Z + a-z)
python3 -m workbook_builder --letters all-both

# Mix uppercase and lowercase
python3 -m workbook_builder --letters A a B b C c

# Mix with other activities
python3 -m workbook_builder --activities circles numbers letters --numbers 5 --letters A B a b
```

### Adjust Difficulty

**Change the number of rows** (more rows = more practice):

```bash
python3 -m workbook_builder --rows 3    # Easier (fewer rows)
python3 -m workbook_builder --rows 6    # Harder (more rows)
```

**Change line thickness** (thicker = easier to see):

```bash
python3 -m workbook_builder --line-thickness 2.0    # Thinner
python3 -m workbook_builder --line-thickness 5.0    # Thicker
```

**Change guide line style:**

```bash
python3 -m workbook_builder --guide-style dashed    # Dashed lines (default)
python3 -m workbook_builder --guide-style dotted    # Dotted lines
python3 -m workbook_builder --guide-style solid     # Solid lines
```

### Save with a Custom Name

```bash
python3 -m workbook_builder --output my_worksheet.pdf
```

---

## Quick Examples

### Example 1: Simple Line Practice

Create a worksheet with just straight and wavy lines:

```bash
python3 -m workbook_builder --activities straight wavy --theme animals -o lines_practice.pdf
```

### Example 2: Numbers 1-5 for Beginners

```bash
python3 -m workbook_builder --numbers 1 2 3 4 5 --theme space --rows 3 -o numbers_easy.pdf
```

### Example 3: Alphabet Practice

```bash
python3 -m workbook_builder --letters all --theme garden --rows 4 -o alphabet.pdf
```

### Example 4: Mixed Practice

Combine lines, shapes, numbers, and letters:

```bash
python3 -m workbook_builder --activities straight circles numbers letters --numbers 0 1 2 --letters A B C --theme ocean -o mixed_practice.pdf
```

### Example 5: Everything!

Create a complete workbook with all activities:

```bash
python3 -m workbook_builder --activities all --theme food --rows 5 -o complete_workbook.pdf
```

---

## Understanding the Options

| Option | What It Does | Default |
|--------|-------------|---------|
| `--activities` | Which activities to include | `all` |
| `--theme` | Decoration theme | `animals` |
| `--numbers` | Which numbers to trace (0-9) | None |
| `--letters` | Which letters to trace (A-Z) | None |
| `--rows` | How many rows per page (3-6) | `5` |
| `--line-thickness` | How thick the guide lines are (2.0-5.0) | `3.0` |
| `--guide-style` | Line style (dashed/dotted/solid) | `dashed` |
| `--output` or `-o` | PDF filename | `worksheet_<theme>.pdf` |

---

## Tips for Best Results

### For Younger Kids (Ages 2-3)
```bash
python3 -m workbook_builder --activities straight wavy circles --rows 3 --line-thickness 4.0 --theme animals
```
- Fewer rows (3)
- Thicker lines (4.0)
- Simple activities (straight, wavy, circles)

### For Older Kids (Ages 4-5)
```bash
python3 -m workbook_builder --activities all --numbers all --letters all --rows 6 --theme space
```
- More rows (6)
- Include numbers and letters
- All activities for variety

### For Number Practice Only
```bash
python3 -m workbook_builder --numbers all --theme ocean --rows 4
```

### For Letter Practice Only
```bash
python3 -m workbook_builder --letters all --theme garden --rows 4
```

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

## What's On Each Page?

Each worksheet page includes:
- **Colorful banner** at the top with the activity title
- **Instructions** telling kids what to do
- **Themed decorations** in the corners and bottom
- **Main activity area** with guide lines or shapes to trace
- **Encouraging message** at the bottom ("Great job!", "Keep going!", etc.)
- **Page numbers** to keep track

For numbers and letters:
- **Example character** in a box (top-left corner)
- **Grid of traceable characters** with dashed single-line strokes
- **Guide lines** (baseline and midline) to help with proper formation
- **Colorful variety** - each character uses different colors

---

## Examples of What You Can Create

**Animals Theme + Shapes:**
```bash
python3 -m workbook_builder --activities circles squares triangles --theme animals -o shapes.pdf
```

**Ocean Theme + All Numbers:**
```bash
python3 -m workbook_builder --numbers all --theme ocean -o ocean_numbers.pdf
```

**Space Theme + Vowels:**
```bash
python3 -m workbook_builder --letters A E I O U --theme space -o vowels.pdf
```

**Garden Theme + Everything:**
```bash
python3 -m workbook_builder --activities all --numbers all --letters all --theme garden -o mega_workbook.pdf
```

---

## Need Help?

If you encounter any issues or have questions, please check:
1. Make sure Python 3.10+ is installed
2. Make sure reportlab and Hershey-Fonts are installed
3. Run `python3 -m workbook_builder --help` to see all options

---

## Have Fun!

These worksheets are designed to make learning fun! Mix and match themes, activities, and options to create the perfect practice sheets for your child.

Happy tracing! ✏️
