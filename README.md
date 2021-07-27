# esp
Description of Evan Style Python with examples.

My highschool art teacher used to say that drawing was like writing your
signature: If you do it long enough, not only do you get better,
but you get a style that's all your own. When I started coding in
Python, I did it like everyone else: One .py file, one class,
everything self-contained. I buried variables inside dicts of
dicts that even I couldn't decipher. I made tools for co-workers
that they never bothered using, because my code was unreadable.

Recently, I've done things differently. I take all my input
variables and all my data and put it in a .json file outside the
code. Values in these files are updated during runtime. The
principle advantages of decoupling files this way are thus:

1) At any step during runtime, the modified data can be saved
to .json as a snapshot. You can save and load executions and
configurations this way.

2) People who don't write Python can still interact with a text
file and still use your code for their purposes.

3) Data is restricted to what can be written as a .json dictionary,
so the program can interact with other object-oriented languages
more easily.

4) Dynamic variables and functions are more manageable in nested
dicts, but .json formatting ensures they are always readable.

There's no "one right way" to program, but the ESP
method will make your code more accessible. I've included
two examples of programming using this method.
Each folder contains an EspApp and its associated .json file.
The parent folder contains an example empty EspApp for
experimentation.

esp_resume_maker: Use a .json file as input to create a
formatted resume in MS Word.

esp_scrum_manager: See ESP resource management using a scrum
board management system. Print scrum boards in console or
on MS Excel.

future_third_project: tbd
