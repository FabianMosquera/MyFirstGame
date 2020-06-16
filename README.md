## Game RPG in Python

# General
For this challenge, you will be in charge of modeling a Hero/Heroine for a roleplaying game using an object- oriented programming design. 
You will be given some general rules for the structure of the model, but you are free to add any extra features, and decide the best approach for any specifics. 

# Requeriments
* Base Champion: 
-Our champion has some general attributes : 
• Name: Can be any combination of 10 Unicode characters 
• Race: Human, Elf, Dwarf, Hobbit, Orc (Only 1) 
• Gender: Male, Female, Other (Only 1) 
• Level: Starts at 0 and can go up to 100 
• EXP for Next Level: The amount of experience needed to reach the next level. 
• Current EXP: The amount of EXP our hero has in the current level. 
• Total EXP: The amount of EXP our hero/heroine has in total from all levels. (Positive) 
• Stats: Health, Attack, Defense, Magic, Speed (All of them) These stats range from 0 to 100 
• Stat-points: A certain number of points that can be used to increase any stat of our character. (Positive) 
-Our champion has some general actions: 
• Level Up: After certain amount of EXP, our character levels up, increasing his/her level value and gains 3 stat points. Current EXP is reset to 0, EXP for next level is set, and Total EXP is increased. 
• Gain EXP: Increases the champion Current EXP 
• Death: If our character dies, he/she loses 50% of the Current EXP. 
• Save character: Must save all the relevant champion information to a JSON file. 
• Load character: Reads all relevant champion information from a JSON file. 
• Increase Stats: Uses a dictionary to update stats based off the amount of stat points the champion currently has 
* Champion Class: 
Our hero/heroine, can be any of 6 different classes, Cleric, Fighter, Mage, Paladin, Ranger, or Rogue. 
You are expected to design the model for at least 3 different classes. 
-General attributes for the class: 
• Initial Stats: The values which our champion takes at the beginning of the adventure. (Will be different depending on the chosen class) 
• Attack Weapon: The attack weapon depending on the class chosen, such as a bow and arrow, sword, staff, hammer, or blades. 
• Defense Equipment: Can be a shield or no shield. 
• Armor: A list of armor equipment that encompasses [Helmet, Gauntlets, Chest armor, Leg armor] This armor must contribute (positively or negatively) to the defense and speed stats of the hero/heroine. 
-General methods for the class: 
• Attack: Performs the corresponding action using the attack/speed stat of the champion and his/her attack weapon. 
• Defend: Performs the corresponding action using the defense stat of the champion and his/her Defense equipment if any. 
• Use Magic: Uses a special Magic attack based off the magic stat of the champion. 
* Subclasses: 
Besides the main class of our champion, we also have 3 different subclasses, Solar, Arc, and Void. 
You are expected to model at least 1 Sub-class. 
-General attributes for the Sub-class: 
• Type: Solar, Arc, or Void (Only 1) 
• Sub-class Stats: Power, Elemental Affinity (All of them) Power is a stat that determines base damage Affinity affects power by a certain percentage depending on the following: 
Sub-Class No Change 
Against (+ 0 %) 
Weak Against (-25%) 
Strong Against (+25%) Solar Solar Void Arc Arc Arc Solar Void Void Void Arc Solar 
-General methods for the Sub-class: 
• Sub-class skill: Uses a special Sub-class skill with an efficacy based off the sub class stats. This method must know the element of an enemy.

## Authors
* **Alejandro Rusca** - [dondropo](https://github.com/dondropo)
* **Juan Gómez** - []()
* **Jose Omar** - []()
* **Santiago Peña** - []()
* **Ricky Mosquera** - [FabianMosquera](https://github.com/FabianMosquera)