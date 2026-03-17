# Coloring Images Folder Guide

## 📁 Available Folders

Your coloring images are organized into these folders:

| Folder | Purpose | Status |
|--------|---------|--------|
| **shapes/** | Basic geometric shapes | ✅ 12 shapes included |
| **animals/** | Animal outlines | 📂 Ready for your images |
| **objects/** | Common objects | 📂 Ready for your images |
| **nature/** | Flowers, trees, etc. | 📂 Ready for your images |
| **custom/** | Anything else! | 📂 Ready for your images |

## 🔄 How Images Are Selected

**Smart Rotation System:**
- Images are shown in a **deterministic order** (same images appear in same order every time)
- **No duplicates** until all images have been shown once
- After all images are shown, the cycle repeats with a slightly different order
- Perfect for generating multiple worksheets without repetition!

**Example with 12 shapes:**
- Pages 1-12: Each shape appears exactly once
- Pages 13-24: Each shape appears exactly once again (different order)
- Pages 25-36: Another cycle with variation

This means you can generate dozens of pages and each image gets equal representation!

## 🎨 How to Use Specific Folders

### In the Command Line:

```bash
# Use all folders (default)
python -m workbook_builder --activities colour --theme animals

# Use only shapes folder
python -m workbook_builder --activities colour --colour-folder shapes --theme ocean

# Use only animals folder
python -m workbook_builder --activities colour --colour-folder animals --theme garden

# Mix different folders in custom pages
python -m workbook_builder --pages colour:shapes colour:animals colour:nature --theme space
```

### In the Streamlit UI:

**Activity Selection Mode:**
1. Check "Coloring 🎨" checkbox
2. In the sidebar, choose from "Image folder" dropdown:
   - All folders (uses all images)
   - shapes
   - animals
   - objects
   - nature
   - custom

**Custom Page Order Mode:**
1. Click "🎨 Coloring" section
2. Select folder from dropdown
3. Click "➕ Add Coloring"
4. Each coloring page can use a different folder!

## 💡 Examples

### Example 1: Shapes-only Worksheet (No Repeats)
```bash
python -m workbook_builder --pages \
    colour:shapes colour:shapes colour:shapes colour:shapes colour:shapes \
    --theme animals -o shapes.pdf
```
**Result:** 5 different shapes, no duplicates

### Example 2: Full Cycle of All Shapes
```bash
python -m workbook_builder --pages \
    colour:shapes colour:shapes colour:shapes colour:shapes \
    colour:shapes colour:shapes colour:shapes colour:shapes \
    colour:shapes colour:shapes colour:shapes colour:shapes \
    --theme garden -o all_shapes.pdf
```
**Result:** All 12 shapes, each appearing exactly once

### Example 3: Mixed Activities with Shapes
```bash
python -m workbook_builder --pages \
    colour:shapes straight colour:shapes wavy \
    colour:shapes zigzag colour:shapes loops \
    --theme space -o mixed.pdf
```
**Result:** 4 different shapes interspersed with line activities

### Example 4: Progressive Difficulty
Add simple shapes first, then more complex animals:
```bash
python -m workbook_builder --pages \
    colour:shapes colour:shapes colour:shapes \
    colour:animals colour:animals \
    --theme animals -o progressive.pdf
```

## 📝 Tips

✓ **Start with shapes** - The included shapes are perfect for beginners
✓ **No duplicates** - Within each cycle, every image appears exactly once
✓ **Predictable order** - Same worksheet generates same images every time
✓ **Equal distribution** - All images get equal screen time
✓ **Mix and match** - Different pages can use different folders in the same worksheet!

## 🚀 Quick Start for Parents/Teachers

1. **Use shapes folder** (already has 12 images ready to go!)
   ```bash
   python -m workbook_builder --activities colour --colour-folder shapes -o my_worksheet.pdf
   ```

2. **Add your own images** to animals/, objects/, nature/, or custom/ folders

3. **Generate worksheets** using specific folders or all folders

That's it! 🎉

---

See `_HOW_TO_ADD_IMAGES.txt` for instructions on adding your own images.
