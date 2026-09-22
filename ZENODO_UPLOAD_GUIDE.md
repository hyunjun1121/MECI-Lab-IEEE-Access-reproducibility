# GitHub and Zenodo Upload Guide

## Before publishing

1. Confirm the author order, biographies, conflict-of-interest statement, and
   the final public data-access URL.
2. Choose a code/data license in consultation with the authors and institution.
3. Add the assigned Zenodo DOI to `main.tex` and rebuild `main.pdf` before the
   final release.

## GitHub

Create a repository from this directory, then commit the prepared package:

```powershell
cd C:\project\MECI-Lab-zenodo
git init
git add .
git commit -m "Prepare reproducibility archive for IEEE Access manuscript"
git branch -M main
git remote add origin https://github.com/<account>/<repository>.git
git push -u origin main
```

Create a version tag after the manuscript and metadata are final:

```powershell
git tag -a v1.0.1 -m "Update manuscript data availability DOI"
git push origin v1.0.1
```

## Zenodo

The sanitized GitHub repository is public and can be enabled in Zenodo's GitHub
integration for automatic release archiving.

1. Sign in to Zenodo with the GitHub account that owns the repository.
2. Open **GitHub** settings and enable the repository.
3. Create a GitHub release for `v1.0.1`, or let Zenodo archive that release.
4. Check the generated record metadata, author order, affiliation, keywords,
   funding information, and license.
5. Publish the Zenodo record and copy its version DOI.
6. Keep the DOI and public URL synchronized with the manuscript Data
   Availability statement.

Do not upload raw YouTube media, raw private Analytics responses, OAuth files,
cookies, access tokens, model weights, runtime caches, or local virtual
environments.
