from PIL import Image, ImageDraw, ImageFont
import colorsys
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import math

color_dict_ori = {
    "A": {
        "list": [0, 0, 0, 0, 0, 51, 102, 153, 204],
        "freq": 21
    },
    "B": {
        "list": [17, 34, 51, 68, 85, 119, 153, 187, 221],
        "freq": 6,
    },
    "C": {
        "list": [34, 68, 102, 136, 170, 187, 204, 221, 238],
        "freq": 6,
    },
    "D": {
        "list": [51, 102, 153, 204, 255, 255, 255, 255, 255],
        "freq": 21,
    }
}

color_list_ori = [
    {
        "colors": "color-0",
        "values": "DAA"
    },
    {
        "colors": "color-1",
        "values": "DBA"
    },
    {
        "colors": "color-2",
        "values": "DCA"
    },
    {
        "colors": "color-3",
        "values": "DDA"
    },
    {
        "colors": "color-4",
        "values": "CDA"
    },
    {
        "colors": "color-5",
        "values": "BDA"
    },
    {
        "colors": "color-6",
        "values": "ADA"
    },
    {
        "colors": "color-7",
        "values": "ADB"
    },
    {
        "colors": "color-8",
        "values": "ADC"
    },
    {
        "colors": "color-9",
        "values": "ADD"
    },
    {
        "colors": "color-10",
        "values": "ACD"
    },
    {
        "colors": "color-11",
        "values": "ABD"
    },
    {
        "colors": "color-12",
        "values": "AAD"
    },
    {
        "colors": "color-13",
        "values": "BAD"
    },
    {
        "colors": "color-14",
        "values": "CAD'"
    },
    {
        "colors": "color-15",
        "values": "DAD"
    },
    {
        "colors": "color-16",
        "values": "DAC"
    },
    {
        "colors": "color-17",
        "values": "DAB"
    }
]


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

    color_list = [
        {
            "colors": "color-0",
            "values": "DAA"
        },
        {
            "colors": "color-1",
            "values": "DBA"
        },
        {
            "colors": "color-2",
            "values": "DCA"
        },
        {
            "colors": "color-3",
            "values": "DDA"
        },
        {
            "colors": "color-4",
            "values": "CDA"
        },
        {
            "colors": "color-5",
            "values": "BDA"
        },
        {
            "colors": "color-6",
            "values": "ADA"
        },
        {
            "colors": "color-7",
            "values": "ADB"
        },
        {
            "colors": "color-8",
            "values": "ADC"
        },
        {
            "colors": "color-9",
            "values": "ADD"
        },
        {
            "colors": "color-10",
            "values": "ACD"
        },
        {
            "colors": "color-11",
            "values": "ABD"
        },
        {
            "colors": "color-12",
            "values": "AAD"
        },
        {
            "colors": "color-13",
            "values": "BAD"
        },
        {
            "colors": "color-14",
            "values": "CAD'"
        },
        {
            "colors": "color-15",
            "values": "DAD"
        },
        {
            "colors": "color-16",
            "values": "DAC"
        },
        {
            "colors": "color-17",
            "values": "DAB"
        }
    ]
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
    
    
# ----------------------------------------------------------------func----------------------------------------------------------------


def prepare_color(col_list, col_dict):
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
    color_title = []
    for color_group in col_list:
        list_r = color_group['values'][0]
        list_g = color_group['values'][1]
        list_b = color_group['values'][2]
        new_matrix = [col_dict[list_r]['list'], col_dict[list_g]['list'], col_dict[list_b]['list']]
        new_trans = [list(row) for row in zip(*new_matrix)]
        color_array.append(new_trans)
        color_title.append(color_group['values'])
    return color_array, color_title
    pass

def gen_image_rgb(color_groups, column_titles=None, output_path="color_palette.png"):
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
            
            draw.multiline_text((text_x, text_y), text_str, 
                                fill=text_color, 
                                # fill="black", 
                                font=font, align="center")


    # 7. Save the result
    img.save(output_path)

def plot_lines(col_dict, output_path='line.png'):
    plt.clf()
    markers = ['o', 's', '^', 'd', 'v', '<', '>', 'p', '*', 'h']
    
    for i, (key, value) in enumerate(col_dict.items()):
        # Use modulo (%) to cycle back to the start of the marker list if needed
        current_marker = markers[i % len(markers)]
        
        # Plot the line and markers
        plt.plot(value['list'], label=key, marker=current_marker)
        
        # Loop through the list to add text annotations to each marker
        for j, val in enumerate(value['list']):
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

# def extract_lum(color_array):
#     lum_array = []
#     for color_grou[p]

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

    color_array, color_title = prepare_color(color_list, color_dict)
    plot_lines(color_dict, output_path=f"images/lines/line-{A_star}-{A_gap_1}-{A_gap_2}.png")
    gen_image_rgb(color_array, column_titles=color_title, output_path=f"images/palettes/palette-{A_star}-{A_gap_1}-{A_gap_2}.png")


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
    for A_star, A_gap_1, A_gap_2 in poss_list:
        brute_func(A_star, A_gap_1, A_gap_2)

# ----------------------------------------luminance-------------------------------------------------

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


if __name__ == "__main__":
    brute_mini()
    # brute_force()
    # plot_lines(color_dict_4)
    # prepare_color(color_list_4, color_dict_4)
    # prepare_color(color_list_ori, color_dict_ori)
    # prepare_color(color_list_3, color_dict_3)