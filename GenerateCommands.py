# Function to generate mcfunction commands. Then put them into tick.mcfunction
def generate_minecraft_commands(file_name, total_maps):
    with open(file_name, 'w') as file:
        for map_id in range(total_maps + 1):  
            z_coord = map_id
            
            file.write(f'setblock ~ ~-1 ~{z_coord} minecraft:packed_ice\n')
            file.write(f'setblock ~1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=east]\n')
            file.write(f'setblock ~-1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=west]\n')
            file.write(f'setblock ~-2 ~ ~{z_coord} minecraft:white_wool\n')
            file.write(f'setblock ~2 ~ ~{z_coord} minecraft:white_wool\n')
            file.write(f'setblock ~2 ~1 ~{z_coord} minecraft:white_wool\n')
            file.write(f'summon minecraft:item_frame ~1 ~1 ~{z_coord} {{Facing:4, Item:{{id:"minecraft:filled_map",Count:1b,tag:{{map:{map_id}}}}}}}\n')

    print(f"Commands generated and saved to {file_name}")

if __name__ == "__main__":
    # Second argument is your last frame id
    generate_minecraft_commands("minecraft_commands.txt", 1406)
