# learntextvis.github.io

The Learn Text Vis Website


## Installation

To work on the site locally, you will need a few things.

First, we need to clone the site locally and navigate to its directory:

```
git clone git@github.com:learntextvis/learntextvis.github.io.git

cd learntextvis.github.io
```

This site is powered by [Jekyll](https://jekyllrb.com/), a popular ruby static site generator.

The ruby gem dependencies are managed by [Bundler](http://bundler.io/).

First, ensure `bundler` is installed:

```
gem install bundler
```

Now we can use the `bundle` command to install all the packages required for this site.

```
bundle install
```

This command will read the local `Gemfile` and download the required ruby gems.

## Running Locally

Assuming everything installs without issue, you should be able to start a local server to serve this site using:

```
make watch
```

The site should be accessible from [http://localhost:4000/](http://localhost:4000/).

Behind the scenes, this is really just running `jekyll`. It is equivalent to this command:

```
bundle exec jekyll serve
```

The Make command just makes it easier to remember.

## Modifying Content

Almost all the content for the site is in the `_posts` directory.

### Chapter Naming

Each "chapter" is its own markdown file. The naming convention follows the following convention:

```
YEAR-MONTH-DAY-cXX-NAME.md
```

The date in the name is a requirement of Jekyll - as it is traditionally used for blog posts. Here, we have used the same date for each chapter - so that the order is based on the `cXX` component of the name.

The `NAME` section is optional and provides some details on the contents of the chapter.

### Chapter Content

Chapters are written in Markdown. Each chapter file starts with a "preamble" that starts with and ends with three dashes - `---`. This is a Jekyll feature that allows us to add meta-data to our chapters. Currently, we are using `title` and `description` to provide content on the home page.

The markdown provides the ability to do code snippets and syntax highlighting. We just use the three backticks and append the language the snippet should be highlighted as:

> \`\`\`python

> \`\`\`

We can also use [gists](https://gist.github.com/) if the external hosting is desirable for some snippets.


### Other Pages

Right now, we just have one additional page besides the chapters. `index.md` controls the content for the home `index.html` page.

Other pages outside of chapter contents, like an 'about' page are easily created - when we need them.

### Layouts and Includes

The preamble also indicates the layout that the file will use. A layout is just a templating system. We currently have 2 layouts - one for posts and one for the main page. They are stored under `_layouts`.

A layout or a page can also include a fragment of html stored in `_includes`. Includes are used to ensure the header and footer are consistent between layouts. As more reusable snippets are identified, we can move them into `_includes`.

### Styling

The site uses [SASS](http://sass-lang.com/) for its styling. Each page, include, or layout can have its own `.scss` file in the `_sass` directory.

These files should be `@included` in `css/main.scss`. The Jekyll build system and `gh-pages` both support SASS for styling.

## Deployment

This site is considered a github [organization page](https://help.github.com/articles/user-organization-and-project-pages/).

As such, simply pushing local commits to the `master` branch of this repo on Github will republish the site with any changes. It might take a minute or two to see updates live.

The url for the site is currently: [http://learntextvis.github.io/](http://learntextvis.github.io/).

We will be able to have our own custom domain name as well - like learntextvis.com - in the future.
