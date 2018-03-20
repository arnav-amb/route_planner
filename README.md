# Tourist Helper

## Setting up your Development Environment ##
1. First, fork this repository to your account.

2. Create a virtual environment on your machine. 
    ```
    virtualenv -p python3 your_environment_name
    ```
    We recommend using python3-virtualenv. Any other packages would do fine though.

3. Activate the newly created virtual environment:
    ```
    cd your_environment_name
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/modihere/tourist_helper.git
    ```
    
5. Install the dependencies for the project.
    ```
    cd tourist_helper
    pip3 install -r requirements.txt
    ```

##Generate an API key and enable the Places,GeoCode and Directions API from the Google Developer Console.##

6. Migrate your database.
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate 
    ``` 

7. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    
    or 

    ```
    python3 manage.py runserver 8080
    ```
    or

    If you want to change the server’s IP, pass it along with the port. So to listen on all public IPs (useful if you want to show off your work on other computers on your network), use:

    ```
    python3 manage.py runserver 0.0.0.0:8000
    ```

    Once the server is started, open http://127.0.0.1:8000 or whatever server you are running on in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.

##You can see the output in the terminal as well to check the proper rendering of data on the webpage template.##
    
8. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/website.git
    ```
    
9. Find an issue in this repository that you would like to and can fix.
   Start working on an issue. Steps 9 and beyond will guide you in doing this.
   
10. Create a new branch and switch to it. (make sure you are on master before doing this).
    ```
    git branch mybranch
    git checkout mybranch
    ```
    'mybranch' can be replaced by your preferred name for the branch.
    The above to commands are equivalent to the following
    ```
    git checkout -b mybranch
    ```

11. Make your changes and then execute the tests to make sure you didn't break anything.

    ```
    python3 manage.py test
    ```
    Ensure that you follow [PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) style guide for python code while naming functions or classes.

    Then stage them and commit them.
    Check out Chris Beams's guide to writing good commit messages [here](https://chris.beams.io/posts/git-commit/).

    *A small description of your changes is must in the commit messages.* 

12. After you are done making changes, push the branch to your fork.
    ```
    git push -u myfork mybranch
    ```
    The **-u** option is required only the first time you push the branch.
	**In case you have made multiple commits, you need to squash them into a single commit before pushing.**
    Use
    ```
    git rebase -i HEAD~n
    ```
    `n` is the number of commits to rebase back to.
    You will be given some options such as pick, squash etc. with the commit in front of it, select the commit to squash by adding `squash` or s
    check here for more on [squashing and rebasing](https://www.devroom.io/2011/07/05/git-squash-your-latests-commits-into-one/)

13. Then create a Pull Request from that branch using GitHub.