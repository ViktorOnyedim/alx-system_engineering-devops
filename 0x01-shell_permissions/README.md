SHELL PERMISSIONS README

0-i_am_betty:
    This script switches the current user to the user betty.

1-who_am_i:
    This script prints the effective username of the current user.

2-groups:
    This script prints all the groups the current user is part of.

3-new_owner:
    This script changes the owner of the file "hello" to the user "betty"

4-empty:
    This script creates an empty file called hello.

5-execute:
    This script adds execute permission to the owner of the file "hello"

6-multiple_permissions:
    This script adds execute permission to the owner and the group owner, and read permission to other users, to the file "hello".

7-everybody:
    This script adds execution permission to the ownerk the group owner and the other users, to the file "hello".

8-James_Bond:
    This script sets the permission to the file "hello" (using Octal Notation) as follows:
        > Owner: no permission at all
        > Group: no permission at all
        > Other users: all the permissions
    With the file "hello" being in the working directory.

9-John_Doe:
    This script sets the mode of the file "hello" to:
        > -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
    With the file "hello" being in the working directory.

10-mirror_permissions:
    This script sets the mode of the file "hello" the same as 0lleh's mode.
    Both the file hello and olleh will be in the working directory
    NOTE: The script is dynamic in the sense that it works for any mode.

11-directories_permissions:
    This script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users (without changing regular files).

12-directory_permissions:
    This script creates a directory called my_dir with permissions 751 in the working directory

13-change_group:
    This script changes the group owner to school for the file "hello".

100-change_owner_and_group:
    This script changes the owner to "vincent" and the group owner to "staff" for all the files and directories in the working directory.

101-if_only:
    This script changes the owner of the file "hello" to "betty" only if it is owned by the user "guillaume".

102-Star_Wars:
    This script plays the StarWars IV episode in the terminal. 
