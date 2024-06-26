## Create a new repository on the command line

echo "# Demo-Project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fabricefadegnon/Demo-Project.git
git push -u origin main

## Push an existing repository from th command line

git remote add origin https://github.com/fabricefadegnon/Demo-Project.git
git branch -M main
git push -u origin main

## Git Commands line
# GIT COMMANDS
# We divide Git into high level ("porcelain") commands and low level ("plumbing") commands.

High-level commands (porcelain)
We separate the porcelain commands into the main commands and some ancillary user utilities.
# Main porcelain commands
git-add[1]
Add file contents to the index

git-am[1]
Apply a series of patches from a mailbox

git-archive[1]
Create an archive of files from a named tree

git-bisect[1]
Use binary search to find the commit that introduced a bug

git-branch[1]
List, create, or delete branches

git-bundle[1]
Move objects and refs by archive

git-checkout[1]
Switch branches or restore working tree files

git-cherry-pick[1]
Apply the changes introduced by some existing commits

git-citool[1]
Graphical alternative to git-commit

git-clean[1]
Remove untracked files from the working tree

git-clone[1]
Clone a repository into a new directory

git-commit[1]
Record changes to the repository

git-describe[1]
Give an object a human readable name based on an available ref

git-diff[1]
Show changes between commits, commit and working tree, etc

git-fetch[1]
Download objects and refs from another repository

git-format-patch[1]
Prepare patches for e-mail submission

git-gc[1]
Cleanup unnecessary files and optimize the local repository

git-grep[1]
Print lines matching a pattern

git-gui[1]
A portable graphical interface to Git

git-init[1]
Create an empty Git repository or reinitialize an existing one

git-log[1]
Show commit logs

git-maintenance[1]
Run tasks to optimize Git repository data

git-merge[1]
Join two or more development histories together

git-mv[1]
Move or rename a file, a directory, or a symlink

git-notes[1]
Add or inspect object notes

git-pull[1]
Fetch from and integrate with another repository or a local branch

git-push[1]
Update remote refs along with associated objects

git-range-diff[1]
Compare two commit ranges (e.g. two versions of a branch)

git-rebase[1]
Reapply commits on top of another base tip

git-reset[1]
Reset current HEAD to the specified state

git-restore[1]
Restore working tree files

git-revert[1]
Revert some existing commits

git-rm[1]
Remove files from the working tree and from the index

git-shortlog[1]
Summarize git log output

git-show[1]
Show various types of objects

git-sparse-checkout[1]
Reduce your working tree to a subset of tracked files

git-stash[1]
Stash the changes in a dirty working directory away

git-status[1]
Show the working tree status

git-submodule[1]
Initialize, update or inspect submodules

git-switch[1]
Switch branches

git-tag[1]
Create, list, delete or verify a tag object signed with GPG

git-worktree[1]
Manage multiple working trees

gitk[1]
The Git repository browser

scalar[1]
A tool for managing large Git repositories

Ancillary Commands
Manipulators:

git-config[1]
Get and set repository or global options

git-fast-export[1]
Git data exporter

git-fast-import[1]
Backend for fast Git data importers

git-filter-branch[1]
Rewrite branches

git-mergetool[1]
Run merge conflict resolution tools to resolve merge conflicts

git-pack-refs[1]
Pack heads and tags for efficient repository access

git-prune[1]
Prune all unreachable objects from the object database

git-reflog[1]
Manage reflog information

git-remote[1]
Manage set of tracked repositories

git-repack[1]
Pack unpacked objects in a repository

git-replace[1]
Create, list, delete refs to replace objects

Interrogators:

git-annotate[1]
Annotate file lines with commit information

git-blame[1]
Show what revision and author last modified each line of a file

git-bugreport[1]
Collect information for user to file a bug report

git-count-objects[1]
Count unpacked number of objects and their disk consumption

git-diagnose[1]
Generate a zip archive of diagnostic information

git-difftool[1]
Show changes using common diff tools

git-fsck[1]
Verifies the connectivity and validity of the objects in the database

git-help[1]
Display help information about Git

git-instaweb[1]
Instantly browse your working repository in gitweb

git-merge-tree[1]
Perform merge without touching index or working tree

git-rerere[1]
Reuse recorded resolution of conflicted merges

git-show-branch[1]
Show branches and their commits

git-verify-commit[1]
Check the GPG signature of commits

git-verify-tag[1]
Check the GPG signature of tags

git-version[1]
Display version information about Git

git-whatchanged[1]
Show logs with differences each commit introduces

gitweb[1]
Git web interface (web frontend to Git repositories)

Interacting with Others
These commands are to interact with foreign SCM and with other people via patch over e-mail.

git-archimport[1]
Import a GNU Arch repository into Git

git-cvsexportcommit[1]
Export a single commit to a CVS checkout

