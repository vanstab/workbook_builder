"""
Workbook Generator - Simple Web UI
Run with: streamlit run app.py
"""

import streamlit as st
import sys
from pathlib import Path
from argparse import Namespace

# Add the project to path
sys.path.insert(0, str(Path(__file__).parent))

from workbook_builder.generator import generate
from workbook_builder.icons import available_themes, get_theme

# Page config
st.set_page_config(
    page_title="Worksheet Generator",
    page_icon="✏️",
    layout="wide"
)

# Title and description
st.title("✏️ Workbook Generator")
st.markdown("Create beautiful tracing worksheets for young children (ages 2-5)")

# Sidebar for all options
with st.sidebar:
    st.header("⚙️ Settings")

    # Theme selection
    theme = st.selectbox(
        "🎨 Theme",
        options=available_themes(),
        help="Choose decorative theme for the worksheet"
    )

    # Theme preview
    theme_data = get_theme(theme)
    if "colors" in theme_data and theme_data["colors"]:
        with st.expander("🎨 Theme Color Preview", expanded=False):
            colors = theme_data["colors"]

            def color_to_hex(color):
                """Convert reportlab Color to hex string."""
                # hexval() returns something like '0xff6b9d' or 'ff6b9d'
                hex_val = color.hexval()
                if isinstance(hex_val, int):
                    return f"#{hex_val:06x}"
                else:
                    # It's a string, just format it properly
                    hex_val = str(hex_val).replace('0x', '')
                    return f"#{hex_val}"

            # Background colors
            if "backgrounds" in colors:
                st.markdown("**Page Backgrounds:**")
                bg_html = '<div style="display: flex; gap: 5px; margin-bottom: 10px; flex-wrap: wrap;">'
                for bg in colors["backgrounds"]:
                    hex_str = color_to_hex(bg)
                    bg_html += f'<div style="width: 35px; height: 35px; background-color: {hex_str}; border: 1px solid #ccc; border-radius: 4px;" title="{hex_str}"></div>'
                bg_html += '</div>'
                st.markdown(bg_html, unsafe_allow_html=True)

            # Banner colors
            if "banners" in colors:
                st.markdown("**Banner Colors:**")
                banner_html = '<div style="display: flex; gap: 5px; margin-bottom: 10px; flex-wrap: wrap;">'
                for banner in colors["banners"]:
                    hex_str = color_to_hex(banner)
                    banner_html += f'<div style="width: 35px; height: 35px; background-color: {hex_str}; border: 1px solid #ccc; border-radius: 4px;" title="{hex_str}"></div>'
                banner_html += '</div>'
                st.markdown(banner_html, unsafe_allow_html=True)

            # Accent colors
            if "accents" in colors:
                st.markdown("**Accent Colors:**")
                accent_html = '<div style="display: flex; gap: 5px; flex-wrap: wrap;">'
                for accent in colors["accents"]:
                    hex_str = color_to_hex(accent)
                    accent_html += f'<div style="width: 35px; height: 35px; background-color: {hex_str}; border: 1px solid #ccc; border-radius: 4px;" title="{hex_str}"></div>'
                accent_html += '</div>'
                st.markdown(accent_html, unsafe_allow_html=True)

    # Rows slider
    rows = st.slider(
        "📊 Rows per page",
        min_value=3,
        max_value=6,
        value=5,
        help="More rows = more practice"
    )

    # Line thickness
    thickness = st.slider(
        "📏 Line thickness",
        min_value=2.0,
        max_value=5.0,
        value=3.0,
        step=0.5,
        help="Thicker lines are easier to see"
    )

    # Guide style
    guide_style = st.selectbox(
        "✨ Guide style",
        options=["dashed", "dotted", "solid"],
        help="Line pattern for tracing guides"
    )

    # Math settings
    st.markdown("---")
    st.subheader("➕ Math Settings")

    col1, col2 = st.columns(2)
    with col1:
        math_min = st.number_input(
            "🔢 Min number",
            min_value=0,
            max_value=100,
            value=0,
            help="Minimum number for addition/subtraction (0-100)"
        )
    with col2:
        math_max = st.number_input(
            "🔢 Max number",
            min_value=0,
            max_value=100,
            value=10,
            help="Maximum number for addition/subtraction (0-100)"
        )

    # Build math_range from min/max
    math_range = f"{int(math_min)}-{int(math_max)}"

    problems = st.slider(
        "📝 Problems per page",
        min_value=6,
        max_value=20,
        value=12,
        help="How many math problems on each page"
    )

    # Coloring settings
    st.markdown("---")
    st.subheader("🎨 Coloring Settings")

    colour_folder = st.selectbox(
        "📁 Image folder",
        options=["All folders", "shapes", "animals", "objects", "nature", "custom"],
        help="Choose which folder to use for coloring images"
    )

    # Convert "All folders" to None
    colour_folder = None if colour_folder == "All folders" else colour_folder

    # Spelling settings
    st.markdown("---")
    st.subheader("📝 Spelling Settings")

    col_min, col_max = st.columns(2)
    with col_min:
        min_word_length = st.number_input(
            "Min length:",
            min_value=0,
            max_value=10,
            value=0,
            help="Minimum word length (0 = no minimum)"
        )
    with col_max:
        max_word_length = st.number_input(
            "Max length:",
            min_value=0,
            max_value=10,
            value=0,
            help="Maximum word length (0 = no maximum)"
        )

    # Convert 0 to None
    min_word_length = min_word_length if min_word_length > 0 else None
    max_word_length = max_word_length if max_word_length > 0 else None

    # Output filename
    st.markdown("---")
    output_file = st.text_input(
        "💾 Output filename",
        value="worksheet.pdf",
        help="Name of the PDF file to create"
    )

