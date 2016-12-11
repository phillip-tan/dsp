# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
pwd print working directory
mkdir make directory
cd change directory
rmdir remove directory
pushd push directory
popd pop directory
cp copy a file or directory
mv move a file or directory
less page through a file
cat print the whole file
xargs execute arguments
find find files
grep find things inside files
man read a manual page
env look at your environment
echo print some arguments
export export/set a new environment variable
sudo become super user

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah` 
`ls -t`  
`ls -Glp`  
> > 
`ls`  list directory.
`ls -a`  displays all files.
`ls -l`  displays the long format listing.
`ls -lh`  list files that show sizes in human readable format.
`ls -lah`  list all files that show sizes in human readable format.
`ls -t`  displays newest files first. (based on timestamp)
`ls -Glp`  inhibits display of group information and uses long listing format to append indicator to entries.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
'ls -r' displays files in reverse order.
'ls -m' displays the names as a comma-separated list.
'ls -u' displays files by the file access time.
'ls -d' displays only directories.
'ls -1' displays each entry on a line.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' executes arguments. More specifically, it executes the same command on a bunch of items in order. For example, I can sequence a list of numbers while simultaneously listing out each one as an individual entry next to a specific word. It would look something like 
'seq 10 | xargs -n 1 echo "Hello". 'xargs' allows me, entirely at the command line, perform the same command a bunch of times in order. 

 

