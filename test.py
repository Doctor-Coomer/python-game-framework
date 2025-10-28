import framework #import the framework

#constants
WIDTH = 550;
HEIGHT = 450;

game = framework.game_framework();

#creates a new window
game.spawn_window(width=WIDTH, height=HEIGHT, draw_stepping=True);

game.step_window();

print(game.get_font_names());
