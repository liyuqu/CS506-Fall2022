from .firestation import draw_firestation
from .hospital import draw_hospital
from .policestation import draw_policestation

def draw_safety(a):
    draw_firestation(a)
    draw_hospital(a)
    draw_policestation(a)
    return