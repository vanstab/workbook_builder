"""Colour activity - color in images from the coloring_images folder."""

import os
from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
from ..colors import C
from .base import Activity, WIDTH, HEIGHT


class Colour(Activity):
    """Colour activity - displays images from coloring_images folder."""

    name = "colour"
    title = "Color the Pictures"
    instruction = "Use your crayons to color in each picture!"

    def __init__(self, images_per_page=1, folder=None):
        """Initialize colour activity.

        Args:
            images_per_page: Number of images to display per page (1, 2, 4, or 6)
            folder: Specific subfolder to use (e.g., "shapes", "animals"), or None for all
        """
        self.images_per_page = images_per_page
        self.folder = folder

        # Update title if specific folder is selected
        if folder:
            self.title = f"Color the {folder.title()}"

        self._image_files = self._load_image_list()

    def _load_image_list(self):
        """Load list of available coloring images from specified folder or all subfolders."""
        # Get the coloring_images folder path
        package_dir = Path(__file__).parent.parent
        images_dir = package_dir / "coloring_images"

        # Supported image formats
        supported_formats = {'.png', '.jpg', '.jpeg', '.pdf'}

        # Find all image files
        image_files = []

        if not images_dir.exists():
            return image_files

        if self.folder:
            # Load from specific subfolder
            target_dir = images_dir / self.folder
            if target_dir.exists() and target_dir.is_dir():
                for file in target_dir.iterdir():
                    if file.is_file() and file.suffix.lower() in supported_formats:
                        # Skip hidden files and README
                        if not file.name.startswith('.') and not file.name.startswith('_'):
                            image_files.append(file)
        else:
            # Load from all subfolders
            for file in images_dir.rglob('*'):
                if file.is_file() and file.suffix.lower() in supported_formats:
                    # Skip hidden files and README
                    if not file.name.startswith('.') and not file.name.startswith('_'):
                        image_files.append(file)

        return sorted(image_files)  # Sort for deterministic ordering

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw the coloring content - images from folder."""
        if not self._image_files:
            # No images found - show a friendly message
            self._draw_no_images_message(canvas)
            return

        # Select images for this page (deterministic based on page_idx)
        images_to_draw = self._select_images_for_page(page_idx)

        # Draw images in grid layout
        if self.images_per_page == 1:
            self._draw_single_image(canvas, images_to_draw[0])
        elif self.images_per_page == 2:
            self._draw_two_images(canvas, images_to_draw)
        elif self.images_per_page == 4:
            self._draw_four_images(canvas, images_to_draw)
        elif self.images_per_page == 6:
            self._draw_six_images(canvas, images_to_draw)

    def _select_images_for_page(self, page_idx):
        """Select which images to display on this page.

        Uses a shuffled sequence to ensure images don't repeat until all have been shown.

        Args:
            page_idx: Current page index

        Returns:
            List of image file paths to display
        """
        if not self._image_files:
            return []

        # Generate a deterministic shuffle sequence based on a simple LCG
        # This ensures the same images appear in the same order every time,
        # but without repetition until all images have been used
        total_images = len(self._image_files)
        selected = []

        for i in range(self.images_per_page):
            # Calculate which image in the global sequence this is
            global_idx = page_idx * self.images_per_page + i

            # Use deterministic "shuffle" - divide into cycles
            # Within each cycle of total_images, show each image once
            cycle_number = global_idx // total_images
            position_in_cycle = global_idx % total_images

            # Simple deterministic shuffle using prime number
            # This distributes images evenly without obvious patterns
            shuffled_idx = (position_in_cycle * 7919 + cycle_number * 1103) % total_images

            selected.append(self._image_files[shuffled_idx])

        return selected

    def _draw_single_image(self, canvas, image_path):
        """Draw one large centered image."""
        # Center position
        cx = WIDTH / 2
        cy = (self.content_top() + self.content_bottom()) / 2

        # Large size for single image
        max_width = WIDTH - 120
        max_height = self.content_top() - self.content_bottom() - 40

        self._draw_image(canvas, image_path, cx, cy, max_width, max_height)

    def _draw_two_images(self, canvas, image_paths):
        """Draw two images stacked vertically."""
        cx = WIDTH / 2
        available_height = self.content_top() - self.content_bottom()
        spacing = available_height / 2

        max_width = WIDTH - 120
        max_height = spacing - 30

        # Top image
        cy_top = self.content_top() - spacing / 2
        self._draw_image(canvas, image_paths[0], cx, cy_top, max_width, max_height)

        # Bottom image
        if len(image_paths) > 1:
            cy_bottom = self.content_bottom() + spacing / 2
            self._draw_image(canvas, image_paths[1], cx, cy_bottom, max_width, max_height)

    def _draw_four_images(self, canvas, image_paths):
        """Draw four images in 2x2 grid."""
        available_width = WIDTH - 120
        available_height = self.content_top() - self.content_bottom()

        col_width = available_width / 2
        row_height = available_height / 2

        max_img_width = col_width - 20
        max_img_height = row_height - 20

        positions = [
            (60 + col_width / 2, self.content_top() - row_height / 2),  # Top left
            (60 + 3 * col_width / 2, self.content_top() - row_height / 2),  # Top right
            (60 + col_width / 2, self.content_bottom() + row_height / 2),  # Bottom left
            (60 + 3 * col_width / 2, self.content_bottom() + row_height / 2),  # Bottom right
        ]

        for i, (cx, cy) in enumerate(positions):
            if i < len(image_paths):
                self._draw_image(canvas, image_paths[i], cx, cy, max_img_width, max_img_height)

    def _draw_six_images(self, canvas, image_paths):
        """Draw six images in 2x3 grid."""
        available_width = WIDTH - 120
        available_height = self.content_top() - self.content_bottom()

        cols = 2
        rows = 3
        col_width = available_width / cols
        row_height = available_height / rows

        max_img_width = col_width - 20
        max_img_height = row_height - 20

        for i, image_path in enumerate(image_paths):
            if i >= 6:
                break

            row = i // cols
            col = i % cols

            cx = 60 + col * col_width + col_width / 2
            cy = self.content_top() - row * row_height - row_height / 2

            self._draw_image(canvas, image_path, cx, cy, max_img_width, max_img_height)

    def _draw_image(self, canvas, image_path, cx, cy, max_width, max_height):
        """Draw an image centered at (cx, cy) scaled to fit within max dimensions.

        Args:
            canvas: reportlab Canvas
            image_path: Path to image file
            cx, cy: Center coordinates
            max_width, max_height: Maximum dimensions
        """
        try:
            # Get image dimensions
            if image_path.suffix.lower() == '.pdf':
                # For PDF, use a default aspect ratio
                img_width = max_width
                img_height = max_height
            else:
                # For image files, get actual dimensions
                with Image.open(image_path) as img:
                    img_width, img_height = img.size

            # Calculate scaling to fit within max dimensions while preserving aspect ratio
            scale = min(max_width / img_width, max_height / img_height)
            scaled_width = img_width * scale
            scaled_height = img_height * scale

            # Calculate bottom-left position (reportlab uses bottom-left as origin)
            x = cx - scaled_width / 2
            y = cy - scaled_height / 2

            # Draw the image
            canvas.drawImage(
                str(image_path),
                x, y,
                width=scaled_width,
                height=scaled_height,
                preserveAspectRatio=True,
                mask='auto'
            )

        except Exception as e:
            # If image fails to load, draw a placeholder
            self._draw_image_placeholder(canvas, cx, cy, max_width, max_height, str(e))

    def _draw_image_placeholder(self, canvas, cx, cy, width, height, error_msg=""):
        """Draw a placeholder when image can't be loaded."""
        x = cx - width / 2
        y = cy - height / 2

        # Draw dashed rectangle
        canvas.saveState()
        canvas.setStrokeColor(HexColor("#CCCCCC"))
        canvas.setLineWidth(2)
        canvas.setDash(5, 5)
        canvas.rect(x, y, width, height)

        # Draw "Image" text
        canvas.setFillColor(HexColor("#999999"))
        canvas.setFont("Helvetica", 14)
        canvas.drawCentredString(cx, cy, "Image not found")

        canvas.restoreState()

    def _draw_no_images_message(self, canvas):
        """Draw a message when no images are available."""
        cx = WIDTH / 2
        cy = (self.content_top() + self.content_bottom()) / 2

        canvas.saveState()
        canvas.setFillColor(HexColor("#666666"))

        # Title
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(cx, cy + 60, "No Coloring Images Found")

        # Instructions
        canvas.setFont("Helvetica", 14)
        canvas.drawCentredString(cx, cy + 20, "Add PNG, JPG, or PDF images to any folder:")
        canvas.setFont("Helvetica-Oblique", 11)
        canvas.drawCentredString(cx, cy - 10, "workbook_builder/coloring_images/shapes/")
        canvas.drawCentredString(cx, cy - 30, "workbook_builder/coloring_images/animals/")
        canvas.drawCentredString(cx, cy - 50, "workbook_builder/coloring_images/custom/")
        canvas.setFont("Helvetica", 12)
        canvas.drawCentredString(cx, cy - 80, "See _HOW_TO_ADD_IMAGES.txt for help!")

        canvas.restoreState()
