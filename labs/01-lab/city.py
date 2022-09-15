from safety.safety import draw_safety
from leisure.leisure import draw_leisure
from outdoors.outdoors import draw_outdoors
from education.education import draw_education
from infrastructure import road, power, tree
a=[[[""]for x in range (100)]for y in range(100)]
def draw_city(a):
    draw_safety(a)
    road.draw_road(a)
    power.draw_power_plant(a)
    road.draw_road(a)
    draw_leisure()
    road.draw_road(a)
    draw_outdoors(a)
    tree.draw_tree(a)
    road.draw_road(a)
    draw_education()
    return print(a)

draw_city(a)
