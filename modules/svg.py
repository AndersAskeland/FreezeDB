# -----------------------------------------------------------------------------
# Module: SVG images   
#
# What: SVG images and class functions to change colors.  
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules

# Local functions 

# Local classes 

# Local resources 

# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class Icons:
    def svg_moon(self):
        pass

def convert_svg_bytes(svg):
    ''' Converts svg text definition to bytes. '''
    return bytearray(svg, encoding='utf-8')

def change_icon_color(theme):
    if theme == "dark":
        pass
    else:
        pass




svg_moon =  '''<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24" fill="#f5f5f5" width="500px" height="500px"><rect fill="none" height="24" width="24"/><path d="M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36c-0.98,1.37-2.58,2.26-4.4,2.26 c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z"/></svg>'''

svg_sun =   '''<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24" fill="#333333" width="500px" height="500px"><rect fill="none" height="24" width="24"/><path d="M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5S14.76,7,12,7L12,7z M2,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0 c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2 c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1 C11.45,19,11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06 c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41 l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41 c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36 c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z"/></svg>'''

# --------------------------- # 
svg_menu_white = """
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <rect width="352" height="32" x="80" y="96" fill="var(--ci-primary-color, currentColor)" class="ci-primary"/>
                    <rect width="352" height="32" x="80" y="240" fill="var(--ci-primary-color, currentColor)" class="ci-primary"/>
                    <rect width="352" height="32" x="80" y="384" fill="var(--ci-primary-color, currentColor)" class="ci-primary"/></svg>
                """

svg_home_white ="""
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <path fill="var(--ci-primary-color, currentColor)" d="M469.666,216.45,271.078,33.749a34,34,0,0,0-47.062.98L41.373,217.373,32,226.745V496H208V328h96V496H480V225.958ZM248.038,56.771c.282,0,.108.061-.013.18C247.9,56.832,247.756,56.771,248.038,56.771ZM448,464H336V328a32,32,0,0,0-32-32H208a32,32,0,0,0-32,32V464H64V240L248.038,57.356c.013-.012.014-.023.024-.035L448,240Z" class="ci-primary"/></svg>
                """

svg_add_white = """
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <path fill="var(--ci-primary-color, currentColor)" d="M48,464V144H16V472a24.027,24.027,0,0,0,24,24H368V464H48Z" class="ci-primary"/>
                    <path fill="var(--ci-primary-color, currentColor)" d="M144,400H112V80H80V408a24.027,24.027,0,0,0,24,24H432V400H144Z" class="ci-primary"/>
                    <path fill="var(--ci-primary-color, currentColor)" d="M472,16H168a24.027,24.027,0,0,0-24,24V344a24.027,24.027,0,0,0,24,24H472a24.027,24.027,0,0,0,24-24V40A24.027,24.027,0,0,0,472,16Zm-8,320H176V48H464Z" class="ci-primary"/>
                    <polygon fill="var(--ci-primary-color, currentColor)" points="304 288 336 288 336 204 420 204 420 172 336 172 336 88 304 88 304 172 220 172 220 204 304 204 304 288" class="ci-primary"/>
                    </svg>
                """

# ------------------------------------------------------------------------------
# 2 - Functions 
# ------------------------------------------------------------------------------
