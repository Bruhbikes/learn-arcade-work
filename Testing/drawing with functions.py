import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_fish(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_ellipse_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_fish(on_draw.fish_x, 140)
    draw_fish(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.fish_x += 5


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.fish_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Fish animation")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
