virtual environments is used to create a logical partition.
it helps to create different unique environments for each project.

**use case**

1. Create a virtual environment

```bash
pip install virtualenv
```
2. Start a new project that uses the virtual environment 

```bash
python -m venv project-gab
```

3. Start another project

```bash
python -m venv project-tetris-gab
```
4. Work on a project using its own unique virtualenv.

```bash 
source project-gab/bin/activate
```
you can install any package on this isolated environment that can not be accessible on `project-tetris-gab`

for example: if you install 
```bash
pip install jira
```
it will only be installed for use in the `project-gab` virtualenv. this Will help to avoid any form of conflicts in each projects packages

5. Check which package you have installed 

```bash
pip list
```

6. Exiting the virtualenv

```bash
deactivate 
```




