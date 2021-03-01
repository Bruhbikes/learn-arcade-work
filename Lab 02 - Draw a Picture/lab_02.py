import arcade

arcade.open_window(800, 600, "drawing")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

arcade.draw_triangle_filled(400, 250, 400, 400, 350, 300, arcade.color.WHITE)

arcade.draw_triangle_filled(400, 250, 400, 400, 450, 300, arcade.color.WHITE)

arcade.draw_rectangle_filled(100, 600, 1400, 400, arcade.color.EMERALD)

arcade.draw_rectangle_filled(0, 50, 1600, 200, arcade.color.EMERALD)

arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()