# Main content area - Mode selection
st.subheader("📋 Worksheet Mode")
mode = st.radio(
    "How would you like to create your worksheet?",
    options=["Custom Page Order", "Activity Selection"],
    horizontal=True,
    help="Custom Page Order: Build exactly what you need with full control | Activity Selection: Traditional checkbox selection"
)

st.markdown("---")

# Variables to hold configuration
custom_pages = None
activities = []
numbers_list = None
letters_list = None

if mode == "Custom Page Order":
    st.subheader("📄 Custom Page Order")

    # Initialize session state for pages if not exists
    if 'custom_pages_list' not in st.session_state:
        st.session_state.custom_pages_list = []

    # Quick add section
    st.markdown("### Quick Add")

    col_add1, col_add2 = st.columns(2)

    with col_add1:
        st.markdown("**📝 Letters & Numbers**")
        letter_input = st.text_input("Add letter:", key="letter_add", placeholder="A, B, C...")

        letter_size = st.selectbox(
            "Size:",
            options=["small", "medium", "large", "extra-large"],
            index=1,
            key="letter_size",
            help="Font size for tracing"
        )

        # Visual preview of size
        size_pixels = {"small": 40, "medium": 60, "large": 80, "extra-large": 100}
        if letter_input and len(letter_input) == 1:
            st.info(f"📏 Size preview - PDF will use single-stroke Hershey font", icon="ℹ️")
            st.markdown(
                f"""<div style='text-align: center; font-size: {size_pixels[letter_size]}px; font-weight: 300;
                color: #4CAF50; padding: 10px; font-family: "Courier New", monospace;
                border: 2px dashed #4CAF50; border-radius: 8px; margin: 10px 0;'>{letter_input}</div>""",
                unsafe_allow_html=True
            )

        if st.button("➕ Add Letter", use_container_width=True):
            if letter_input and len(letter_input) == 1 and letter_input.isalpha():
                page_spec = f"{letter_input}:{letter_size}" if letter_size != "medium" else letter_input
                st.session_state.custom_pages_list.append(page_spec)
                st.rerun()

        st.markdown("---")

        number_input = st.selectbox("Add number:", options=[""] + list(range(10)), key="number_add")

        number_size = st.selectbox(
            "Size:",
            options=["small", "medium", "large", "extra-large"],
            index=1,
            key="number_size",
            help="Font size for tracing"
        )

        # Visual preview of size
        if number_input != "":
            st.info(f"📏 Size preview - PDF will use single-stroke Hershey font", icon="ℹ️")
            st.markdown(
                f"""<div style='text-align: center; font-size: {size_pixels[number_size]}px; font-weight: 300;
                color: #2196F3; padding: 10px; font-family: "Courier New", monospace;
                border: 2px dashed #2196F3; border-radius: 8px; margin: 10px 0;'>{number_input}</div>""",
                unsafe_allow_html=True
            )

        if st.button("➕ Add Number", use_container_width=True):
            if number_input != "":
                page_spec = f"{number_input}:{number_size}" if number_size != "medium" else str(number_input)
                st.session_state.custom_pages_list.append(page_spec)
                st.rerun()

    with col_add2:
        st.markdown("**🎯 Activities**")
        activity_select = st.selectbox(
            "Select activity:",
            options=[""] + ["straight", "wavy", "zigzag", "diagonals", "waves", "loops",
                          "circles", "squares", "triangles", "pentagons", "hexagons",
                          "octagons", "ovals", "rectangles", "trapezoids", "diamonds", "spirals"],
            key="activity_add"
        )
        if st.button("➕ Add Activity", use_container_width=True):
            if activity_select:
                st.session_state.custom_pages_list.append(activity_select)
                st.rerun()

        st.markdown("---")
        st.markdown("**🎨 Coloring**")
        colour_folder_select = st.selectbox(
            "Folder:",
            options=["All folders", "shapes", "animals", "objects", "nature", "custom"],
            key="colour_folder_select",
            help="Choose which images to use"
        )

        if st.button("➕ Add Coloring", use_container_width=True):
            if colour_folder_select == "All folders":
                colour_spec = "colour"
            else:
                colour_spec = f"colour:{colour_folder_select}"
            st.session_state.custom_pages_list.append(colour_spec)
            st.rerun()

    st.markdown("---")

    col_add3, col_add4 = st.columns(2)

    with col_add3:
        st.markdown("**📝 Spelling**")
        st.markdown("**Word Length:**")
        col_min, col_max = st.columns(2)
        with col_min:
            min_len = st.number_input("Min:", min_value=0, max_value=10, value=0, key="spell_min", help="0 = no minimum")
        with col_max:
            max_len = st.number_input("Max:", min_value=0, max_value=10, value=0, key="spell_max", help="0 = no maximum")

        if st.button("➕ Add Spelling", use_container_width=True):
            # Build the spec based on inputs
            if min_len > 0 and max_len > 0:
                spelling_spec = f"spelling:{min_len}-{max_len}"
            elif min_len > 0:
                spelling_spec = f"spelling:{min_len}-10"  # Use 10 as practical max
            elif max_len > 0:
                spelling_spec = f"spelling:1-{max_len}"  # Use 1 as practical min
            else:
                spelling_spec = "spelling"

            st.session_state.custom_pages_list.append(spelling_spec)
            st.rerun()

    with col_add4:
        st.markdown("**➕➖ Math Problems**")
        math_type = st.selectbox("Type:", options=["addition", "subtraction"], key="math_type")
        col_min, col_max = st.columns(2)
        with col_min:
            math_min_custom = st.number_input("Min:", min_value=0, max_value=100, value=0, key="math_min_custom")
        with col_max:
            math_max_custom = st.number_input("Max:", min_value=0, max_value=100, value=10, key="math_max_custom")
        math_problems = st.slider("Problems:", min_value=6, max_value=20, value=12, key="math_problems")

        if st.button("➕ Add Math", use_container_width=True):
            math_range_spec = f"{int(math_min_custom)}-{int(math_max_custom)}"
            math_spec = f"{math_type}:{math_range_spec}:{math_problems}"
            st.session_state.custom_pages_list.append(math_spec)
            st.rerun()

    st.markdown("---")

    # Display current pages
    st.markdown("### 📄 Current Pages")

    if st.session_state.custom_pages_list:
        st.success(f"✅ Total: {len(st.session_state.custom_pages_list)} pages")

        # Show pages as vertical list with delete and move buttons
        for idx, page in enumerate(st.session_state.custom_pages_list):
            col1, col2, col3 = st.columns([1, 6, 1])

            with col1:
                st.markdown(f"**{idx + 1}.**")

            with col2:
                # Format page display nicely
                if ":" in page:
                    parts = page.split(":")
                    # Check if it's a letter/number with size (single char + size name)
                    if len(parts) == 2 and len(parts[0]) == 1 and parts[1] in ["small", "medium", "large", "extra-large"]:
                        char = parts[0]
                        size = parts[1].replace("-", " ").title()
                        if char.isalpha():
                            display = f"**Letter {char}** - {size} size"
                        else:
                            display = f"**Number {char}** - {size} size"
                    # Math page with 3 parts
                    elif len(parts) == 3 and parts[0].lower() in ["addition", "subtraction"]:
                        display = f"**{parts[0].title()}** - {parts[1].title()} ({parts[2]} problems)"
                    # Math page with 2 parts
                    elif len(parts) == 2 and parts[0].lower() in ["addition", "subtraction"]:
                        display = f"**{parts[0].title()}** - {parts[1].title()}"
                    # Spelling with word length
                    elif len(parts) == 2 and parts[0].lower() == "spelling":
                        if "-" in parts[1]:
                            min_len, max_len = parts[1].split("-")
                            if min_len == max_len:
                                display = f"**Spelling** - {min_len} letters only"
                            else:
                                display = f"**Spelling** - {min_len}-{max_len} letter words"
                        else:
                            display = f"**Spelling** - max {parts[1]} letters"
                    # Coloring with folder
                    elif len(parts) == 2 and parts[0].lower() == "colour":
                        display = f"**Coloring** - {parts[1].title()} folder"
                    else:
                        display = page
                else:
                    # No colon - simple page
                    if len(page) == 1 and page.isalpha():
                        display = f"**Letter {page}**"
                    elif len(page) == 1 and page.isdigit():
                        display = f"**Number {page}**"
                    else:
                        display = f"**{page.title()}**"
                st.markdown(display)

            with col3:
                if st.button("🗑️", key=f"delete_{idx}", help=f"Delete {page}"):
                    st.session_state.custom_pages_list.pop(idx)
                    st.rerun()

        # Action button
        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.custom_pages_list = []
            st.rerun()
    else:
        st.warning("No pages yet. Use the 'Quick Add' buttons above to build your worksheet!")

    # Set custom_pages from session state
    custom_pages = st.session_state.custom_pages_list if st.session_state.custom_pages_list else None

    # Advanced: Manual text edit option
    with st.expander("✏️ Advanced: Edit as Text"):
        st.markdown("You can also edit the page list directly as text:")
        manual_pages = st.text_area(
            "Pages (one per line or space-separated):",
            value="\n".join(st.session_state.custom_pages_list),
            height=150,
            help="Edit manually if needed"
        )
        if st.button("💾 Update from Text"):
            # Parse the manual input
            new_pages = [p.strip() for p in manual_pages.replace('\n', ' ').split() if p.strip()]
            st.session_state.custom_pages_list = new_pages
            st.rerun()

