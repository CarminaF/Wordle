from colored import fg, bg, attr

####### COLORS GLOBAL DICTIONARY #########
# - Initializing global colors dictionary for 
#   better readability
# - Utilises colored module
COLORS = {
    "green_bg": bg(28),
    "yellow_bg": bg(94),
    "grey_bg": bg(243),
    "red_font": fg(1),
    "blue_font": fg(6),
    "green_font": fg(28),
    "yellow_font": fg(11),
    "pink_font": fg(199),
    "reset": attr('reset')
}
