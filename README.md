# quantumfit.github.io
Web page of the QuantumFIT research group at Faculty of Information Technology, Brno University of Technology

## Structure

Built with Jekyll, using the [academicpages](https://github.com/academicpages/academicpages.github.io) theme
pulled in at build time via `remote_theme:` in `_config.yml` (GitHub Pages fetches it automatically -- the
theme is not cloned/forked into this repo).

- `_pages/` -- site pages (About/home, People, Publications, News, Contact)
- `_data/team.yml` -- group members, shown on the People page
- `_publications/` -- one Markdown file per publication (see the
  [academicpages publication format](https://academicpages.github.io/markdown/) for front matter fields)
- `_posts/` -- one Markdown file per news item (`YYYY-MM-DD-title.md`), shown on the News page
- `_config.yml` -- site settings and theme configuration

## Enabling GitHub Pages

In the repo's Settings -> Pages, set the source to the `master` branch (root). The site then builds
automatically on every push and is served at https://quantumfit.github.io/.

## Local preview

```
bundle install
bundle exec jekyll serve
```

Requires Ruby matching GitHub Pages' legacy build environment (Ruby ~2.7). On a newer system Ruby
(3.4+/4.x), the bundled `github-pages` gem chain may fail with missing-stdlib errors (`csv`, `bigdecimal`,
`logger`, ...) or a `String#tainted?` error from an old `liquid` version -- both are local-environment
artifacts of running an old gem stack on a new Ruby, not real GitHub Pages build failures. Use a Ruby version
manager (e.g. `rbenv install 2.7.8`) for a faithful local preview, or just push and check the Pages build log.
