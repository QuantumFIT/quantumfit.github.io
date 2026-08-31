# quantumfit.github.io
Web page of QuantumFIT, the Quantum Computing Systems research group at Faculty of Information Technology, Brno University of Technology

## Structure

Built with Jekyll, using the theme from [liuyxpp/liuyxpp.github.io](https://github.com/liuyxpp/liuyxpp.github.io)
pulled in at build time via `remote_theme:` in `_config.yml`, pinned to a fixed commit. GitHub Pages fetches
it automatically -- the theme is not cloned/forked into this repo.

`_layouts/home.html` is a local override of the theme's homepage layout: upstream hardcodes its own group's
branding and links directly in that layout file (not in config/data), so it had to be copied and adapted here
rather than left untouched. Every other theme file (includes, sass, assets) is pulled unmodified.

- `pages/` -- site pages (Group, Publications, News, About), plus `index.html` for the home page
- `_data/group.yml` -- group members, shown on the Group page (placeholder entries)
- `_data/news.yml` -- news items, shown on the home page and the News page
- `_data/positions.yml` -- contact/affiliation info, shown on the About page
- `_data/navigation.yml`, `authors.yml`, `language.yml`, `share.yml`, `tags.yml` -- theme configuration data
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
