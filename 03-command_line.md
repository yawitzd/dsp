# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > go home: cd ~
cat > file.txt ---- lets you write inside file
cat file.txt ----- displays contents of file
touch file.txt ---- creates this file
mkdir -----------  self explanatory
rm file.txt ------- self explanatory
rm folder/folder/file.txt
rm -rf folder ----------- clears the contents of this folder
cd ../.. -------------- go up 2 folders
pushd folder/folder ----- lets you jump to this place
popd folder/folder ------ lets you jump back
pwd ------------ PRINT WORKING DIRECTORY
ls ------------- look around


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls -a -------------- lists hidden files
ls -l ------------------ lists everything with details
ls -1 ------------------- lists everything in one column
ls -lh ----------------- lists 
ls -la ----------------- lists hidden files with details

---


---

What does `xargs` do? Give an example of how to use it.

> > excecute argument
lets you do something to a list of things
for example
ls ----- lists every file. say it's a list of folders
ls | xargs rmdir ------ deletes every empty directory in the folder


ls | xargs 

---

