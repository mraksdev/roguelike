import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet("tiles.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    event_handler = EventHandler()

    player = Entity(x=screen_width // 2, y=screen_height // 2, char="@", color=(255, 255, 255))
    npc = Entity(x=screen_width // 2 - 5, y=screen_height // 2, char="@", color=(255, 255, 0))
    entities = [player, npc]

    with tcod.context.new(
        columns=screen_width, 
        rows=screen_height, 
        tileset=tileset, 
        title = "Rogue Like", 
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()

            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            
            context.present(root_console)


            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player.move(action.dx, action.dy)

                if isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
