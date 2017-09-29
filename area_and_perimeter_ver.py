# Created by: Scarlett Gao
# Created on: 21-Sep 2017
# Created for: ICS3U
# This program displays area and perimeter of a rectangle,
# but this time the user can enter different lengths and widths

import ui

def calculate_button_touch_up_inside(sender):
    # calculate area and perimeter
    
    # input
    length = int(view['length_textbox'].text)
    width = int(view['width_textbox'].text)
    
    # process
    area = length * width
    perimeter = 2 * (length + width)
    
    # output
    view['area_answer_label'].text = 'The area is: ' + str(area) + ' cm^2'
    view['perimeter_answer_label'].text = 'The perimeter is: ' + str(perimeter) + ' cm'
    
view = ui.load_view()
view.present('full_screen')