else:  # Activity Selection mode
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Line & Shape Activities")
        st.markdown("*Select activities to include:*")

        activities = []

        if st.checkbox("Straight Lines"):
            activities.append("straight")
        if st.checkbox("Wavy Lines"):
            activities.append("wavy")
        if st.checkbox("Zigzag Lines"):
            activities.append("zigzag")
        if st.checkbox("Diagonal Lines"):
            activities.append("diagonals")
        if st.checkbox("Waves"):
            activities.append("waves")
        if st.checkbox("Loops"):
            activities.append("loops")
        if st.checkbox("Circles"):
            activities.append("circles")
        if st.checkbox("Squares"):
            activities.append("squares")
        if st.checkbox("Triangles"):
            activities.append("triangles")
        if st.checkbox("Pentagons"):
            activities.append("pentagons")
        if st.checkbox("Hexagons"):
            activities.append("hexagons")
        if st.checkbox("Octagons"):
            activities.append("octagons")
        if st.checkbox("Ovals"):
            activities.append("ovals")
        if st.checkbox("Rectangles"):
            activities.append("rectangles")
        if st.checkbox("Trapezoids"):
            activities.append("trapezoids")
        if st.checkbox("Diamonds"):
            activities.append("diamonds")
        if st.checkbox("Spirals"):
            activities.append("spirals")

        st.markdown("---")
        st.markdown("**Math Activities:**")
        if st.checkbox("Addition ➕"):
            activities.append("addition")
        if st.checkbox("Subtraction ➖"):
            activities.append("subtraction")

        st.markdown("---")
        st.markdown("**Learning Activities:**")
        if st.checkbox("Spelling 📝"):
            activities.append("spelling")
        if st.checkbox("Coloring 🎨"):
            activities.append("colour")

        if st.button("✅ Select All Activities"):
            activities = ["straight", "wavy", "zigzag", "diagonals", "waves", "loops",
                         "circles", "squares", "triangles", "pentagons", "hexagons", "octagons",
                         "ovals", "rectangles", "trapezoids", "diamonds", "spirals",
                         "addition", "subtraction", "spelling", "colour"]

    with col2:
        st.subheader("🔢 Numbers & Letters")

        # Numbers section
        st.markdown("**Numbers to trace:**")
        include_numbers = st.checkbox("Include numbers", value=False)

        numbers_list = None
        numbers_size = "medium"
        if include_numbers:
            number_option = st.radio(
                "Which numbers?",
                options=["All (0-9)", "Custom selection"],
                horizontal=True
            )

            if number_option == "All (0-9)":
                numbers_list = list(range(10))
            else:
                numbers_input = st.text_input(
                    "Enter numbers (separated by spaces)",
                    value="",
                    placeholder="Example: 1 2 3 or 0 5 9",
                    help="Example: 1 2 3 or 0 5 9"
                )
                try:
                    numbers_list = [int(n.strip()) for n in numbers_input.split() if n.strip().isdigit()]
                except:
                    st.error("Please enter valid numbers (0-9) separated by spaces")
                    numbers_list = []

            # Font size selector
            numbers_size = st.selectbox(
                "Font size for numbers:",
                options=["small", "medium", "large", "extra-large"],
                index=1,
                key="activity_numbers_size"
            )

        st.markdown("---")

        # Letters section
        st.markdown("**Letters to trace:**")
        include_letters = st.checkbox("Include letters", value=False)

        letters_list = None
        letters_size = "medium"
        if include_letters:
            letter_case = st.radio(
                "Letter case:",
                options=["Uppercase", "Lowercase", "Both"],
                horizontal=True
            )

            letter_option = st.radio(
                "Which letters?",
                options=["All", "Custom selection"],
                horizontal=True
            )

            if letter_option == "All":
                if letter_case == "Uppercase":
                    letters_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                elif letter_case == "Lowercase":
                    letters_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
                else:  # Both
                    letters_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
                                  [chr(i) for i in range(ord('a'), ord('z') + 1)]
            else:
                letters_input = st.text_input(
                    "Enter letters (separated by spaces)",
                    value="",
                    placeholder="Example: A B C or a b c (case matters!)",
                    help="Example: A B C or a b c (case matters!)"
                )
                try:
                    # Don't force case - preserve what user enters
                    letters_list = [l.strip() for l in letters_input.split() if l.strip().isalpha() and len(l.strip()) == 1]
                except:
                    st.error("Please enter valid letters separated by spaces")
                    letters_list = []

            # Font size selector
            letters_size = st.selectbox(
                "Font size for letters:",
                options=["small", "medium", "large", "extra-large"],
                index=1,
                key="activity_letters_size"
            )

    # Add numbers/letters to activities if selected (only in Activity Selection mode)
    if include_numbers and numbers_list:
        activities.append("numbers")
    if include_letters and letters_list:
        activities.append("letters")

