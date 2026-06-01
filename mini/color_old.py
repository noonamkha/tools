
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

D_star = 255
C_star = 247
B_star = 239
A_star = 239

color_dict = {
    "A": {
        "list": [0, 0, 0, 0, 0, 51, 102, 153, 204],
        "freq": 21
    },
    "B": {
        "list": [
            B_star-32*4-16*4, 
            B_star-32*4-16*3, 
            B_star-32*4-16*2, 
            B_star-32*4-16, 
            B_star-32*4, 
            B_star-32*3, 
            B_star-32*2, 
            B_star-32, 
            B_star
        ],
        "freq": 6,
    },
    "C": {
        "list": [
            C_star-16*4-32*4, 
            C_star-16*4-32*3, 
            C_star-16*4-32*2, 
            C_star-16*4-32, 
            C_star-16*4, 
            C_star-16*3, 
            C_star-16*2, 
            C_star-16, 
            C_star
        ],
        "freq": 6,
    },
    "D": {
        # "list": [15, 79, 143, 175, 207, 223, 239, 247, 255],
        "list": [
            D_star-8*3-16*2-32*2-64, 
            D_star-8*3-16*2-32*2, 
            D_star-8*3-16*2-32, 
            D_star-8*3-16*2, 
            D_star-8*3-16, 
            D_star-8*3, 
            D_star-8*2, 
            D_star-8, 
            D_star
        ],
        "freq": 21,
    }
}

mid_star = 24
mid_gap = 26

color_list_4 = [
    {
        "colors": "color-0",
        "values": "DAA"
    },
    {
        "colors": "color-1",
        "values": "DBA"
    },
    # {
    #     "colors": "color-2",
    #     "values": "DCA"
    # },
    {
        "colors": "color-3",
        "values": "DDA"
    },
    {
        "colors": "color-4",
        "values": "CDA"
    },
    # {
    #     "colors": "color-5",
    #     "values": "BDA"
    # },
    {
        "colors": "color-6",
        "values": "ADA"
    },
    # {
    #     "colors": "color-7",
    #     "values": "ADB"
    # },
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
    # {
    #     "colors": "color-11",
    #     "values": "ABD"
    # },
    {
        "colors": "color-12",
        "values": "AAD"
    },
    # {
    #     "colors": "color-13",
    #     "values": "BAD"
    # },
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



def rgb_to_hex(r, g, b):
    """Converts RGB values to a HKX string"""
    return f"#{r:02x}{g:02x}{b:02x}".upper()


def hsl_to_rgb(h, s, l):
    """
    Converts standard HSL values to standard RGB values.
    
    :param h: Hue (0-360 degrees)
    :param s: Saturation (0-100 percent)
    :param l: Lightness (0-100 percent)
    :return: A tuple of (R, G, B) with values from 0-255
    """
    
    # 1. Normalize the HSL values to a 0.0 - 1.0 range
    h_norm = h / 360.0
    s_norm = s / 100.0
    l_norm = l / 100.0

    # 2. Use colorsys to convert (Note the H, L, S order!)
    r_norm, g_norm, b_norm = colorsys.hls_to_rgb(h_norm, l_norm, s_norm)

    # 3. Scale the normalized RGB values back to the standard 0-255 range
    r = round(r_norm * 255)
    g = round(g_norm * 255)
    b = round(b_norm * 255)

    return (r, g, b)


def gen_image_old(color_groups, output_path="color_palette.png"):
    """
    Generates an image displaying columns of color swatches with their values.
    
    :param color_groups: List of lists containing HSL tuples. 
                         Example: [[(0, 100, 50), ...], [(240, 100, 50), ...]]
    :param output_path: String path for saving the image.
    """
    # 1. Layout & Styling Configuration
    box_width = 180
    box_height = 60
    text_area_width = 130
    row_spacing = 5
    col_spacing = 70
    margin_x = 40
    margin_y = 40
    border_thickness = 4
    
    # 2. Calculate dynamic image dimensions based on the input lists
    num_cols = len(color_groups)
    max_rows = max([len(group) for group in color_groups]) if color_groups else 0
    
    img_width = (margin_x * 2) + num_cols * (text_area_width + box_width) + (num_cols - 1) * col_spacing
    img_height = (margin_y * 2) + max_rows * box_height + (max_rows - 1) * row_spacing
    
    # 3. Create white canvas
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)
    
    # Load default font (You can replace this with ImageFont.truetype("arial.ttf", 14) for better looking text)
    font = ImageFont.load_default()

    # 4. Draw color groups column by column
    for col_idx, group in enumerate(color_groups):
        for row_idx, (h, s, l) in enumerate(group):
            # Convert colors
            r, g, b = hsl_to_rgb(h, s, l)
            hex_val = rgb_to_hex(r, g, b)
            
            # Format text strings
            text_str = f"hsl({h}, {s}%, {l}%)\nrgb({r}, {g}, {b})\n{hex_val}"
            
            # Calculate X and Y coordinates for the current row/column
            start_x = margin_x + col_idx * (text_area_width + box_width + col_spacing)
            start_y = margin_y + row_idx * (box_height + row_spacing)
            
            # Text position (aligned slightly down to center next to the box)
            text_x = start_x
            text_y = start_y + (box_height // 5) 
            
            # Box position
            box_x0 = start_x + text_area_width
            box_y0 = start_y
            box_x1 = box_x0 + box_width
            box_y1 = box_y0 + box_height
            
            # Draw multiline text block
            draw.multiline_text((text_x, text_y), text_str, fill="black", font=font, align="right")
            
            # Draw the color swatch rectangle with thick borders
            draw.rectangle(
                [box_x0, box_y0, box_x1, box_y1], 
                fill=(r, g, b), 
                outline="black", 
                width=border_thickness
            )

    # 5. Save the result
    img.save(output_path)
    print(f"Palette successfully saved to: {output_path}")

def extract_color():
    
    # Structure: A list containing lists of HSL tuples (Hue 0-360, Sat 0-100, Light 0-100)
    # Column 1 is reds/warm colors, Column 2 is blues/cool colors

    nam_pallete = []
    color_dict = defaultdict(int)
    for idx, hue in enumerate(range(0, 360, 20)):
        chan_r = []
        chan_g = []
        chan_b = []
        color_group = {
            "colors": f"color-{idx}",
            "values": []
        }
        for light in range(10, 100, 10):
            r, g, b = hsl_to_rgb(hue, 100, light)
            color_group["list"].append(f"{r}{' '*(8-len(str(r)))}{g}{' '*(8-len(str(g)))}{b}")
            chan_r.append(r)
            chan_g.append(g)
            chan_b.append(b)
        nam_pallete.append(color_group)
        tup_r = tuple(chan_r)
        tup_g = tuple(chan_g)
        tup_b = tuple(chan_b)
        color_dict[tup_r] += 1
        color_dict[tup_g] += 1
        color_dict[tup_b] += 1
    with open("colors.json", "w") as json_file:
        # Use json.dump() to write the data to the file
        json.dump(nam_pallete, json_file, indent=4)

A_list = [
            A_star,
            A_star+4,
            A_star+4*2,
            A_star+4*3,
            A_star+4*4,
            A_star+4*4+16,
            A_star+4*4+16*2,
            A_star+4*4+16*2+32,
            A_star+4*4+16*2+32+64,
        ]


B_list = [
    B_star,
    B_star+8,
    B_star+8*2,
    B_star+8*2+16,
    B_star+8*2+16*2,
    B_star+8*2+16*3,
    B_star+8*2+16*4,
    B_star+8*2+16*4+32,
    B_star+8*2+16*4+32*2,
]