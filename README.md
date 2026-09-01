# quantumfit.github.io
Web page of QuantumFIT, the Quantum Computing Systems research group at Faculty of Information Technology, Brno University of Technology

## Structure

Built with Jekyll. The theme is **vendored into this repo** -- `_sass/`, `_includes/`, `_layouts/` and
`assets/` were copied from [liuyxpp/liuyxpp.github.io](https://github.com/liuyxpp/liuyxpp.github.io)
at commit `8d46aef`, which `remote_theme:` used to be pinned to. There is no `remote_theme:` any more;
those directories are ours to edit.

It was vendored to make site-wide dark mode possible: the theme's palette is Sass variables, which are
compile-time, while runtime theme switching needs CSS custom properties -- and `lighten()`/`darken()`/`mix()`
hard-error when handed a `var()`. Roughly 140 such calls sit inside theme partials, which had to become
editable. Theme partials the site does not use (`_syntax`, `_gist`, `_dl-menu`, `_publication`, `_bloghome`,
`_sidebar`) have been removed.

`_layouts/home.html` was already adapted before vendoring: upstream hardcodes its own group's branding
and links in that layout rather than in config/data.

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

Now that the theme is vendored, `jekyll-remote-theme` is no longer needed and a modern Jekyll can build
the site directly. Do **not** use `bundle exec`: the `Gemfile` pins the legacy `github-pages` gem chain,
which fails on a current system Ruby (missing `csv`/`bigdecimal`/`logger`, or `String#tainted?` from an
old `liquid`). Run Jekyll from a directory that has no `Gemfile` so it does not try to bundle-load:

```
cd "$(mktemp -d)"
jekyll serve --source /path/to/quantumfit.github.io
```

`site.url` is the production URL, so page assets are absolute and a plain local build still pulls CSS
from the live site. For a genuinely local preview, overlay the URL:

```
printf 'url: "http://localhost:8899"\n' > /tmp/local.yml
cd "$(mktemp -d)"
jekyll build --source /path/to/quantumfit.github.io \
  --config /path/to/quantumfit.github.io/_config.yml,/tmp/local.yml \
  --destination ./_localsite
(cd _localsite && python3 -m http.server 8899)
```

Sass emits deprecation warnings (`@import`, `lighten()`, `$a/$b`) under dart-sass but compiles without
errors. To iterate on colours alone, skip Jekyll entirely -- strip the front matter from
`assets/css/main.scss` and run `sass --load-path=_sass`.

The `Gemfile` is kept only because GitHub Pages' own build reads it.
