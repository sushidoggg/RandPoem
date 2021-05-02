# RandPoem
This is a program that rearrange the Chinese poems into a 3x3 grid. It can be used in games or activities like guessing the poem.

## How to use it?
Before executing the program
1. The program relys on the pygame module. Install it by ```pip install pygame```.
2. Make sure that the ```poem.txt``` file is not empty. In fact, it contains all possible poems that would appear in the program. Feel free to add some, but please follow the existing format.
   - Each line contains two sentences, each with a length of 5 Chinese characters.
   - Don't use commas nor spaces to separate the two sentences.
   - An example would be ```床前明月光疑是地上霜```.
3. If you failed to execute the program in your IDE, try to swicth your directory to the folder where the codes are at by ```cd 'C:/some/random/directory'```.
4. Make sure that all source files are in the same folder.

When using the program
1. Press SPACE to advance to the next poem.
2. Press any key to rearrange the same poem in another way.
3. All characters displayed are included in two continuous sentences of a poem. Since the 3x3 grid has only 9 positions, only one of the sentences is complete. Your goal is to find this complete sentence without being distracted by the other.

## Any customized inputs?
- Background picture
- List of poems
- Fonts
- Colors
- ...

Those features can be customized by changing the source files and the codes by replacing filenames.