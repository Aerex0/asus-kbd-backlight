

RBG_values = open_color_picker_via_gtk()
red = green = blue = None

red[0], green[1], blue[2] = RBG_values
print(f"Red: {red}, Green: {green}, Blue: {blue}")