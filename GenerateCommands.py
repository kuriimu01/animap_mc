import os

# Function to generate mcfunction commands and save them into tick.mcfunction
def GenerateCommands(tick_path, total_frames):
    # Create directories if they do not exist
    directory = os.path.dirname(tick_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write commands to the tick.mcfunction file
    with open(tick_path, 'w') as file:
        for map_id in range(total_frames + 1):  
            z_coord = map_id

            file.write(f'setblock ~ ~-1 ~{z_coord} minecraft:packed_ice\n')
            file.write(f'setblock ~1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=east]\n')
            file.write(f'setblock ~-1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=west]\n')
            file.write(f'setblock ~-2 ~ ~{z_coord} minecraft:white_wool\n')
            file.write(f'setblock ~2 ~ ~{z_coord} minecraft:white_wool\n')
            file.write(f'setblock ~2 ~1 ~{z_coord} minecraft:white_wool\n')
            file.write(f'summon minecraft:item_frame ~1 ~1 ~{z_coord} {{Facing:4, Item:{{id:"minecraft:filled_map",Count:1b,tag:{{map:{map_id}}}}}}}\n')

    print(f"Commands generated and saved into {tick_path}. Now you can load it with /function animap:tick")
