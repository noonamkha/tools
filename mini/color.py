from PIL import Image, ImageDraw, ImageFont
import colorsys
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import math
import itertools
import colorsys

# ----------------------------------------------------------------list 4----------------------------------------------------------------
if False:
    # Define A
    color_gap=16
    A_star = 0
    A_gap = int((256-A_star*2-color_gap*3)/4)
    A_list = [
                A_star,
                A_star,
                A_star,
                A_star,
                A_star,
                A_star+A_gap,
                A_star+A_gap*2,
                A_star+A_gap*3,
                A_star+A_gap*4,
            ]
    # Define B
    B_star = A_star+color_gap
    B_mid = int((256-A_star*2)/3)+A_star
    B_gap_1 = int((B_mid-B_star)/4)
    B_gap_2 = int((256-A_star-color_gap*2-B_mid)/4)
    B_list = [
        B_star,
        B_star+B_gap_1,
        B_star+B_gap_1*2,
        B_star+B_gap_1*3,
        B_star+B_gap_1*4,
        B_mid+B_gap_2,
        B_mid+B_gap_2*2,
        B_mid+B_gap_2*3,
        B_mid+B_gap_2*4,
    ]

    # Define C
    C_list = [256-x for x in reversed(B_list)]

    # Define D
    D_list = [256-x for x in reversed(A_list)]

    color_dict = {
        "A": {
            "list": A_list,
            "freq": 21
        },
        "B": {
            "list": B_list,
            "freq": 6,
        },
        "C": {
            "list": C_list,
            "freq": 6,
        },
        "D": {
            "list": D_list,
            "freq": 21,
        }
    }

    color_list = ['DAA', 'DBA', 'DCA', 'DDA', 'CDA', 'BDA', 'ADA', 'ADB', 'ADC', 'ADD', 'ACD', 'ABD', 'AAD', 'BAD', "CAD'", 'DAD', 'DAC', 'DAB']
else:
# ----------------------------------------------------------------list 3----------------------------------------------------------------
    # color_gap=16
    # Define A
    A_star = 32
    # A_gap = int((256-A_star*2-color_gap*2)/4)
    A_gap_1 = 32
    A_gap_2 = 32
    A_list = [
                A_star,
                A_star+A_gap_1,
                A_star+A_gap_1*2,
                A_star+A_gap_1*3,
                A_star+A_gap_1*4,
                A_star+A_gap_1*4+A_gap_2,
                A_star+A_gap_1*4+A_gap_2*2,
                A_star+A_gap_1*4+A_gap_2*3,
                A_star+A_gap_1*4+A_gap_2*4,
            ]
    
    # A_list = [
    #             A_star,
    #             A_star,
    #             A_star,
    #             A_star,
    #             A_star,
    #             A_star+A_gap,
    #             A_star+A_gap*2,
    #             A_star+A_gap*3,
    #             A_star+A_gap*4,
    #         ]
    
    # Define D
    D_list = [256-x for x in reversed(A_list)]

    # Define K
    K_star = int((A_list[0] + D_list[0])/2)
    K_end = int((A_list[-1] + D_list[-1])/2)
    K_gap = int((K_end - K_star) / 8)
    K_list = [
                K_star,
                K_star+K_gap,
                K_star+K_gap*2,
                K_star+K_gap*3,
                K_star+K_gap*4,
                K_star+K_gap*5,
                K_star+K_gap*6,
                K_star+K_gap*7,
                K_star+K_gap*8,
            ]
    
    color_dict = {
        "A": A_list,
        "K": K_list,
        "D": D_list
    }

    # color list
    color_list = ['DAA', 'DKA', 'DDA', 'KDA', 'ADA', 'ADK', 'ADD', 'AKD', 'AAD', 'KAD', 'DAD', 'DAK']
    
    
