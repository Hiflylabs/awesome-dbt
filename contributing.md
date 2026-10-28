# Contribution Guidelines

Thanks for helping keep Awesome dbt useful! This project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating you agree to its terms.

## Adding a resource

1. **It should be about dbt.** Tools need a real dbt integration; articles and courses need to be about working with dbt. Generic data tools without one don't fit.
2. **Pick the most specific section.** The list is organized by topic, not by format: a blog post about CI goes in *CI/CD*, a package that tests data goes in *Testing & Data Quality*. *Learning* is for general material, and *Packages* for general-purpose packages that don't belong to one topic.
3. **Add it at the top of that section.** The list is newest-first (LIFO), so fresh resources stay visible.
4. **Use the entry format:**

   ```md
   - [Name](https://link) - Description.
   ```

   - The description says what it does and why a dbt user would care, in one or two plain sentences.
   - Start with a capital letter, end with a period, and don't repeat the name.
5. **Say if you're affiliated.** If you build, sell or work on what you're adding, mention it in the pull request. That's welcome, we just want to know.

Prefer an issue? [Suggest a resource](https://github.com/Hiflylabs/awesome-dbt/issues/new?template=suggest-resource.yml) and a maintainer will add it.

## What the checks do

Every pull request runs:

| Check | What it verifies |
| --- | --- |
| **LIFO bot** | New entries are at the top of their section, aren't already listed, and follow the entry format. It comments on the pull request with what to fix. |
| **Awesome lint** | The [awesome-lint](https://github.com/sindresorhus/awesome-lint) rules. |
| **Links** | The links your pull request adds resolve. |

A weekly job checks every link in the list and keeps a single [`link-rot` issue](https://github.com/Hiflylabs/awesome-dbt/issues?q=label%3Alink-rot) up to date.

## What gets removed

- Dead links, unless a living copy or successor exists (then we link that instead).
- Archived or deprecated projects, replaced by their maintained successor when there is one.
- Resources that are no longer about dbt.

## Updating your pull request

If maintainers or the bot ask for changes, there's no need to open a new pull request: push to the same branch. If you're not sure how, [here is a guide](https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md) on the different ways to update a pull request.

Once a maintainer approves and the checks pass, your pull request merges automatically. Pushing after an approval needs a fresh one.