# Generate button
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("🎨 Generate Worksheet", type="primary", use_container_width=True):
        # Validation based on mode
        valid = True
        if mode == "Activity Selection" and not activities:
            st.error("⚠️ Please select at least one activity!")
            valid = False
        elif mode == "Custom Page Order" and not custom_pages:
            st.error("⚠️ Please specify pages for the worksheet!")
            valid = False

        if valid:
            try:
                # Build args object based on mode
                if mode == "Custom Page Order":
                    args = Namespace(
                        activities=None,
                        pages=custom_pages,
                        lesson=None,
                        theme=theme,
                        numbers=None,
                        letters=None,
                        rows=rows,
                        line_thickness=thickness,
                        guide_style=guide_style,
                        math_range=math_range,
                        problems=problems,
                        min_word_length=min_word_length,
                        max_word_length=max_word_length,
                        output=output_file
                    )
                else:  # Activity Selection
                    args = Namespace(
                        activities=activities,
                        pages=None,
                        lesson=None,
                        theme=theme,
                        numbers=numbers_list,
                        letters=letters_list,
                        numbers_size=numbers_size if include_numbers else None,
                        letters_size=letters_size if include_letters else None,
                        rows=rows,
                        line_thickness=thickness,
                        guide_style=guide_style,
                        math_range=math_range,
                        problems=problems,
                        min_word_length=min_word_length,
                        max_word_length=max_word_length,
                        colour_folder=colour_folder,
                        output=output_file
                    )

                # Generate the PDF
                with st.spinner("Creating your worksheet... ✨"):
                    output_path = generate(args)

                # Success message
                st.success(f"✅ Worksheet created successfully!")

                # Download button
                with open(output_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_file,
                        file_name=output_file,
                        mime="application/pdf",
                        use_container_width=True
                    )

                # Show summary based on mode
                if mode == "Custom Page Order":
                    st.info(f"""
                    **Worksheet Summary:**
                    - **Mode:** Custom Page Order
                    - **Pages:** {len(custom_pages)} pages
                    - **Theme:** {theme}
                    - **File:** {output_path}
                    """)
                else:
                    st.info(f"""
                    **Worksheet Summary:**
                    - **Mode:** Activity Selection
                    - **Theme:** {theme}
                    - **Activities:** {', '.join(activities)}
                    - **Numbers:** {numbers_list if numbers_list else 'None'}
                    - **Letters:** {letters_list if letters_list else 'None'}
                    - **Rows:** {rows}
                    - **File:** {output_path}
                    """)

            except Exception as e:
                st.error(f"❌ Error generating worksheet: {str(e)}")
                st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9em;'>
    Made with ❤️ for young learners | Ages 2-5 |
    <a href='README.md' target='_blank'>View Documentation</a>