git-cvsimport[1]
Salvage your data out of another SCM people love to hate

git-cvsserver[1]
A CVS server emulator for Git

git-imap-send[1]
Send a collection of patches from stdin to an IMAP folder

git-p4[1]
Import from and submit to Perforce repositories

git-quiltimport[1]
Applies a quilt patchset onto the current branch

git-request-pull[1]
Generates a summary of pending changes

git-send-email[1]
Send a collection of patches as emails

git-svn[1]
Bidirectional operation between a Subversion repository and Git

Reset, restore and revert
There are three commands with similar names: git reset, git restore and git revert.

git-revert[1] is about making a new commit that reverts the changes made by other commits.

git-restore[1] is about restoring files in the working tree from either the index or another commit. This command does not update your branch. The command can also be used to restore files in the index from another commit.

git-reset[1] is about updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history.

git reset can also be used to restore the index, overlapping with git restore.

# Low-level commands (plumbing)
Although Git includes its own porcelain layer, its low-level commands are sufficient to support development of alternative porcelains. Developers of such porcelains might start by reading about git-update-index[1] and git-read-tree[1].

The interface (input, output, set of options and the semantics) to these low-level commands are meant to be a lot more stable than Porcelain level commands, because these commands are primarily for scripted use. The interface to Porcelain commands on the other hand are subject to change in order to improve the end user experience.

The following description divides the low-level commands into commands that manipulate objects (in the repository, index, and working tree), commands that interrogate and compare objects, and commands that move objects and references between repositories.

# Manipulation commands
git-apply[1]
Apply a patch to files and/or to the index

git-checkout-index[1]
Copy files from the index to the working tree

git-commit-graph[1]
Write and verify Git commit-graph files

git-commit-tree[1]
Create a new commit object

git-hash-object[1]
Compute object ID and optionally create an object from a file

git-index-pack[1]
Build pack index file for an existing packed archive

git-merge-file[1]
Run a three-way file merge

git-merge-index[1]
Run a merge for files needing merging

git-mktag[1]
Creates a tag object with extra validation

git-mktree[1]
Build a tree-object from ls-tree formatted text

git-multi-pack-index[1]
Write and verify multi-pack-indexes

git-pack-objects[1]
Create a packed archive of objects

git-prune-packed[1]
Remove extra objects that are already in pack files

git-read-tree[1]
Reads tree information into the index

git-replay[1]
EXPERIMENTAL: Replay commits on a new base, works with bare repos too

git-symbolic-ref[1]
Read, modify and delete symbolic refs

git-unpack-objects[1]
Unpack objects from a packed archive

git-update-index[1]
Register file contents in the working tree to the index

git-update-ref[1]
Update the object name stored in a ref safely

git-write-tree[1]
Create a tree object from the current index

# Interrogation commands
git-cat-file[1]
Provide contents or details of repository objects

git-cherry[1]
Find commits yet to be applied to upstream

git-diff-files[1]
Compares files in the working tree and the index

git-diff-index[1]
Compare a tree to the working tree or index

git-diff-tree[1]
Compares the content and mode of blobs found via two tree objects

git-for-each-ref[1]
Output information on each ref

git-for-each-repo[1]
Run a Git command on a list of repositories

git-get-tar-commit-id[1]
Extract commit ID from an archive created using git-archive

git-ls-files[1]
Show information about files in the index and the working tree

git-ls-remote[1]
List references in a remote repository

git-ls-tree[1]
List the contents of a tree object

git-merge-base[1]
Find as good common ancestors as possible for a merge

git-name-rev[1]
Find symbolic names for given revs

git-pack-redundant[1]
Find redundant pack files

git-rev-list[1]
Lists commit objects in reverse chronological order

git-rev-parse[1]
Pick out and massage parameters

git-show-index[1]
Show packed archive index

git-show-ref[1]
List references in a local repository

git-unpack-file[1]
Creates a temporary file with a blob’s contents

git-var[1]
Show a Git logical variable

git-verify-pack[1]
Validate packed Git archive files

In general, the interrogate commands do not touch the files in the working tree.

Syncing repositories
git-daemon[1]
A really simple server for Git repositories

git-fetch-pack[1]
Receive missing objects from another repository

git-http-backend[1]
Server side implementation of Git over HTTP

git-send-pack[1]
Push objects over Git protocol to another repository

git-update-server-info[1]
Update auxiliary info file to help dumb servers

The following are helper commands used by the above; end users typically do not use them directly.

git-http-fetch[1]
Download from a remote Git repository via HTTP

git-http-push[1]
Push objects over HTTP/DAV to another repository

git-receive-pack[1]
Receive what is pushed into the repository

git-shell[1]
Restricted login shell for Git-only SSH access

git-upload-archive[1]
Send archive back to git-archive

git-upload-pack[1]
Send objects packed back to git-fetch-pack

