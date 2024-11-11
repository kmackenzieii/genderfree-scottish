# Contributing
## Adding content to the site (through github web interface)
### 1. Log in to github
To commit changes to the website you need a [github account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

### 2. Visit the repository
Go to the [repository site](https://github.com/kmackenzieii/genderfree-scottish) and navigate to where you want to add/edit content. 


### 3. Add/edit content
Events go in `src/events`, individual pages (like about or faq) go in `src/pages`. 

Click the `Add file` button. You can choose to create a new file entirely within the web interface or upload a file you've already edited on your computer. 

Alternatively, you can open a file that already exists and edit the content directly. 

#### Pages
Pages automatically get their own page with a link added to the menu. This link will be labeled with the Page title. 

A page must have a specific header and can have arbitrary Markdown or HTML content. The filename should end in `.md`. Here is an example of a page

```
Title: Example

This is some example content

You can use *Markdown* styling.

Or write <b>HTML</b> instead. As well as mix the two.

```

#### Events
Time-based events go in `src/events`. Each events gets its own Markdown (`*.md`) file. 

The events will automatically get their own page, and also get added to the Events page linked to from the nav-bar. The event with the nearest date is also added to the site's landing page when publishing the site. 

Event files must have some header content followed by arbitrary content, which should ideally include things like timing, teachers, musicians, covid protocols, etc...

The header must include `Date` and `Title`. See the example:
```
Title: GenderFree SCD
Date: 2024-11-7 19:00:00

Teaching by Kat Dutton to recorded music

- 7:00 -- 7:30 - Advanced SCD
- 7:30 -- 8:00 - Dance lesson for all
- 8:00 -- 9:00 - Social dance for all

**COVID PROTOCOLS**: Because wastewater data is showing levels below 500 copies/mL, we will be *MASK RECOMMENDED* for this dance. If possible, please bring and wear a well-fitting high-filtration mask over your nose and mouth. Masking will not be required to participate and there may be dancers present who are unmasked.
```

## Adding content to the site (without github web interface)
### 1. Install Dependencies
To commit changes to the website, you need [git](https://git-scm.com/) and a [github account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

A text editor, like [VSCod(e|ium)](https://vscodium.com/#install), but notepad or any plain-text editor will do. 

### 2. Checkout this repository
Using git, clone the repository. Command line example below, but your editor may be able to provide a graphical interface.
```
git clone git@github.com:kmackenzieii/genderfree-scottish.git
```

Note: Github has started enforcing 2FA and connecting with SSH. For instructions on generating and using ssh keys, see [this guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh). This is a one-time setup process, unless you change development computers.

If you're coming back after some time, someone else may have updated the website. To sync your local copy with the current version, you need to run:
```
git fetch
```
to find out if there are any updates. Followed by
```
git pull
```
To pull those updates into your local copy.

### 3. Add/edit content
Website content is located in `src`. Events, like individual dance classes go in `src/events`. Static pages like `About` and `FAQ` go in `src/pages`. 

See [above](#3-addedit-content)

### 4. Commit Changes
You've made some changes or added new content. Now you need to commit your changes to the local copy of your repository and then push those changes to the remote (GitHub) repository.

To to list the names of files that you modified or created, run:
```
git status
```

For each file you want to add to your commit run:
```
git add <filename>
```

Commit the files with a message to your local repository:
```
git commit -m "Your message here"
```

Push your changes to the remote repository **This will republish the REAL, LIVE website!**:
```
git push
```

## Building the website
You do not need to build the website to contribute to it. But you may wish to check that your content builds correctly before you commit it. To do that you will need some extra things. 

### Install dependencies
To build the site, you need the following software:
 - git
 - python3
 - python3-venv
 - pip

On a debian-based Linux distro, like Ubuntu or Mint, run:
```
sudo apt install git python3 python3-venv pip
```

### Check out this repository
See above.

### Create a Python virtual environment
This keeps the Python packages for deelopment separate from the rest of your system.

From your repository directory, run:
```
python3 -m venv .venv
```

You only need to do this once.

### Load the virtual environment
Do this every time. 

From your repository root directory. Run:
```
source .venv/bin/activate
```

Your virtual environment is now active, you need to install the website's build dependencies into it.

Run:
```
pip install -r requirements.txt
```

### Build the site
```
make html
```

### Start a local server
TO view your site in your browser

```
make serve
```

Then navigate to [http://localhost:8000](http://localhost:8000)

*Congrats!* You are viewing a new (local) copy of the site. 