</div>
""", unsafe_allow_html=True)

# Help section in expander
with st.expander("ℹ️ How to Use"):
    st.markdown("""
    ### Quick Start Guide

    **Choose a Mode:**
    1. **Custom Page Order** (Recommended!) - Build exactly what you need with full control
    2. **Activity Selection** - Traditional checkbox selection

    **For Custom Page Order Mode:**
    Use the Quick Add buttons to build your worksheet:
    1. **Letters & Numbers:** Type a letter or select a number, choose size, see live preview
    2. **Activities:** Select from dropdown (straight, wavy, circles, etc.)
    3. **Math Problems:** Choose type, number range (min-max), and problem count
    4. Click the relevant "➕ Add" button
    5. Pages appear in the list below - use 🗑️ to remove any page
    6. Generate and download!

    **Font Sizes:**
    - **Small (60pt):** Good for older kids with better control
    - **Medium (90pt):** Standard size, great for most learners
    - **Large (120pt):** Easier for younger kids
    - **Extra-Large (150pt):** Perfect for beginners (ages 2-3)

    **Math Number Range:**
    - **0-5:** Perfect for beginners learning basic addition/subtraction
    - **0-10:** Standard difficulty for most young learners
    - **0-20:** More challenging practice for advanced kids
    - **Custom:** Set any range from 0-100 to match your child's level

    **Example Lesson: "Work on Letter A Today"**
    Add pages in order:
    1. A (letter tracing)
    2. straight (warm-up)
    3. Addition - 0-5 range - 8 problems
    4. circles (related to letter A shape)
    5. A (practice again)
    6. Addition - 0-10 range - 10 problems
    7. wavy (variety)
    8. A (mastery)

    **For Activity Selection Mode:**
    1. Check activities you want (lines, shapes, math)
    2. Add numbers/letters if desired
    3. Adjust settings in sidebar (including min/max number range for math)
    4. Generate and download!

    ### Tips:
    - **Younger kids (2-3):** 3-4 rows, thicker lines (4.0+), simple activities, smaller number ranges (0-5)
    - **Older kids (4-5):** 5-6 rows, standard lines (3.0), all activities, larger number ranges (0-20)
    - **Focused practice:** Use Custom Page Order to repeat specific content
    - **Progressive difficulty:** Start with 0-5, then 0-10, then 0-20, or create custom ranges
    - **Themes:** Each page has fun themed decorations to keep kids engaged
    """)