# Internal helper commands
These are internal helper commands used by other commands; end users typically do not use them directly.

git-check-attr[1]
Display gitattributes information

git-check-ignore[1]
Debug gitignore / exclude files

git-check-mailmap[1]
Show canonical names and email addresses of contacts

git-check-ref-format[1]
Ensures that a reference name is well formed

git-column[1]
Display data in columns

git-credential[1]
Retrieve and store user credentials

git-credential-cache[1]
Helper to temporarily store passwords in memory

git-credential-store[1]
Helper to store credentials on disk

git-fmt-merge-msg[1]
Produce a merge commit message

git-hook[1]
Run git hooks

git-interpret-trailers[1]
Add or parse structured information in commit messages

git-mailinfo[1]
Extracts patch and authorship from a single e-mail message

git-mailsplit[1]
Simple UNIX mbox splitter program

git-merge-one-file[1]
The standard helper program to use with git-merge-index

git-patch-id[1]
Compute unique ID for a patch

git-sh-i18n[1]
Git’s i18n setup code for shell scripts

git-sh-setup[1]
Common Git shell script setup code

git-stripspace[1]
Remove unnecessary whitespace

Guides
The following documentation pages are guides about Git concepts.

gitcore-tutorial[7]
A Git core tutorial for developers

gitcredentials[7] 
Providing usernames and passwords to Git

gitcvs-migration[7]
Git for CVS users

gitdiffcore[7]
Tweaking diff output

giteveryday[7]
A useful minimum set of commands for Everyday Git

gitfaq[7]
Frequently asked questions about using Git

gitglossary[7]
A Git Glossary

gitnamespaces[7]
Git namespaces

gitremote-helpers[7]
Helper programs to interact with remote repositories

gitsubmodules[7]
Mounting one repository inside another

gittutorial[7]
A tutorial introduction to Git

gittutorial-2[7]
A tutorial introduction to Git: part two

gitworkflows[7]
An overview of recommended workflows with Git

Repository, command and file interfaces
This documentation discusses repository and command interfaces which users are expected to interact with directly. See --user-formats in git-help[1] for more details on the criteria.

gitattributes[5]
Defining attributes per path

gitcli[7]
Git command-line interface and conventions

githooks[5]
Hooks used by Git

gitignore[5]
Specifies intentionally untracked files to ignore

gitmailmap[5]
Map author/committer names and/or E-Mail addresses

gitmodules[5]
Defining submodule properties

gitrepository-layout[5]
Git Repository Layout

gitrevisions[7]
Specifying revisions and ranges for Git

File formats, protocols and other developer interfaces
This documentation discusses file formats, over-the-wire protocols and other git developer interfaces. See --developer-interfaces in git-help[1].

gitformat-bundle[5]
The bundle file format

gitformat-chunk[5]
Chunk-based file formats

gitformat-commit-graph[5]
Git commit-graph format

gitformat-index[5]
Git index format

gitformat-pack[5]
Git pack format

gitformat-signature[5]
Git cryptographic signature formats

gitprotocol-capabilities[5]
Protocol v0 and v1 capabilities

gitprotocol-common[5]
Things common to various protocols

gitprotocol-http[5]
Git HTTP-based protocols

gitprotocol-pack[5]
How packs are transferred over-the-wire

gitprotocol-v2[5]
Git Wire Protocol, Version 2

# Configuration Mechanism
Git uses a simple text format to store customizations that are per repository and are per user. Such a configuration file may look like this:

# A '#' or ';' character indicates a comment.
#

; core variables
[core]
	; Don't trust file modes
	filemode = false

; user identity
[user]
	name = "Junio C Hamano"
	email = "gitster@pobox.com"
Various commands read from the configuration file and adjust their operation accordingly. See git-config[1] for a list and more details about the configuration mechanism.

Identifier Terminology
<object>
Indicates the object name for any type of object.

<blob>
Indicates a blob object name.

<tree>
Indicates a tree object name.

<commit>
Indicates a commit object name.

<tree-ish>
Indicates a tree, commit or tag object name. A command that takes a <tree-ish> argument ultimately wants to operate on a <tree> object but automatically dereferences <commit> and <tag> objects that point at a <tree>.

<commit-ish>
Indicates a commit or tag object name. A command that takes a <commit-ish> argument ultimately wants to operate on a <commit> object but automatically dereferences <tag> objects that point at a <commit>.

<type>
Indicates that an object type is required. Currently one of: blob, tree, commit, or tag.

<file>
Indicates a filename - almost always relative to the root of the tree structure GIT_INDEX_FILE describes.

Symbolic Identifiers
Any Git command accepting any <object> can also use the following symbolic notation:

HEAD
indicates the head of the current branch.

<tag>
a valid tag name (i.e. a refs/tags/<tag> reference).

<head>
 a valid head name (i.e. a refs/heads/<head> reference).
