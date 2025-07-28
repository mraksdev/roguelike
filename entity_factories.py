from entity import Entity

player = Entity( x=0, y=0, char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Entity( x=1, y=1, char="o", color=(63, 127, 63), name="Orc", blocks_movement=True)
troll = Entity( x=2, y=2, char="T", color=(0, 127, 0), name="Troll", blocks_movement=True)