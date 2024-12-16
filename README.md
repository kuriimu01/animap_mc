
--- 
<!-- ABOUT THE PROJECT -->
## About The Project (outdated readme)



https://github.com/user-attachments/assets/0b6b3cbc-865a-4baa-acd4-40328ecaf648


This tool is designed to automate the placement of map arts in Minecraft, specifically for creating stunning zoetrope effects. Leveraging Minecraft's powerful command system, this tool streamlines the process of arranging map art in a precise grid format, ensuring perfect alignment and timing for an immersive visual experience.



--- 

<!-- GETTING STARTED -->
## Getting Started

This tool offers **two methods** for placing map arts automatically in Minecraft for a zoetrope: **manual placement** and **automated command generation**. 

In the **manual placement method**, users can leverage a Python script utilizing **PyAutoGUI** to send commands directly into the Minecraft chat, allowing for quick and efficient placement of map frames. 
Alternatively, the **automated command generation method** produces a text file containing all necessary commands designed to be inserted into an MCFunction file within a datapack, allowing users to execute these commands instantly in the game. This approach ensures precise control over the positioning of each map art, providing a seamless experience for placing multiple frames at once. Both methods offer **flexibility** to accommodate different user preferences and workflows.

--- 
### Installation
**Automated placement method**
1. Clone the repository
   ```sh
   git clone https://github.com/github_username/animap_mc.git
   ```


**Manual placement method (slow)**
1. Clone the repository
   ```sh
   git clone https://github.com/github_username/animap_mc.git
   ```

2. Install requirements.txt
   ```sh
    pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


--- 

<!-- USAGE EXAMPLES -->
## Usage Examples


**Automated placement method**

In contrast, this method is much faster. By generating a text file with all necessary commands, users can execute them all at once within the Minecraft environment. This allows for rapid placement of blocks and item frames, making it ideal for large-scale projects like creating a zoetrope. 
While this method is faster, it does require a datapack installation to function correctly. Users need to create or modify a datapack to include the generated MCFunction file. This step may be less appealing for some users, especially those who are not familiar with Minecrafts datapack system, but it provides a more efficient means of executing multiple commands at once.

#### Steps to Use the Automated Placement Method

1. **Launch Minecraft** and load the world where you want to place your map arts.
   
2. **Enable Cheats**. Make sure that cheats are enabled in your world settings. To do this, navigate to the **World Settings** menu and toggle the cheats option.

3. **Prepare Your Map Art Data**. Place your converted map art frames (in the format **map_id.data**) into the **data** folder of your Minecraft world. You can use [this tool](https://rebane2001.com/mapartcraft/ "this tool") to convert your images into data files (maximum image size is **128px x 128px**). The path to the folder should look like this:
   ```sh
   .minecraft\saves\Your World\data
   ```

4. **Run the Command Generation Script**. Locate and execute the **GenerateCommands.py** file using your Python environment. Ensure you have Python installed. You can run the script using the following command:
   ```sh
   python GenerateCommands.py
   ```

5. **Copy the Generated Commands**. Once the script has finished running, open the generated file **minecraft_commands.txt**. Copy the commands from this file and paste them into the **tick.mcfunction** file located at:
   ```sh
   .minecraft\saves\Your World\data\animap\functions\tick.mcfunction
   ```

6. **Reload Your World**. In your Minecraft world, execute the `/reload` command in the chat or press **F3 + T** to reload the datapack.

7. **Execute the Function**. Finally, run the command `/function animap:tick` in the chat to place your map arts automatically. Your zoetrope is now ready!

---


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Telegram - [@kuriimu01](https://t.me/kuriimu01 "@kuriimu01")

Project Link: [https://github.com/kuriimu01/animap_mc](https://github.com/kuriimu01/animap_mc)