# ----------------------------------------------------------------func----------------------------------------------------------------
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def prepare_color(col_list, col_map):
    # my_colors = [
    #     [
    #         (0, 100, 50),   # Pure Red
    #         (15, 100, 50),  # Orange-Red
    #         (30, 100, 50),  # Orange
    #         (45, 100, 50),  # Yellow-Orange
    #         (60, 100, 50)   # Yellow
    #     ],
    #     [
    #         (180, 100, 50), # Cyan
    #         (210, 100, 50), # Light Blue
    #         (240, 100, 50), # Blue
    #         (270, 100, 50), # Purple
    #         (359+30, 100, 50)  # Magenta
    #     ]
    # ]
    # generate_palette_image(nam_pallete, "final_color_palette.png")
    color_array = []
    for color_group in col_list:
        list_r = color_group[0]
        list_g = color_group[1]
        list_b = color_group[2]
        new_matrix = [col_map[list_r], col_map[list_g], col_map[list_b]]
        new_trans = transpose(new_matrix)
        color_array.append(new_trans)
    return color_array

# def gen_image_rgb(color_groups, column_titles=None, output_path="color_palette.png", print_text=False):
    # 1. Layout & Styling Configuration
    box_width = 120  # Increased to fit multiline text inside
    box_height = 60  # Increased to fit multiline text inside
    row_spacing = 0  # Added slight vertical gap so boxes don't blend together
    col_spacing = 0
    margin_x = 10
    margin_y = 10
    border_thickness = 0 # Set to 1 so very light colors still have a visible boundary
    
    # 2. Header configuration
    header_height = 20 if column_titles else 0
    
    # 3. Calculate dynamic image dimensions
    num_cols = len(color_groups)
    max_rows = max([len(group) for group in color_groups]) if color_groups else 0
    
    # Removed text_area_width from image width calculation
    img_width = (margin_x * 2) + num_cols * box_width + (num_cols - 1) * col_spacing
    img_height = (margin_y * 2) + header_height + (max_rows * box_height) + ((max_rows - 1) * row_spacing)
    
    # 4. Create white canvas
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    # 5. Draw column titles if provided
    if column_titles:
        for col_idx, title in enumerate(column_titles):
            if col_idx < num_cols:
                start_x = margin_x + col_idx * (box_width + col_spacing)
                
                bbox = draw.textbbox((0, 0), title, font=font)
                text_w = bbox[2] - bbox[0]
                
                title_x = start_x + (box_width // 2) - (text_w // 2)
                title_y = margin_y
                draw.text((title_x, title_y), title, fill="black", font=font)

    # 6. Draw color swatches and text
    for col_idx, group in enumerate(color_groups):
        for row_idx, (r, g, b) in enumerate(group):
            hex_val = f"#{r:02x}{g:02x}{b:02x}".upper() 
            
            # Calculate box positions
            start_x = margin_x + col_idx * (box_width + col_spacing)
            start_y = margin_y + header_height + row_idx * (box_height + row_spacing)
            
            box_x0 = start_x
            box_y0 = start_y
            box_x1 = box_x0 + box_width
            box_y1 = box_y0 + box_height
            
            # Draw the color swatch rectangle FIRST
            draw.rectangle(
                [box_x0, box_y0, box_x1, box_y1], 
                fill=(r, g, b), 
                # fill=(255, 255, 255), 
                outline="black", 
                width=border_thickness
            )
            lum = relative_luminance([r, g, b])
            text_str = f"{lum:4f}\nrgb({r}, {g}, {b})\n{hex_val}"
            text_color = get_text_color([r, g, b])
            # Calculate text size to center it perfectly
            text_bbox = draw.multiline_textbbox((0, 0), text_str, font=font)
            text_w = text_bbox[2] - text_bbox[0]
            text_h = text_bbox[3] - text_bbox[1]
            
            text_x = box_x0 + (box_width - text_w) // 2
            text_y = box_y0 + (box_height - text_h) // 2
            
            # Smart Contrast: Calculate perceived luminance to decide text color
            if print_text:
                draw.multiline_text((text_x, text_y), text_str, 
                                    fill=text_color, 
                                    # fill="black", 
                                    font=font, align="center")
    # 7. Save the result
    img.save(output_path)

def gen_image_rgb(color_groups, column_titles=None, output_path="color_palette.png",
                  print_text=False, num_rows=1):
    # 1. Layout & Styling Configuration
    box_width = 120
    box_height = 60
    row_spacing = 0
    col_spacing = 0
    band_spacing = 20   # vertical gap between bands (rows of groups)
    margin_x = 10
    margin_y = 10
    border_thickness = 0

    # 2. Header configuration
    header_height = 20 if column_titles else 0

    # 3. Split groups into bands (rows)
    num_groups = len(color_groups)
    num_rows = max(1, num_rows)
    cols_per_row = math.ceil(num_groups / num_rows) if num_groups else 0

    # Per-band info: list of (group_index, group) tuples
    bands = []
    for b in range(num_rows):
        start = b * cols_per_row
        end = min(start + cols_per_row, num_groups)
        if start >= num_groups:
            break
        bands.append(list(range(start, end)))

    # Max swatch-rows within each band (for that band's height)
    def band_max_rows(group_indices):
        return max((len(color_groups[i]) for i in group_indices), default=0)

    band_heights = []
    for group_indices in bands:
        mr = band_max_rows(group_indices)
        h = header_height + mr * box_height + max(0, mr - 1) * row_spacing
        band_heights.append(h)

    # Starting y position for each band
    band_y_starts = []
    y = margin_y
    for h in band_heights:
        band_y_starts.append(y)
        y += h + band_spacing

    # 4. Calculate dynamic image dimensions
    img_width = (margin_x * 2) + cols_per_row * box_width + max(0, cols_per_row - 1) * col_spacing
    img_height = (margin_y * 2) + sum(band_heights) + max(0, len(bands) - 1) * band_spacing

    # 5. Create white canvas
    img = Image.new("RGB", (max(img_width, 1), max(img_height, 1)), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # 6. Draw everything band by band
    for band_idx, group_indices in enumerate(bands):
        band_top = band_y_starts[band_idx]

        for col_in_band, group_idx in enumerate(group_indices):
            group = color_groups[group_idx]
            start_x = margin_x + col_in_band * (box_width + col_spacing)

            # Column title (indexed by the global group index)
            if column_titles and group_idx < len(column_titles):
                title = column_titles[group_idx]
                bbox = draw.textbbox((0, 0), title, font=font)
                text_w = bbox[2] - bbox[0]
                title_x = start_x + (box_width // 2) - (text_w // 2)
                title_y = band_top
                draw.text((title_x, title_y), title, fill="black", font=font)

            # Color swatches
            for row_idx, (r, g, b) in enumerate(group):
                hex_val = f"#{r:02x}{g:02x}{b:02x}".upper()

                box_x0 = start_x
                box_y0 = band_top + header_height + row_idx * (box_height + row_spacing)
                box_x1 = box_x0 + box_width
                box_y1 = box_y0 + box_height

                draw.rectangle(
                    [box_x0, box_y0, box_x1, box_y1],
                    fill=(r, g, b),
                    outline="black",
                    width=border_thickness
                )

                lum = relative_luminance([r, g, b])
                text_str = f"{lum:4f}\nrgb({r}, {g}, {b})\n{hex_val}"
                text_color = get_text_color([r, g, b])

                text_bbox = draw.multiline_textbbox((0, 0), text_str, font=font)
                text_w = text_bbox[2] - text_bbox[0]
                text_h = text_bbox[3] - text_bbox[1]
                text_x = box_x0 + (box_width - text_w) // 2
                text_y = box_y0 + (box_height - text_h) // 2

                if print_text:
                    draw.multiline_text((text_x, text_y), text_str,
                                        fill=text_color, font=font, align="center")

    # 7. Save the result
    img.save(output_path)


def plot_lines(col_map, output_path='line.png'):
    plt.clf()
    markers = ['o', 's', '^', 'd', 'v', '<', '>', 'p', '*', 'h']
    
    for i, (key, value) in enumerate(col_map.items()):
        # Use modulo (%) to cycle back to the start of the marker list if needed
        current_marker = markers[i % len(markers)]
        
        # Plot the line and markers
        plt.plot(value, label=key, marker=current_marker)
        
        # Loop through the list to add text annotations to each marker
        for j, val in enumerate(value):
            # j is the x-coordinate (index), val is the y-coordinate (value)
            # ha='center' centers the text horizontally over the marker
            # va='bottom' places the text slightly above the center of the marker
            plt.text(j, val, str(val), fontsize=9, ha='center', va='bottom')

    # Customizing the plot
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Line Plot of Arrays')
    plt.legend()       # Shows the legend to identify which line is which
    plt.grid(True)     # Adds a grid for easier reading

    # Save first, then display!
    plt.savefig(output_path)
    plt.show()
    plt.close()

def avg_lum(color_array):
    lum_array = []
    for idx, color_group in enumerate(color_array):
        lum_array.append([])
        for r, g, b in color_group:
            lum = relative_luminance([r,g,b])
            lum_array[-1].append(lum)
    lum_array = transpose(lum_array)
    lum_avg = [f"{sum(grp)/len(grp):.5f}" for grp in lum_array]
    return lum_avg
    

def brute_func(A_star, A_gap_1, A_gap_2):
    A_list = [
                A_star,
                A_star+A_gap_1,
                A_star+A_gap_1*2,
                A_star+A_gap_1*3,
                A_star+A_gap_1*4,
                A_star+A_gap_1*4+A_gap_2,
                A_star+A_gap_1*4+A_gap_2*2,
                A_star+A_gap_1*4+A_gap_2*3,
                A_star+A_gap_1*4+A_gap_2*4,
            ]
    
    # Define D
    D_list = [256-x for x in reversed(A_list)]

    # Define K
    K_star = int((A_list[0] + D_list[0])/2)
    K_end = int((A_list[-1] + D_list[-1])/2)
    K_gap = int((K_end - K_star) / 8)
    K_list = [
                K_star,
                K_star+K_gap,
                K_star+K_gap*2,
                K_star+K_gap*3,
                K_star+K_gap*4,
                K_star+K_gap*5,
                K_star+K_gap*6,
                K_star+K_gap*7,
                K_star+K_gap*8,
            ]
    
    color_dict = {
        "A": {
            "list": A_list,
            "freq": 21
        },
        "K": {
            "list": K_list,
            "freq": 6,
        },
        "D": {
            "list": D_list,
            "freq": 21,
        }
    }

    # color list
    color_list = [
        {
            "colors": "color-0",
            "values": "DAA"
        },
        {
            "colors": "color-1",
            "values": "DKA"
        },
        {
            "colors": "color-2",
            "values": "DDA"
        },
        {
            "colors": "color-3",
            "values": "KDA"
        },
        {
            "colors": "color-4",
            "values": "ADA"
        },
        {
            "colors": "color-5",
            "values": "ADK"
        },
        {
            "colors": "color-6",
            "values": "ADD"
        },
        {
            "colors": "color-7",
            "values": "AKD"
        },
        {
            "colors": "color-8",
            "values": "AAD"
        },
        {
            "colors": "color-9",
            "values": "KAD"
        },
        {
            "colors": "color-10",
            "values": "DAD"
        },
        {
            "colors": "color-11",
            "values": "DAK"
        }
    ]

    color_array = prepare_color(color_list, color_dict)
    return avg_lum(color_array)
    # plot_lines(color_dict, output_path=f"images/lines/line-{A_star}-{A_gap_1}-{A_gap_2}.png")
    # gen_image_rgb(color_array, column_titles=color_title, output_path=f"images/palettes/palette-{A_star}-{A_gap_1}-{A_gap_2}.png")


def brute_force():
    pass
    list_A_star = [8, 16, 24, 32, 40]
    list_A_gap_1 = [8, 16]
    list_A_gap_2 = [24, 32, 40]
    # list_A_star = [8]
    # list_A_gap_1 = [16]
    # list_A_gap_2 = [32]

    for A_star in list_A_star:
        for A_gap_1 in list_A_gap_1:
            for A_gap_2 in list_A_gap_2:
                brute_func(A_star, A_gap_1, A_gap_2)
                
def brute_mini():
    poss_list = [
        [8, 8, 40],
        [8, 16, 32],
        [16, 8, 40],
        [16, 16, 32],
    ]
    lum_list = []
    for A_star, A_gap_1, A_gap_2 in poss_list:
        lum_list.append(brute_func(A_star, A_gap_1, A_gap_2))
    lum_list = transpose(lum_list)
    with open("lum.json", "w") as file:
        json.dump(lum_list, file)


# ----------------------------------------luminance-------------------------------------------------
def hex_to_rgb(hex_str):
    # Remove the '#' character if present
    h = hex_str.lstrip('#')
    # Convert hex slices directly to integer values
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def convert_ok(L, C, H):
    """
    Convert OKLCH to sRGB.
      L: lightness  (0..1)
      C: chroma     (~0..0.4)
      H: hue        (degrees, 0..360)
    Returns (r, g, b) as integers 0..255.
    """
    # 1. OKLCH -> OKLab  (polar to cartesian)
    h = math.radians(H)
    a = C * math.cos(h)
    b = C * math.sin(h)

    # 2. OKLab -> linear sRGB  (Björn Ottosson's matrices)
    L = L/100
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b

    l, m, s = l_**3, m_**3, s_**3

    r_lin =  4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g_lin = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_lin = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

    # 3. linear sRGB -> sRGB (gamma encode), with per-channel gamut clip
    def gamma(x):
        # x = max(0.0, min(1.0, x))           # clamp out-of-gamut values
        if x <= 0.0031308:
            return 12.92 * x
        return 1.055 * (x ** (1 / 2.4)) - 0.055
    r = gamma(r_lin)
    g = gamma(g_lin)
    b = gamma(b_lin)
    r_255 = max(0, min(255, round(r * 255)))
    g_255 = max(0, min(255, round(g * 255)))
    b_255 = max(0, min(255, round(b * 255)))
    # final_color = tuple(round(gamma(c) * 255) for c in (r_lin, g_lin, b_lin))
    return (r_255, g_255, b_255)

def relative_luminance(rgb):
    """Relative luminance per WCAG 2.x. rgb is a tuple of 0-255 ints."""
    def linearize(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (linearize(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b
def contrast_ratio(l1, l2):
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def get_text_color(bg_rgb):

    """Return black or white (as RGB) for best contrast on bg_rgb."""
    lum = relative_luminance(bg_rgb)
    # threshold = math.sqrt(0.0525)-0.05
    # return (0, 0, 0) if lum > threshold else (255, 255, 255)
    white = contrast_ratio(lum, 1.0)   # white luminance = 1.0
    black = contrast_ratio(lum, 0.0)   # black luminance = 0.0
    return (255, 255, 255) if white >= black else (0, 0, 0)

# ----------------------------------------old-------------------------------------------------
def got_text_color(bg_rgb):
    brightness = (bg_rgb[0] * 299 + bg_rgb[1] * 587 + bg_rgb[2] * 114) / 1000
    return (0, 0, 0) if brightness > 128 else (255, 255, 255)

def build_ok():
    ok_list = []
    for hue in range(24, 361, 24):
        ok_list.append([])
        for light in range(5, 100, 10):
            new_color = convert_ok(light, 0.1, hue)
            ok_list[-1].append(new_color)
    gen_image_rgb(ok_list,  output_path="ok.png")
    gen_image_rgb(ok_list,  output_path="ok_text.png", print_text=True)
    
def google():
    pass
    google_list = [
        "#EA4335",
        "#34A853",
        "#4285F4",
        "#FBBC05",
        "#E37400"
    ]
    # lum_list = [relative_luminance(hex_to_rgb(col)) for col in google_list]
    # rgb_list = [hex_to_rgb(col) for col in google_list]
    lum_list = [
        0.21763776240210037, 
        0.29359861237316676, 
        0.24464961992425516, 
        0.5648662643283174, 
        0.2882167569992944
    ]
    # 32 96 160 224
    # rgb_list = [
    #     "rgb(224, 96, 96)", 
    #     "rgb(96, 224, 160)", 
    #     "rgb(96, 160, 224)", 
    #     "rgb(224, 160, 32)", 
    #     "rgb(224, 96, 32)"
    # ]
    # # 0 85 170 255
    # rgb_list = [
    #     "rgb(255, 85, 85)", 
    #     "rgb(85, 255, 170)", 
    #     "rgb(85, 170, 255)", 
    #     "rgb(255, 170, 0)", 
    #     "rgb(255, 85, 0)"
    # ]
    rgb_list = [
        "rgb(234, 67, 53)", 
        "rgb(227, 116, 0)"
        "rgb(251, 188, 5)", 
        "rgb(52, 168, 83)", 
        "rgb(66, 133, 244)", 
    ]
    # 8 68 128 188 248
    rgb_list = [
        "rgb(248, 68, 68)", 
        "rgb(248, 128, 8)"
        "rgb(248, 188, 8)", 
        "rgb(248, 248, 68)", 
        "rgb(188, 248, 8)",
        "rgb(128, 248, 68)",
        "rgb(68, 248, 8)",
        "rgb(68, 188, 68)", 
        "rgb(68, 248, 188)",
        "rgb(68, 188, 188)", 
        "rgb(68, 128, 248)", 
    ]
    # 8 68 128 188 248
    rgb_list = [
        "rgb(248, 68, 68)", 
        "rgb(248, 128, 8)" 
        "rgb(248, 188, 8)", 
        "rgb(248, 248, 68)", 
        "rgb(188, 248, 8)", # 8 or 68
        "rgb(128, 248, 68)", 
        "rgb(68, 248, 68)", 
        "rgb(8, 248, 128)", 
        "rgb(8, 248, 188)", 
        "rgb(68, 248, 248)", 
        "rgb(68, 188, 248)", 
        "rgb(68, 128, 248)", 
        "rgb(68, 68, 248)", 
        "rgb(128, 8, 248)", 
        "rgb(248, 68, 248)", 
        "rgb(248, 8, 188)",
    ]
    # 32 64 128 192 224
    rgb_list = [
        "rgb(224, 64, 64)", 
        "rgb(64, 192, 64)", 
        "rgb(64, 128, 224)", 
        "rgb(224, 192, 32)", 
        "rgb(224, 128, 32)"
    ]
    # 32 80 128 176 224
    rgb_list = [
        "rgb(232, 24, 24)", 
        "rgb(224, 128, 32)",
        "rgb(224, 176, 32)", 
        "rgb(80, 176, 80)", 
        "rgb(80, 128, 224)", 
        "rgb(66, 66, 240)" #AAD
        "rgb(124, 66, 240)" #BAD
    ]
    # 8 68 128 188 248 
    # A B  K   C   D
    rgb_list = [
        "DBB rgb(248, 68, 68)", # new
        "DKA rgb(248, 128, 8)" 
        "DCA rgb(248, 188, 8)", 
        "DDB rgb(248, 248, 68)", # new
        "CDA rgb(188, 248, 8)", 
        "KDB rgb(128, 248, 8)", 
        "BDB rgb(68, 248, 68)",# new
        "ADK rgb(68, 248, 128)", 
        "ADC rgb(8, 248, 188)", 
        "BDD rgb(68, 248, 248)",  # new
        "BCD rgb(68, 188, 248)", 
        "BKD rgb(68, 128, 248)", 
        "BBD rgb(68, 68, 248)", # new
        "KBD rgb(128, 68, 248)", 
        "CBD rgb(188, 68, 248)", 
        "DBD rgb(248, 68, 248)", # new
        "DBC rgb(248, 68, 188)", 
        "DBK rgb(248, 68, 128)", 
    ]

def hue(rgb):
    r, g, b = [x / 255 for x in rgb]
    return colorsys.rgb_to_hsv(r, g, b)[0]   # 0..1
def new_sys():
    # values = [32, 64, 128, 192, 224]
    # values = [32, 96, 128, 160, 224]
    values = [32, 80, 128, 176, 224]
    # values = [0, 85, 128, 170, 255]

    # Each of R, G, B can independently be any of the 4 values → 4**3 = 64 combos
    combos = itertools.product(values, repeat=3)

    # Remove grays (R == G == B). Their hue is undefined, so they can't be sorted by hue.
    colors = [c for c in combos if not (c[0] == c[1] == c[2])]   # 60 colors


    colors_sorted = sorted(colors, key=hue)
    colors_rgb = [f"rgb{str(item)}" for item in colors_sorted]
    color_key = {
        values[0]: "A",
        values[1]: "B",
        values[2]: "K",
        values[3]: "C",
        values[4]: "D",
    }
    color_dict = [f"{color_key[item[0]]}{color_key[item[1]]}{color_key[item[2]]}" for item in colors_sorted]
    with open("color-dict-5.json", "w") as file:
        json.dump(color_dict, file, indent=4)
    
    # with open("color_list_2.json", "w") as file:
    #     json.dump(colors_rgb, file, indent=4)
    pass


def brute_four():
    # -------------------------profile 0
    # mid_A = 0
    # mid_B = 85
    # mid_C = 170
    # mid_D = 255
    # outer_gap_slow = 0
    # outer_gap_fast = 51
    # inner_gap_slow = 17
    # inner_gap_fast = 34
    # -------------------------profile 1
    # mid_A = 24
    # mid_B = 92
    # mid_C = 164
    # mid_D = 232
    # outer_gap_slow = 4
    # outer_gap_fast = 46
    # inner_gap_slow = 18
    # inner_gap_fast = 32
    # -------------------------profile 2
    # mid_A = 32
    # mid_B = 95
    # mid_C = 160
    # mid_D = 223
    # outer_gap_slow = 8
    # outer_gap_fast = 44
    # inner_gap_slow = 20
    # inner_gap_fast = 32
    # -------------------------profile 3
    # mid_A = 32
    # mid_B = 96
    # mid_C = 160
    # mid_D = 224
    # outer_gap_slow = 4
    # outer_gap_fast = 40
    # inner_gap_slow = 16
    # inner_gap_fast = 28
    # -------------------------profile 4
    mid_A = 103
    mid_B = 151
    mid_C = 199
    mid_D = 247

    # outer_gap_slow = 2
    # outer_gap_fast = 26
    # inner_gap_slow = 10
    # inner_gap_fast = 18

    start_A = 7
    start_B = 23
    start_C = 39
    start_D = 55
    
    end_A = 207
    end_B = 223
    end_C = 239
    end_D = 255

    dark_A = round((mid_A-start_A)/4)
    dark_B = round((mid_B-start_B)/4)
    dark_C = round((mid_C-start_C)/4)
    dark_D = round((mid_D-start_D)/4)
    
    light_A = round((end_A-mid_A)/4)
    light_B = round((end_B-mid_B)/4)
    light_C = round((end_C-mid_C)/4)
    light_D = round((end_D-mid_D)/4)

    color_map = {
        "A": [
                mid_A-dark_A*4,
                mid_A-dark_A*3,
                mid_A-dark_A*2,
                mid_A-dark_A,
                mid_A,
                mid_A+light_A,
                mid_A+light_A*2,
                mid_A+light_A*3,
                mid_A+light_A*4,
            ],
        "B": [
                mid_B-inner_gap_slow*4,
                mid_B-inner_gap_slow*3,
                mid_B-inner_gap_slow*2,
                mid_B-inner_gap_slow,
                mid_B,
                mid_B+inner_gap_fast,
                mid_B+inner_gap_fast*2,
                mid_B+inner_gap_fast*3,
                mid_B+inner_gap_fast*4,
            ],
        "C": [
                mid_C-inner_gap_fast*4,
                mid_C-inner_gap_fast*3,
                mid_C-inner_gap_fast*2,
                mid_C-inner_gap_fast,
                mid_C,
                mid_C+inner_gap_slow,
                mid_C+inner_gap_slow*2,
                mid_C+inner_gap_slow*3,
                mid_C+inner_gap_slow*4,
            ],
        "D": [
                mid_D-outer_gap_fast*4,
                mid_D-outer_gap_fast*3,
                mid_D-outer_gap_fast*2,
                mid_D-outer_gap_fast,
                mid_D,
                mid_D+outer_gap_slow,
                mid_D+outer_gap_slow*2,
                mid_D+outer_gap_slow*3,
                mid_D+outer_gap_slow*4,
            ],
    }
    with open('color-dict-18.json', 'r') as file:
        color_dlist = json.load(file)
    color_list = prepare_color(col_list=color_dlist, col_map=color_map)
    # color_flat = [item for sublist in color_list for item in sublist]
    # colors_sorted = sorted(color_flat, key=hue)
    
    # for idx, color in enumerate(color_flat):
    #     if color != colors_sorted[idx]:
    #         break
    
    gen_image_rgb(color_list, column_titles=color_dlist, output_path="color_palette-185.png", print_text=False)
    gen_image_rgb(color_list, column_titles=color_dlist, output_path="color_palette-185-text.png", print_text=True)


    plot_lines(color_map, output_path='line-185.png')
    pass


def brute_five():
    # -------------------------profile 0
    mid_A = 8
    mid_B = 68
    mid_K = 128
    mid_C = 188
    mid_D = 248

    outer_gap_slow = 0
    outer_gap_fast = 44
    mid_gap = 22
    inner_gap_slow = 11
    inner_gap_fast = 33
    # -------------------------profile 1
    # mid_A = 32
    # mid_B = 64
    # mid_K = 128
    # mid_C = 192
    # mid_D = 224

    # outer_gap_slow = 4
    # outer_gap_fast = 40
    # mid_gap = 22
    # inner_gap_slow = 10
    # inner_gap_fast = 34
    # -------------------------profile 2
    # mid_A = 32
    # mid_B = 80
    # mid_K = 128
    # mid_C = 176
    # mid_D = 224

    # outer_gap_slow = 4
    # outer_gap_fast = 40
    # mid_gap = 22
    # inner_gap_slow = 13
    # inner_gap_fast = 31
    # -------------------------profile 3
    # mid_A = 32
    # mid_B = 96
    # mid_K = 128
    # mid_C = 160
    # mid_D = 224

    # outer_gap_slow = 4
    # outer_gap_fast = 40
    # mid_gap = 22
    # inner_gap_slow = 16
    # inner_gap_fast = 28
    # -------------------------color map
    color_map = {
        "A": [
                mid_A-outer_gap_slow*4,
                mid_A-outer_gap_slow*3,
                mid_A-outer_gap_slow*2,
                mid_A-outer_gap_slow,
                mid_A,
                mid_A+outer_gap_fast,
                mid_A+outer_gap_fast*2,
                mid_A+outer_gap_fast*3,
                mid_A+outer_gap_fast*4,
            ],
        "B": [
                mid_B-inner_gap_slow*4,
                mid_B-inner_gap_slow*3,
                mid_B-inner_gap_slow*2,
                mid_B-inner_gap_slow,
                mid_B,
                mid_B+inner_gap_fast,
                mid_B+inner_gap_fast*2,
                mid_B+inner_gap_fast*3,
                mid_B+inner_gap_fast*4,
            ],
        "K": [
                mid_K-mid_gap*4,
                mid_K-mid_gap*3,
                mid_K-mid_gap*2,
                mid_K-mid_gap,
                mid_K,
                mid_K+mid_gap,
                mid_K+mid_gap*2,
                mid_K+mid_gap*3,
                mid_K+mid_gap*4,
            ],
        "C": [
                mid_C-inner_gap_fast*4,
                mid_C-inner_gap_fast*3,
                mid_C-inner_gap_fast*2,
                mid_C-inner_gap_fast,
                mid_C,
                mid_C+inner_gap_slow,
                mid_C+inner_gap_slow*2,
                mid_C+inner_gap_slow*3,
                mid_C+inner_gap_slow*4,
            ],
        "D": [
                mid_D-outer_gap_fast*4,
                mid_D-outer_gap_fast*3,
                mid_D-outer_gap_fast*2,
                mid_D-outer_gap_fast,
                mid_D,
                mid_D+outer_gap_slow,
                mid_D+outer_gap_slow*2,
                mid_D+outer_gap_slow*3,
                mid_D+outer_gap_slow*4,
            ],
    }
    with open('color-dict-120-filter.json', 'r') as file:
        color_dict = json.load(file)
    plot_lines(color_map, output_path='line-50.png')
    # quit()
    color_list = prepare_color(col_list=color_dict, col_map=color_map)
    # color_flat = [item for sublist in color_list for item in sublist]
    # colors_sorted = sorted(color_flat, key=hue)
    
    # for idx, color in enumerate(color_flat):
    #     if color != colors_sorted[idx]:
    #         break
    
    gen_image_rgb(color_list, column_titles=color_dict, output_path="color_palette-50f.png", print_text=False, num_rows=3)
    gen_image_rgb(color_list, column_titles=color_dict, output_path="color_palette-50f-text.png", print_text=True, num_rows=3)


    pass

if __name__ == "__main__":
    # result = convert_ok(90, 0.2, 200)
    # build_ok()
    # brute_five()
    # new_sys()
    # brute_mini()
    brute_four()
    # plot_lines(color_dict_4)
    # prepare_color(color_list_4, color_dict_4)
    # prepare_color(color_list_ori, color_dict_ori)
    # prepare_color(color_list_3, color_dict_3)
