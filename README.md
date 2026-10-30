<!--lint disable awesome-heading-->
# Awesome dbt [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme) <img alt="GitHub stars" src="https://img.shields.io/github/stars/Hiflylabs/awesome-dbt"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Hiflylabs/awesome-dbt"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Hiflylabs/awesome-dbt">

[<img src="dbt-logo.png" align="right" width="200">](https://www.getdbt.com/)

A curated list of the best dbt resources: courses and guides, tools and packages, and the community around them. Maintained by [Hiflylabs](https://hiflylabs.com/) since 2021, with the help of 60+ contributors.

**Contributions are welcome!** Add your resource **at the top** of the most specific section (the list is newest-first), as `- [Name](https://link) - Description.` See the [contribution guidelines](contributing.md); a bot checks placement and format on every pull request.

## Contents

- [Learning](#learning)
  - [Courses](#courses)
  - [Tutorials & Cheat Sheets](#tutorials--cheat-sheets)
  - [Best Practices](#best-practices)
  - [Platform Guides](#platform-guides)
  - [User Stories](#user-stories)
- [Development](#development)
  - [Editors, IDEs & UIs](#editors-ides--uis)
  - [Linting & Conventions](#linting--conventions)
  - [Code Generation](#code-generation)
  - [Developer Utilities](#developer-utilities)
- [AI & LLMs](#ai--llms)
  - [Agents, MCP & Skills](#agents-mcp--skills)
  - [AI Assistants & Tools](#ai-assistants--tools)
- [Testing & Data Quality](#testing--data-quality)
  - [Testing](#testing)
  - [Data Observability](#data-observability)
- [CI/CD](#cicd)
- [Orchestration & Ingestion](#orchestration--ingestion)
- [Data Modeling](#data-modeling)
- [Data Governance](#data-governance)
  - [Lineage](#lineage)
  - [Docs, Diagrams & Catalogs](#docs-diagrams--catalogs)
- [Security & Privacy](#security--privacy)
- [BI & Semantic Layer](#bi--semantic-layer)
- [Machine Learning](#machine-learning)
- [Scaling dbt](#scaling-dbt)
  - [Large Projects & Mesh](#large-projects--mesh)
  - [Performance, Monitoring & Cost](#performance-monitoring--cost)
- [dbt Cloud](#dbt-cloud)
- [Packages](#packages)
- [Adapters](#adapters)
- [Sample Projects](#sample-projects)
- [Community](#community)
  - [Events & Talks](#events--talks)
  - [Newsletters & Reports](#newsletters--reports)
  - [Podcasts](#podcasts)
  - [Forums & Social](#forums--social)
- [Contributors](#contributors)

## Learning

General material to learn dbt and analytics engineering. Topic-specific guides live in their topic's section.

### Courses

Structured courses, free and paid.

- [Advanced dbt](https://uplimit.com/course/advanced-dbt) - Paid Uplimit course on advanced dbt topics.
- [Mastering dbt: Beginner to Pro](https://www.udemy.com/course/mastering-dbt-data-build-tool-bootcamp/) - Paid Udemy course that covers theory, building a dbt project from scratch, and deploying to dbt Cloud.
- [Zero to Hero dbt](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/) - Complete course covering both theory & practice through real-world Airbnb use-case.
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - Data engineering course on cutting edge tools including dbt.
- [Analytics Engineering with dbt](https://uplimit.com/course/analytics-engineering-with-dbt) - Paid course offered by Uplimit covering the basics of dbt.
- [Refactoring SQL for Modularity](https://learn.getdbt.com/courses/refactoring-sql-for-modularity) - Free dbt Labs course on refactoring legacy SQL into modular dbt models.
- [dbt Fundamentals](https://learn.getdbt.com/catalog) - Official free course by dbt Labs. Excellent for learning the basics of dbt.
- [Learn DBT from Scratch](https://www.udemy.com/course/learn-dbt-from-scratch/) - Guides you through a setup paired with Snowflake, with extras.

### Tutorials & Cheat Sheets

Hands-on walkthroughs and quick references.

- [dbt Jinja Functions Cheat Sheet](https://datacoves.com/post/dbt-jinja-functions-cheat-sheet) - Datacoves' cheat sheet covering the Jinja additions in dbt Core.
- [The Ultimate Guide to dbt](https://count.co/canvas/JpkaYdqr9oN) - A comprehensive canvas guide to dbt, from the basics to advanced topics.
- [Understanding the scopes of dbt tags](https://yu-ishikawa.medium.com/understanding-the-scopes-of-dbt-tags-691d0286f3aa) - How tags set in `dbt_project.yml`, property files and config blocks combine and inherit.
- [Jinja cheatsheet](https://github.com/zsombor-flds/dbt-jinja-cheatsheet) - Quick reference for the Jinja syntax used in dbt models and macros.
- [Tips and Tricks about working with dbt](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287) - Tips from community members.
- [dbt-tips](https://github.com/erika-e/dbt-tips) - Excellent companion to your dbt practice with rich collection of tips.
- [dbt for Data Transformation – Hands-on](https://www.kdnuggets.com/2021/07/dbt-data-transformation-tutorial.html) - Hands-on tutorial for building your first project in dbt Cloud.

### Best Practices

How to structure, style and maintain a dbt project.

- [How we style our dbt projects](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects) - Official dbt Labs style guide for models, SQL, YAML and Jinja.
- [How we structure our dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview) - Official dbt Labs guide to organizing staging, intermediate and mart models.
- [Best Practices for your dbt Style Guide](https://airbyte.com/blog/best-practices-dbt-style-guide) - Standards for well organized base layer with Airbyte ingestion.
- [Clean your warehouse of old and deprecated models](https://discourse.getdbt.com/t/clean-your-warehouse-of-old-and-deprecated-models/1547) - Clean out warehouse models which are not existent in the project.
- [GitLab dbt Guide](https://handbook.gitlab.com/handbook/enterprise-data/platform/dbt-guide/) - GitLab Data Team's guide to setting up and working with dbt.
- [Your Essential dbt Project Checklist](https://discourse.getdbt.com/t/your-dbt-project-checklist/1377) - Checklist on items necessary for a successful dbt project.

### Platform Guides

Running dbt well on a specific warehouse or cloud.

- [Run dbt on Snowflake and DuckDB with shared Iceberg tables](https://www.greybeam.ai/blog/run-dbt-on-snowflake-and-duckdb) - One dbt project that runs some models on Snowflake and others on DuckDB, both reading and writing the same Iceberg tables through Snowflake's Horizon catalog, with no S3 bucket or IAM setup.
- [Best Practices for Leveraging Amazon Redshift and dbt](https://d1.awsstatic.com/products/Redshift/Amazon-Redshift-dBT-Best-Practices_paper.pdf) - Best practices for running dbt on Redshift, including performance tuning and dbt code optimizations.
- [Accelerating Data Teams with dbt & Snowflake](https://www.snowflake.com/en/developers/guides/data-teams-with-dbt-cloud/) - A dbt & Snowflake workshop on financial data.
- [Doing More With Less: Using DBT to load data from AWS S3 to Snowflake via External Tables](https://medium.com/slateco-blog/doing-more-with-less-usingdbt-to-load-data-from-aws-s3-to-snowflake-via-external-tables-a699d290b93f) - An alternative guide to set up your dbt-external-tables workflow.
- [Beware of DBT Incremental Updates Against Snowflake External Tables](https://dm03514.medium.com/beware-of-dbt-incremental-updates-against-snowflake-external-tables-beeda513e748) - Things you should be aware of when using external tables with dbt.
- [Start Modeling Data](https://dataschool.com/sql-optimization/start-modeling-data/) - Configuring BigQuery for your dbt project.
- [dbt + Materialize: Streaming to a dbt project near you](https://www.getdbt.com/blog/dbt-materialize-streaming-to-a-dbt-project-near-you) - How to own your real-time transformation workflows like batch-based alternatives.
- [Deploying and Running dbt on Azure Container Instances](https://medium.com/hashmapinc/deploying-and-running-dbt-on-azure-container-instances-f6136f8ea74c) - Demonstration of integration with Azure.

### User Stories

How teams use dbt, and what they learned.

- [Building an extension framework for dbt](https://medium.com/data-monzo/building-an-extension-framework-for-dbt-654ca99495da) - How Monzo built an extension framework for dbt.
- [Leveraging DBT as a Data Modeling tool](https://medium.com/analytics-and-data/leveraging-dbt-as-a-data-modeling-tool-b3caf78f4a3a) - Reflection on one-year usage of dbt.
- [Who's really using dbt?](https://semistructured.substack.com/p/dbt-analytics-engineering-or-data-engineering) - Behind the community of analytics engineers.
- [dbt and the Analytics Engineer — what's the hype about](https://medium.com/validio/dbt-and-the-analytics-engineer-whats-the-hype-about-907eb86c4938) - Behind the upheaval of the analytics engineer profession.

## Development

Tools for writing, checking and generating dbt code.

### Editors, IDEs & UIs

Editor extensions and local web UIs for working on dbt projects.

- [Lunapad](https://lunapad.dev/) - Open-source notebook for running, exploring, and debugging dbt projects with interactive data analysis.
- [dbt-ui](https://github.com/data-diving/dbt-ui) - A modern web-based user interface for dbt-core projects.
- [dbt-Workbench](https://github.com/rezer-bleede/dbt-Workbench) - An open UI for dbt providing model browsing, lineage visualization, run orchestration, documentation, environment management — without vendor lock-in. Designed for local, on‑prem, and air‑gapped deployments.
- [dbt-command-center](https://github.com/montara-io/dbt-command-center) - A local web application that provides a user-friendly interface to monitor and manage dbt runs.
- [Turntable VS Code extension](https://www.turntable.so/extension) - Docs composer and column-level lineage in VS Code.
- [dbtpal](https://github.com/PedramNavid/dbtpal) - A Neovim plugin for dbt model editing.
- [dbt Power User](https://github.com/AltimateAI/vscode-dbt-power-user) - VS Code extension for dbt: model lineage, query preview, autocompletion and documentation.

### Linting & Conventions

Linters, formatters and checks that keep a project consistent.

- [dbt-doctor](https://github.com/northgraindata/dbt-doctor) - CLI health check and linter for dbt projects (SQL, YAML, Jinja): 190+ custom rules, optional SQLFluff, 0–100 score, GitHub Actions CI, and coding-agent skills.
- [dbtective](https://github.com/feliblo/dbtective) - Rust-powered linter that checks dbt projects and their metadata against best practices.
- [dbt-bouncer](https://github.com/godatadriven/dbt-bouncer) - Configure and enforce conventions for your dbt project.
- [dbt-score](https://github.com/PicnicSupermarket/dbt-score) - Linter for dbt metadata.
- [dbt-checkpoint](https://github.com/dbt-checkpoint/dbt-checkpoint) - Pre-commit hooks that check your dbt project (docs, tests, naming) before changes are committed.
- [oliver-twist](https://github.com/autotraderuk/oliver-twist) - Audits the dbt DAG and generates a summary report.
- [dbt-project-evaluator](https://github.com/dbt-labs/dbt-project-evaluator) - Highlights areas of a dbt project that are misaligned with dbt Labs' best practices.
- [sqlfmt](https://github.com/tconbeer/sqlfmt) - Formats your dbt SQL code so you don't have to.
- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - SQL linter that supports dbt and Jinja templating.
- [dbt-coverage](https://github.com/slidoapp/dbt-coverage) - Checks dbt docs and tests coverage.
- [dbt-meta-testing](https://github.com/tnightengale/dbt-meta-testing) - Enforce documentation and test coverage on your models.

### Code Generation

Scaffold projects and generate models, sources and YAML.

- [cookiecutter-dbt](https://github.com/datacoves/cookiecutter-dbt) - Cookiecutter template for dbt projects.
- [dbt-cue](https://github.com/gilcrest/dbt-cue) - Generate dbt yml files using the CUE language.
- [dbt-osmosis](https://github.com/z3z1ma/dbt-osmosis) - Automated YAML management and a Streamlit workbench to speed up dbt development.
- [dbt-invoke](https://github.com/Dashlane/dbt-invoke) - CLI for creating, updating, and deleting dbt property files.
- [dbt-codegen](https://github.com/dbt-labs/dbt-codegen) - Macros that generate dbt code, and log it to the command line.
- [dbt-coves](https://pypi.org/project/dbt-coves/) - CLI tool for generating a scaffold for your dbt project.

### Developer Utilities

Smaller helpers for day-to-day dbt work.

- [backfill](https://github.com/shyamsivakumar/backfill) - Terminal footer that pays you while dbt runs - one sponsored line on the bottom row during long commands (dbt Core and dbt Cloud CLI), 50% ad revenue share. Open-source Go CLI; never reads your code, queries, or output.
- [dbt-ibis](https://github.com/binste/dbt-ibis) - Write your dbt models using [Ibis](https://ibis-project.org/), the portable Python dataframe library.
- [fst: flow state tool](https://github.com/sungchun12/fst) - A tool to help you stay in flow state while developing dbt models.
- [dbt-feature-flags](https://github.com/z3z1ma/dbt-feature-flags) - Feature Flags in dbt models.
- [dbt-container-skeleton](https://github.com/gnilrets/dbt-container-skeleton) - All the basics to get a nice containerized dbt development environment.
- [dbt-artifacts-parser](https://github.com/yu-iskw/dbt-artifacts-parser) - Work with `catalog.json`, `manifest.json`, `run_results.json` and `sources.json` as Python objects.
- [dbtenv](https://github.com/brooklyn-data/dbtenv) - A version manager for dbt.
- [Run changed models based on Git status](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287/2) - Handy bash function to run changed models since last commit.
- [fzf-dbt](https://github.com/Infused-Insight/fzf-dbt) - Search dbt models interactively from terminal.
- [How we set up our computers for working on dbt projects](https://discourse.getdbt.com/t/how-we-set-up-our-computers-for-working-on-dbt-projects/243) - Tools and setup tips that improve the dbt development experience.

## AI & LLMs

Generative AI for dbt: giving agents access to your project, and LLM-powered tools built on it.

### Agents, MCP & Skills

MCP servers, agent skills and harnesses that let coding agents and assistants work with dbt.

- [Dex](https://github.com/exmergo/dex) - Agent skills (Claude Code, Codex) that author dbt models, tests, and MetricFlow semantic models as reviewable diffs, profile source warehouses read-only, and detect schema, grain, and semantic drift. Apache-2.0.
- [dlin](https://github.com/eitsupi/dlin) - Gives coding agents instant dbt lineage: no dbt compile, no Python, no grep. Fast model-level lineage CLI parsing SQL files directly (or a `manifest.json`), with experimental column-level lineage too.
- [Altimate Code](https://github.com/AltimateAI/altimate-code) - Open-source data engineering harness with 100+ deterministic tools for building, validating, optimizing, and shipping data products — usable from any LLM, across your warehouses. Ranked #1 on ADE-Bench (78%).
- [Bonnard](https://bonnard.ai) - Governed, multi-tenant MCP access to customer data. Turn your dbt models into a secure, per-customer MCP for AI agents.
- [dbt-agent-skills](https://github.com/dbt-labs/dbt-agent-skills) - A curated collection of agent skills, built and maintained by dbt Labs, to help AI coding agents work more effectively with dbt.
- [dbt-cli-mcp](https://github.com/MammothGrowth/dbt-cli-mcp) - MCP server that wraps the dbt CLI, so agents can run, test and inspect dbt projects.
- [dbt MCP Server](https://github.com/dbt-labs/dbt-mcp) - Official dbt Labs MCP server: lets AI agents query the dbt Semantic Layer, discover models and lineage, and run dbt commands.

### AI Assistants & Tools

LLM-powered analysts, assistants and generators built on dbt projects.

- [Dot](https://www.getdot.ai/integrations/dbt) - AI data analyst for Slack, Microsoft Teams and the web. Syncs your dbt project (model and column docs, SQL, lineage) to write more accurate SQL, and exports its dashboards back to dbt as exposures.
- [Ragstar](https://github.com/pragunbhutani/dbt-llm-agent) - AI data analyst that builds a knowledge base from your dbt models and docs and answers questions in a web app or Slack (formerly dbt-llm-tools).
- [turboYAML](https://github.com/fredbrowne/turboYAML) - An AI-powered CLI tool for converting dbt SQL files to YAML using OpenAI.
- [datapilot](https://github.com/AltimateAI/datapilot-cli) - CLI for Altimate's AI teammate that checks SQL and dbt projects against best practices.
- [Entity matching with LLMs in dbt](https://github.com/jacopotagliabue/foundation-models-for-dbt-entity-matching) - An experiment in productionizing LLMs: a dbt pipeline that asks a language model whether two product records are the same item.

## Testing & Data Quality

Test your models and keep an eye on the data they produce.

### Testing

Testing frameworks, packages and guides, from unit tests to data contracts.

- [SQL Data Checks](https://www.arcodash.com/tools/sql-data-checks/) - Free browser tool that writes copy-ready SQL for freshness, row count, null rate, duplicate key and job heartbeat checks across 10 dialects.
- [grainguard](https://github.com/rohitchaurasia195-web/GRAINGUARD) - Static checker that flags SUM, COUNT and AVG computed after joins that can repeat rows (fan outs and chasm traps). Infers the grain of every model from unique tests and the SQL itself, with no warehouse connection, so it runs in CI or pre-commit.
- [data-contract-validator](https://github.com/OGsiji/data-contract-validator) - Fails the pull request when a model stops producing what a downstream consumer expects. Reads columns from `catalog.json`/`manifest.json` (falling back to a sqlglot parse of the SQL) and compares them against reverse-ETL destinations such as HubSpot CRM and against FastAPI/Pydantic services, in CI or pre-commit.
- [Misata](https://github.com/rasinmuhammed/misata) - Generate known-answer seed and test data for dbt models: declare the expected aggregates (revenue curves, rates, rollups) and assert your models return them exactly.
- [dbt-testgen](https://github.com/kgmcquate/dbt-testgen) - Generate dbt tests based on sample data.
- [dbt-assertions](https://github.com/AxelThevenot/dbt-assertions) - Package to assert rows in-line with dbt macros.
- [Power up your data quality with grouped checks](https://docs.getdbt.com/blog/grouping-data-tests) - How to use grouped checks in dbt-utils to keep your data on track.
- [pytest-dbt-core](https://github.com/godatadriven/pytest-dbt-core) - A pytest plugin for testing your dbt projects.
- [Writing Unit Tests for dbt](https://www.equalexperts.com/blog/our-thinking/writing-unit-tests-for-dbt-with-tdd/) - Test-driven development in dbt with the dbt-unit-testing package.
- [dbt-unit-testing](https://github.com/EqualExperts/dbt-unit-testing) - Package which contains macros to support unit testing.
- [Environment-dependent Unit Testing in dbt](https://medium.com/hiflylabs/environment-dependent-unit-testing-in-dbt-c081a0a5ff1e) - Guide on how to run unit tests in dbt dynamically.
- [dbt-expectations](https://github.com/metaplane/dbt-expectations) - Great Expectations-style tests as dbt macros. Maintained fork by Metaplane of the original calogica package, which is no longer supported.
- [How do you test your data](https://discourse.getdbt.com/t/how-do-you-test-your-data/149) - Suggestions on testing your data powered by the community.
- [How to unit test sql transforms in dbt](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/) - Unit test using source defer and generic custom tests.

### Data Observability

Monitoring, anomaly detection and alerting on the data your models build.

- [DataOps TestGen](https://github.com/DataKitchen/dataops-testgen) - Open-source data quality tool that complements `dbt test`: profiles the tables your models build and the sources they read, generates tests from the profiling results, and monitors freshness, volume, and schema, with a web UI.
- [Upstrace](https://github.com/ashg2099/upstrace) - Column-level drift detection and lineage-based root-cause analysis for dbt projects.
- [Aegis DQ](https://github.com/aegis-dq/aegis-dq) - Agentic data quality framework that runs YAML rules against your warehouse (DuckDB, BigQuery, Snowflake, Databricks, Athena, PostgreSQL), then uses LLMs to diagnose failures, trace root causes, and propose SQL fixes. Pairs naturally with dbt models as the validation layer after `dbt run`.
- [Scherlok](https://github.com/rbmuller/scherlok) - Zero-config data quality CLI that complements `dbt test` with auto-detected anomalies (volume, schema drift, freshness, distribution, cardinality) on every materialized model after `dbt run`.
- [DataKitchen Open Source Data Observability](https://github.com/DataKitchen/data-observability-installer) - Open source observability and alerting across your data estate, with fast data quality test generation and execution.
- [diqu](https://diqu.iflambda.com/latest/) - CLI companion that turns dbt test results into detailed alerts on the platforms your team already uses.
- [dq-tools](https://github.com/infinitelambda/dq-tools) - Store dbt test results and visualize them in a BI dashboard built on 6 data quality KPIs.
- [BigQuery Stale data detection](https://eponkratova.medium.com/stale-data-detection-with-dbt-and-bigquery-dataset-metadata-662196cf9370) - Stale data detection with dbt and BigQuery dataset metadata.
- [Elementary](https://github.com/elementary-data/elementary) - Data observability for dbt: anomaly detection as dbt tests, plus a report of test results and run history.
- [Metaplane](https://www.metaplane.dev/) - Data observability platform on top of your dbt and BI stack.
- [Soda](https://docs.soda.io/soda-documentation/soda-v3/integrate-soda/integrate-dbt) - Integration of Soda's data observability platform and dbt.
- [re_data](https://github.com/re-data/re-data) - A dbt package for monitoring metrics and detecting anomalies.

## CI/CD

Ship changes safely: slim CI, data diffs, deployment patterns and pull request workflows.

- [reladiff](https://github.com/erezsh/reladiff) - Diff large datasets within or across databases. Maintained continuation of Datafold's data-diff, which is archived.
- [dbt-plan](https://github.com/PresentJay/dbt-plan) - `terraform plan` for dbt: diffs compiled SQL between two revisions to predict the DDL `dbt run` would emit. Names the columns an `on_schema_change: sync_all_columns` model will drop, the downstream models and data tests that drop breaks, and enforced-contract violations. Reads files only -- no warehouse connection -- so it runs locally before `dbt run` and on fork pull requests, where warehouse-connected checks cannot.
- [Guide to Running DBT in Production](https://jaehyeon.me/blog/2024-09-13-dbt-guide/) - A complete CI/CD process for a dbt project: defer (slim CI) and unit tests for CI, automatic deployment to lower environments, and [Write-Audit-Publish](https://lakefs.io/blog/data-engineering-patterns-write-audit-publish/) with dbt clone for production.
- [DBT CI/CD Demo with BigQuery and GitHub Actions](https://jaehyeon.me/blog/2024-09-05-dbt-cicd-demo/) - A demo CI/CD implementation using GitHub Actions, including [slim CI](https://docs.getdbt.com/reference/node-selection/defer) and [unit tests](https://docs.getdbt.com/docs/build/unit-tests).
- [dbt-ci-cd](https://github.com/bruno-szdl/dbt-ci-cd) - Example setup that demonstrates best practices for testing and deploying dbt models.
- [dbt-data-diff](https://github.com/infinitelambda/dbt-data-diff) - Data-diff solution for dbt-ers with Snowflake.
- [How to Create CI/CD Pipelines for dbt Core](https://paulfry999.medium.com/v0-4-pre-chatgpt-how-to-create-ci-cd-pipelines-for-dbt-core-88e68ab506dd) - Implement dbt Cloud's Slim CI job pattern with dbt Core.
- [dbt-beyond-the-basics](https://github.com/pgoslatara/dbt-beyond-the-basics) - Showcase of advanced options when running CI for dbt.
- [Continuous Integration and Automated Build Testing with dbt Cloud](https://blog.rittmananalytics.com/continuous-integration-and-automated-analytics-test-pipelines-using-dbt-and-dbtcloud-c4517f40b874) - Detailed walkthrough of setting up Slim CI in dbt Cloud.
- [Datafold](https://docs.datafold.com/data-diff/what-is-data-diff) - Data diffs in CI: see how a change affects the data before it's merged.
- [DDO](https://github.com/marco-roy/DDO) - Perform DataOps & administrative CI/CD on your data warehouse.
- [dbt-dry-run](https://github.com/autotraderuk/dbt-dry-run) - Auto Trader's tool that validates a whole dbt project with BigQuery dry run jobs, catching invalid SQL in seconds without running any models.
- [Slim CI/CD with Bitbucket Pipelines](https://docs.getdbt.com/blog/slim-ci-cd-with-bitbucket-pipelines) - How to set up slim CI on Bitbucket.
- [Test SQL Pipelines against Production Clones using DBT and Snowflake](https://medium.com/airtribe/test-sql-pipelines-against-production-clones-using-dbt-and-snowflake-2f8293722dd4) - Use Snowflake zero-copy clones to run slim CI checks against production data.
- [Performing a blue/green deploy of your dbt project on Snowflake](https://discourse.getdbt.com/t/performing-a-blue-green-deploy-of-your-dbt-project-on-snowflake/1349) - A tidy, fail-safe way to run dbt in production with two parallel production environments.
- [How we speed up our CI runs by 10x using Slim CI](https://discourse.getdbt.com/t/how-we-sped-up-our-ci-runs-by-10x-using-slim-ci/2603) - Limit data in long-running CI checks to speed up development.
- [How to review an analytics pull request](https://www.getdbt.com/blog/how-to-review-an-analytics-pull-request) - Checkpoints to consider when reviewing an analytics engineer PR.
- [How to set up a dbt data-ops workflow, using dbt cloud and Snowflake](https://www.startdataengineering.com/post/cicd-dbt/) - Leverage GitHub Actions to set up CI/CD with dbt Core.

## Orchestration & Ingestion

Schedule and run dbt, and load the data it transforms.

- [Datanika](https://github.com/datanika-io/datanika-core) - Open-source platform that runs dbt-core transformations alongside dlt-powered extract and load, with 36 connectors, cron scheduling, and run history in one web UI. AGPL-3.0, self-hostable with Docker Compose or Helm.
- [ModelDock](https://modeldock.run) - Hosted dbt-core scheduler. Connect your repo, pick dbt-core and adapter version, set a cron, run dbt-core in isolated Docker containers. No Airflow to manage.
- [ingestr](https://github.com/bruin-data/ingestr) - CLI tool to copy data from any source to any destination with a single command. Load data into your warehouse before dbt transforms it. Supports 50+ sources including PostgreSQL, MongoDB, Salesforce, Shopify.
- [Bruin](https://github.com/bruin-data/bruin) - Run and schedule dbt-style SQL transformations without Airflow. Adds data ingestion (50+ sources) and built-in data quality to the transformation layer. Open-source CLI or managed [Bruin Cloud](https://getbruin.com) for teams who want dbt Cloud-like experience with ingestion included.
- [dlt (data load tool)](https://dlthub.com/) - Open source Python library for loading data into your warehouse, ready for dbt.
- [Orchestrate dbt Core jobs with Airflow and Cosmos](https://www.astronomer.io/docs/airflow/airflow-dbt) - Run your dbt Core projects as Apache Airflow DAGs and Task Groups.
- [modal-dbt](https://github.com/trouze/modal-dbt) - Run dbt jobs on Modal, a serverless application platform.
- [Why I moved my dbt workloads to GitHub and saved over $65,000](https://medium.com/@datajuls/why-i-moved-my-dbt-workloads-to-github-and-saved-over-65-000-759b37486001) - Save by replacing dbt Cloud with GitHub Actions.
- [prefect-dbt](https://www.prefect.io/docs/integrations/prefect-dbt) - Prefect integration for running dbt Core and dbt Cloud jobs from your Prefect flows.
- [Run dbt in Azure Data Factory](https://medium.com/@guangx/run-dbt-in-azure-data-factory-a-clean-solution-for-azure-cloud-edddf0c85849) - Primer about dbt on Azure Data Stack.
- [Dagster dbt integration](https://dagster.io/docs/integrations/libraries/dbt) - Load dbt models as Dagster assets and orchestrate them alongside the rest of your pipelines.
- [Building a Scalable Analytics Architecture with Airflow and dbt](https://www.astronomer.io/blog/airflow-dbt-1/) - Leveraging the dbt manifest in Airflow.
- [Building a robust data pipeline with the dAG stack: dbt, Airflow, Great Expectations](https://airflowsummit.org/sessions/2021/building-a-robust-data-pipeline-with-the-dag-stack/) - Demonstration of a data orchestration project with Airflow.

## Data Modeling

Modeling patterns: Kimball, Data Vault and slowly changing dimensions.

- [dbt-scd2-utils](https://github.com/henryupton/dbt-scd2-utils) - Materializations for SCD Type 0, 1 and 2 tables on Snowflake with shared audit columns, soft-delete handling, a metadata-preserving full refresh and an `scd2_join` macro for temporal joins.
- [metadv](https://github.com/data-diving/metadv) - Python library for generating models from a declarative YAML configuration. It supports multiple data modeling approaches including Data Vault 2.0, Anchor Modeling, and Dimensional Modeling, with template packages for popular dbt libraries.
- [trange_join](https://gist.github.com/gnilrets/48886b4c8945dde1da13547c2373df73) - Macro to join dbt snapshots.
- [How to create Kimball dimensional models with dbt](https://docs.getdbt.com/blog/kimball-dimensional-model) - A step by step guide on how to build Kimball dimensional models with dbt.
- [dq-vault](https://github.com/infinitelambda/dq-vault) - Data Quality Observation of Data Vault layer.
- [dbtvault-generator](https://github.com/Oracen/dbtvault-generator) - Generate AutomateDV (formerly dbtvault) files from YAML metadata.
- [TurboVault Engine](https://github.com/ScalefreeCOM/turbovault-engine) - Generates a complete dbt project of Data Vault models for the datavault4dbt package from source metadata (successor of turbovault4dbt).
- [datavault4dbt](https://github.com/ScalefreeCOM/datavault4dbt) - Macros for staging and creation of all DataVault-Entities you need, to build your own DataVault2.0 solution.
- [AutomateDV](https://automate-dv.readthedocs.io/en/latest/) - Package for generating and executing ETL for Data Vault 2.0 (formerly dbtvault).

## Data Governance

Know what you have and where it comes from.

### Lineage

Column-level lineage and impact analysis.

- [sqllens](https://github.com/NiclasOlofsson/sqllens) - TypeScript SQL parser and static analyzer: type inference, schema diagnostics, and column-level lineage. Reads Jinja-templated SQL (dbt models) natively, without rendering.
- [dbt-colibri](https://github.com/b-ned/dbt-colibri) - Self hostable column-level lineage for dbt core projects.
- [dbt-column-lineage](https://github.com/Oisix/dbt-column-lineage) - Visualize the column-level lineage of dbt models.
- [dbt-column-lineage-extractor](https://github.com/canva-public/dbt-column-lineage-extractor) - Extract column-level lineage from dbt projects.
- [dbt-lineagex](https://github.com/sfu-db/dbt-lineagex) - A Column Level Lineage Graph for dbt.

### Docs, Diagrams & Catalogs

Documentation sites, ERDs and data catalogs built from dbt metadata.

- [dbt Docs on Databricks Apps](https://apps-cookbook.dev/gallery/dbt-docs-on-databricks-apps) - Serve the site from `dbt docs generate` as a Databricks App, with a small Python server that handles the docs' client-side routing.
- [quickdbd-cli](https://github.com/MarkPhamm/quickdbd-cli) - Interactive ER diagrams from a dbt `manifest.json` (keys and relationships inferred from tests) or QuickDBD/DBML text, readable at 200+ tables, with schema diffs as PR comments and a VS Code extension.
- [ERD Studio](https://github.com/liam-machine/erd-studio) - VS Code extension that puts a visual ERD designer inside your dbt repo. Two-stage (logical/physical) canvas, drift detection against `manifest.json`, auto-generated `selectors.yml`, and AI-readable semantic models (YAML/JSON) with a built-in harness for Claude, Copilot, Gemini, and Codex.
- [docbt](https://github.com/aleenprd/docbt) - Documentation Build Tool - Generate YAML documentation for dbt models with optional AI assistance. Built with Streamlit for an intuitive and familiar web interface.
- [metaplane cli](https://github.com/metaplane/cli) - CLI that builds a browsable UI of your latest dbt run from the target folder.
- [dbt_to_dbdiagram](https://gist.github.com/pcreux/b2e4a288b272fb17a36d319734fbb8ee) - Generate an ERD via dbdiagram.io from a dbt project.
- [DataHub](https://docs.datahub.com/docs/generated/ingestion/sources/dbt/) - Open source data catalog with governance and observability: view models, docs, test results and column-level lineage across dbt projects and downstream dashboards.
- [dbt-exposures-crawler](https://github.com/voi-oss/dbt-exposures-crawler) - Automate the creation of dbt exposures from different sources.
- [Speeding up the dbt™ docs by 20x with React Server Components](https://dagster.io/blog/dbt-docs-on-react) - A rewrite of dbt docs using Next.js with React Server Components and SSG.
- [dbt Docs as a Static Website](https://medium.com/hiflylabs/dbt-docs-as-a-static-website-c50a5b306514) - How to deploy dbt docs as a static website with App Engine and GitHub Actions.
- [dbterd](https://github.com/datnguye/dbterd) - CLI to generate DBML file from dbt manifest.json.
- [Automatically generate ERD](https://github.com/dbt-labs/docs.getdbt.com/discussions/1541) - Automatically generate ERDs and display in your docs site.
- [dbt-docs-to-notion](https://github.com/marketplace/actions/dbt-docs-to-notion) - A GitHub action for exporting dbt model docs to a Notion database.
- [dbt-erdiagram-generator](https://github.com/intellishore/dbt-erdiagram-generator) - Generates ERDs from a dbt project.

## Security & Privacy

Masking, tagging and anonymizing sensitive data.

- [dbt-snow-mask](https://github.com/entechlog/dbt-snow-mask) - A dbt package for Snowflake Dynamic Data Masking.
- [dbt-privacy](https://github.com/pvcy/dbt-privacy) - Macros to make it easier to protect your customers' data.
- [dbt-tags](https://github.com/infinitelambda/dbt-tags) - Tag-based masking policies management in Snowflake.

## BI & Semantic Layer

Metrics, semantic layers and BI tools that build on dbt models.

- [Cube](https://cube.dev/blog/introducing-dbt-integration) - Semantic layer that turns every dbt model into a governed cube with dimensions, measures, joins and descriptions. Re-syncs from CI or on every push by parsing your project, without touching the warehouse.
- [MetricFlow](https://github.com/dbt-labs/metricflow) - Define metrics in code and generate the SQL to compute them. Powers the dbt Semantic Layer and replaces the deprecated dbt_metrics package.
- [dbt_semantic_view](https://hub.getdbt.com/Snowflake-Labs/dbt_semantic_view/) - Materialize Snowflake Semantic Views with dbt and reference them from downstream models.
- [dal](https://github.com/coterahq/dal) - Build a GraphQL API on top of your dbt project.
- ["Semantic-free" is the future of Business Intelligence](https://towardsdatascience.com/semantic-free-is-the-future-of-business-intelligence-27aae1d11563) - How to leverage dbt as a data catalog and semantic layer (joins, synonyms, etc.) that BI tools can just plug into.
- [How HomeToGo connected dbt and Superset to make metadata more accessible and reduce analytical overhead](https://engineering.hometogo.com/how-hometogo-connected-dbt-and-superset-to-make-metadata-more-accessible-and-reduce-analytical-2223af539cc6) - A dbt<>Superset connector that leverages Superset's API capabilities and dbt's manifest.
- [looker-gen](https://github.com/aaronbannin/looker-gen) - Generate LookML from dbt.
- [Business Intelligence Standards](https://github.com/flexanalytics/dbt-business-intelligence) - Best practices in Business Intelligence standards for integrating with dbt.
- [FlexIt Analytics](https://learn.flexitanalytics.com/docs/dbt/) - Business Intelligence platform with deep dbt Cloud and CLI integration.
- [Self-service Business Intelligence](https://medium.com/modern-business-intelligence/self-service-business-intelligence-powered-by-dbt-3b7e24a92e27) - Eliminate the need for a data modeling semantic layer in BI.
- [dbt-metabase](https://github.com/gouline/dbt-metabase) - Model synchronization from dbt to Metabase.
- [dbt2looker](https://github.com/lightdash/dbt2looker) - Generate Looker views for dbt models.
- [dbt-superset-lineage](https://github.com/slidoapp/dbt-superset-lineage) - Push and pull metadata between dbt and Superset.
- [Lightdash](https://github.com/lightdash/lightdash) - Open source Looker alternative with deep dbt integration.
- [Superset](https://superset.apache.org/) - Open source visualization layer for your Modern Data Stack.

## Machine Learning

Feature engineering, in-warehouse models and ML workflows around dbt.

- [dbt-ml-inline-preprocessing](https://github.com/Matts52/dbt-ml-inline-preprocessing) - Feature engineering macros (scaling, encoding, imputation) that run inline in your dbt models.
- [dbt_linreg](https://github.com/dwreeves/dbt_linreg) - Linear regression in SQL using dbt.
- [dbt_ml](https://github.com/kristeligt-dagblad/dbt_ml) - Package for dbt that allows users to train, audit and use BigQuery ML models.
- [dbt + Machine Learning: What makes a great baton pass?](https://docs.getdbt.com/blog/maching-learning-dbt-baton-pass) - Landscape of ML utilities around dbt.
- [dbt-feature-store](https://github.com/fal-ai/dbt_feature_store) - Macros to build a feature store right within your dbt project.
- [dbt-ml-preprocessing](https://github.com/omnata-labs/dbt-ml-preprocessing) - A SQL port of scikit-learn's preprocessing module, provided as cross-database dbt macros.

## Scaling dbt

Keep large projects fast, cheap and manageable.

### Large Projects & Mesh

Repository layout, multi-project setups and dbt Mesh.

- [Accelerating and Scaling dbt for the Enterprise](https://www.phdata.io/blog/accelerating-and-scaling-dbt-for-the-enterprise/) - Guide for large scale dbt projects.
- [dbt-loom](https://github.com/adrienneyager/dbt-loom) - A dbt-core plugin to weave together multi-project dbt-core deployments.
- [dbt Monorepo Workflow](https://www.loom.com/share/3b4f2d1d209444f1bff75bf4aac2fe1c) - How to get started with a team dbt workflow in a monorepo.
- [How to configure your dbt repository](https://discourse.getdbt.com/t/how-to-configure-your-dbt-repository-one-or-many/2121) - Mono-repo or not mono-repo?

### Performance, Monitoring & Cost

Run metadata, warehouse cost and query performance.

- [dbt-query-tags](https://github.com/get-select/dbt-query-tags) - Automatically tag dbt-issued queries with informative metadata, on multiple warehouses (successor of dbt-snowflake-query-tags).
- [dbt_artifacts](https://github.com/brooklyn-data/dbt_artifacts) - Builds a mart of tables from dbt artifacts in your warehouse, to monitor runs, models and tests over time.
- [dbt-dag-monitoring](https://github.com/techindicium/dbt-dag-monitoring) - A dbt package for monitoring Airflow DAGs and tasks.
- [dbt_otel_export](https://github.com/irvingpop/dbt_otel_export) - Takes dbt runs and turns them into OpenTelemetry traces.
- [BigQuery Ingestion-Time Partitioning and Partition Copy With dbt](https://medium.com/teads-engineering/bigquery-ingestion-time-partitioning-and-partition-copy-with-dbt-cc8a00f373e3) - Combining ingestion-time partitioning and partition copy is a great way to achieve better performance for your models.
- [snowflake-resource-monitoring](https://github.com/dbt-labs/snowflake-resource-monitoring) - Package by dbt Labs to monitor Snowflake usage.
- [usagedata](https://github.com/anjane-tech/usagedata) - Database- and table-level usage insights from Snowflake.
- [dbt-snowflake-monitoring](https://github.com/get-select/dbt-snowflake-monitoring) - A dbt package to help you monitor Snowflake performance and costs.
- [Analyzing Fishtown's dbt project performance with artifacts](https://discourse.getdbt.com/t/analyzing-fishtowns-dbt-project-performance-with-artifacts/2214) - Using project artifacts to identify anomalies and room for refactoring.

## dbt Cloud

API clients, integrations and automation for dbt Cloud.

- [dbt-cloud-download-artifacts-action](https://github.com/pgoslatara/dbt-cloud-download-artifacts-action) - A GitHub action for downloading dbt artifacts from dbt Cloud CI jobs.
- [dbt-streamdeck](https://github.com/adrienneyager/dbt-streamdeck) - Stream Deck plugin that shows the status of dbt Cloud models and jobs.
- [dbt_cloud_run_cost](https://github.com/danthelion/dbt_cloud_run_cost) - Package to calculate dbt Cloud usage-based cost.
- [Discovery API use-cases](https://docs.getdbt.com/docs/dbt-apis/discovery-use-cases-and-examples) - Use-cases and examples for the dbt Cloud Discovery API.
- [Raycast dbt Metadata](https://github.com/b-per/raycast-dbt-cloud-metadata) - Queries the dbt Cloud API to return some useful information about your models (number of tests, time they took to run etc…).
- [GitHub Action: Cancel Running CI Job](https://github.com/Stevedow99/dbt-cloud-cancel-running-ci-job-action) - Cancels stale dbt Cloud CI runs when new commits arrive, so CI always tests the newest code.
- [dbtc](https://github.com/dpguthrie/dbtc) - Unofficial Python client for the dbt Cloud APIs.
- [Raycast dbt Jobs](https://www.raycast.com/zsombor-flds/dbtcloud) - Raycast integration to monitor dbt Cloud Jobs.
- [Terraform provider for dbt Cloud](https://github.com/dbt-labs/terraform-provider-dbtcloud) - Manage dbt Cloud as infrastructure as code, now maintained by dbt Labs.

## Packages

General-purpose dbt packages. Packages for a specific topic are listed in that topic's section.

- [dbt-unirate](https://github.com/UniRate-API/dbt-unirate) - Currency exchange rate macros and models for dbt, powered by the UniRate API.
- [dbt_diving](https://github.com/data-diving/dbt_diving) - A free to use dbt package with helper macros.
- [dbt-incremental-stream](https://github.com/arnoN7/dbt-incremental-stream) - A dbt package for Snowflake Streams.
- [dbt-reconfigured](https://github.com/Nipsuli/dbt-reconfigured) - A dbt package containing reconfigured macros.
- [dbt-census-utils](https://github.com/sutrolabs/dbt_census_utils) - A collection of dbt macros for working with Census data.
- [dbt_tld](https://github.com/GJMcClintock/dbt_tld) - A self-updating dbt library that will maintain a list of current IANA/ICANN recognized top level domains.
- [dbt-translate](https://github.com/datnguye/dbt-translate) - Translate numbers into words.
- [dbt_constraints](https://github.com/Snowflake-Labs/dbt_constraints) - Generate database constraints based on the tests in a dbt project.
- [dbt-date](https://github.com/godatadriven/dbt-date) - Date logic and calendar functionality.
- [dbt-fivetran-utils](https://github.com/fivetran/dbt_fivetran_utils) - General macros and helpers.
- [dbt-external-tables](https://github.com/dbt-labs/dbt-external-tables) - Macros to stage your external sources.
- [dbt_audit_helper](https://github.com/dbt-labs/dbt-audit-helper/) - Macros for data audits that compare columns values and schemas between tables.
- [dbt-profiler](https://hub.getdbt.com/data-mie/dbt_profiler/latest) - Data profiling and doc block generator.
- [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest) - General macros library. A must have.

## Adapters

Connect dbt to more platforms.

- [dbt-fabricspark](https://github.com/microsoft/dbt-fabricspark) - A code package from Microsoft for enabling dbt to work with Synapse Spark in Microsoft Fabric.
- [dbt-fabricsparknb](https://insight-services-apac.github.io/APAC-Capability-DAI-DbtFabricSparkNb/) - Generates Fabric Spark notebooks from dbt, by Insight; a fork of Microsoft's dbt-fabricspark.
- [dbt-timescaledb](https://github.com/sdebruyn/dbt-timescaledb) - The TimescaleDB adapter plugin for dbt.
- [dbt-fabric](https://github.com/microsoft/dbt-fabric) - A dbt adapter for working with Microsoft Fabric Data Warehouses.
- [dbt-excel](https://github.com/godatadriven/dbt-excel) - A dbt adapter for working with Excel.
- [Supported Adapters](https://docs.getdbt.com/docs/supported-data-platforms) - Trusted and community adapters listed by dbt Labs.

## Sample Projects

Complete projects to learn from, most of them runnable out of the box.

- [dbt-snowflake-template](https://github.com/collinrlenon/dbt-snowflake-template) - Production-ready template deploying dbt project to Snowflake using GH Actions.
- Data Build Tool (dbt) Pizza Shop Demo - A series of posts that illustrate data modeling and Airflow integration, targeting multiple data warehouses.
  - [Part 1 Modelling on PostgreSQL](https://jaehyeon.me/blog/2024-01-18-dbt-pizza-shop-1/)
  - [Part 2 ETL on PostgreSQL via Airflow](https://jaehyeon.me/blog/2024-01-25-dbt-pizza-shop-2/)
  - [Part 3 Modelling on BigQuery](https://jaehyeon.me/blog/2024-02-08-dbt-pizza-shop-3/)
  - [Part 4 ETL on BigQuery via Airflow](https://jaehyeon.me/blog/2024-02-22-dbt-pizza-shop-4/)
  - [Part 5 Modelling on Amazon Athena](https://jaehyeon.me/blog/2024-03-07-dbt-pizza-shop-5/)
  - [Part 6 ETL on Amazon Athena via Airflow](https://jaehyeon.me/blog/2024-03-14-dbt-pizza-shop-6/)
- [Make Open Data](https://github.com/make-open-data/make-open-data/) - A production grade ELT with tests, documentation and CI/CD (GHA) about french open data (housing, demography, geography, etc). Can be used to learn with voluminous and ambiguous data. Contributions are welcome.
- [datafold-dbt-ci-advanced](https://github.com/elliotgunn/datafold-dbt-ci-advanced) - Add 4 more integrations to your dbt CI pipeline: Slim CI, pre-commit hooks, Data Diffs, and Slack notifications.
- [NBA_Data_Modeling](https://github.com/jpooksy/paradime-dbt-nba-challenge) - Ingest, store, transform and serve insights from the official NBA API.
- [dbt-fake](https://github.com/leogodin217/dbt-fake) - Daily updated fake data for dbt learning and projects.
- [awesome-public-dbt-projects](https://github.com/InfuseAI/awesome-public-dbt-projects) - A curated list of awesome public dbt projects.
- [mdsinabox](https://github.com/matsonj/mdsinabox) - MDS in a box deployed anywhere.
- [gee_production_gatekeepers](https://github.com/nszoni/gee_production_gatekeepers) - A demonstration of production gatekeepers in Snowflake and BigQuery.
- [mdsfest-opensource-mds](https://github.com/dagster-io/mdsfest-opensource-mds) - Demo project for open source MDS.
- [f1-data-pipeline](https://github.com/InosRahul/f1-data-pipeline) - F1 Data Pipeline.
- [transfermarkt-datasets](https://github.com/dcaribou/transfermarkt-datasets) - E2E dbt project for scraping and transforming football data from Transfermarkt.
- [dbt_github_archive_bigquery](https://github.com/preset-io/dbt_github_archive_bigquery) - A dbt project for GitHub Archive data on BigQuery.
- [dbt_workspace](https://github.com/randypitcherii/dbt_workspace) - A workspace template for dbt demos.
- [Cloud Cost Monitoring](https://github.com/randypitcherii/cloud_cost_monitoring) - A dbt project to monitor cloud costs.
- dbt on AWS - A series on running dbt across AWS data services.
  - [Part 1 – Redshift](https://jaehyeon.me/blog/2022-09-28-dbt-on-aws-part-1-redshift/)
  - [Part 2 – Glue](https://jaehyeon.me/blog/2022-10-09-dbt-on-aws-part-2-glue/)
  - [Part 3 – EMR on EC2](https://jaehyeon.me/blog/2022-10-19-dbt-on-aws-part-3-emr-ec2/)
  - [Part 4 – EMR on EKS](https://jaehyeon.me/blog/2022-11-01-dbt-on-aws-part-4-emr-eks/)
  - [Part 5 – Athena](https://jaehyeon.me/blog/2022-12-06-dbt-on-aws-part-5-athena/)
- [Analytics Engineer Survey 2023](https://github.com/dbt-labs/analytics-engineering-survey/tree/main) - Repo containing data and dbt template of the survey.
- [Tracking the Fake GitHub Star Black Market with Dagster, dbt and BigQuery](https://dagster.io/blog/fake-stars) - Explore the topic of fake GitHub stars.
- [Data-aware orchestration](https://github.com/jonathanneo/data-aware-orchestration) - Dagster's ability to create a global dependency graph between different dbt projects.
- [AWS Athena x dbt](https://kiwamizamurai.github.io/posts/2022-08-25/) - How to build a small and modern data infrastructure.
- [GitLab Data Team](https://gitlab.com/gitlab-data/analytics/-/tree/master/transform/snowflake-dbt) - GitLab's open source dbt project.
- [attribution-playbook](https://github.com/dbt-labs/attribution-playbook) - A worked example to demonstrate how to model customer attribution.
- [mrr-playbook](https://github.com/dbt-labs/mrr-playbook) - A worked example to demonstrate how to model subscription revenue.
- [Use dbt inside Visual Studio Code development containers](https://github.com/davidgasquez/dbt-devcontainer) - Set up your dbt environment with pre-installed extensions.
- [dag-stack](https://github.com/spbail/dag-stack) - Demo stack combining dbt, Airflow and Great Expectations.
- [Jaffle Shop](https://github.com/dbt-labs/jaffle-shop) - Sandbox project from dbt Labs, built around a fictional sandwich shop, for learning and testing.
- [airflow-dbt-demo](https://github.com/astronomer/airflow-dbt-demo) - Demonstration of Airflow integration.
- [dbt-github-workflow](https://github.com/slve/dbt-github-workflow) - Deploy BigQuery + Airflow.
- [Spotify User Analytics](https://github.com/ftupas/dbt-spotify-analytics) - Sample dbt project with Spotify user data.

## Community

Where analytics engineers meet, read and listen.

### Events & Talks

Conferences, meetups and recorded talks.

- [dbt Summit](https://www.getdbt.com/dbt-summit) - Annual dbt Labs conference (formerly Coalesce), with keynotes and sessions on demand.
- [Data Council Austin 2023](https://www.youtube.com/playlist?list=PLAesBe-zAQmF-GpvZ3ba5YpVzoVbgzl8M) - A conference for data teams.
- [Data Council Austin 2022](https://www.youtube.com/playlist?list=PLAesBe-zAQmEod2ARZjjAHmGFoGcjaXK6) - Worldwide community driven analytics conference with a handful of talks fitting to the dbt stack.
- [Coalesce 2021](https://www.youtube.com/playlist?list=PL0QYlrC86xQnNXXXL7WPRTULbMgh_Sry3) - Second edition of the analytics engineering conference.
- [dbt meetups](https://www.meetup.com/en-AU/pro/dbt/) - List of community led dbt meetups.
- [Coalesce 2020](https://www.youtube.com/playlist?list=PL0QYlrC86xQmPf9QUceFdOarYcv3ETSsz) - Annual dbt conference full of fascinating use-cases.

### Newsletters & Reports

Newsletters, blogs and industry reports.

- [#dbtips](https://dbtips.substack.com) - Newsletter about dbt, with tips and tutorials on various topics.
- [State of Analytics Engineering 2023](https://www.getdbt.com/resources/state-of-analytics-engineering-2023) - A survey of pains, gains, and areas of investment for global data teams.
- [Metadata Weekly](https://metadataweekly.substack.com) - Weekly substack about metadata, the metrics layer and MDS.
- [Analytics Engineer Roundup](https://roundup.getdbt.com/) - Official dbt Labs newsletter on topics of the MDS.
- [Benn Stancil's Newsletter](https://benn.substack.com/) - Thought-provoking reads from the founder of Mode.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Weekly newsletter of recent trends in Data Engineering.

### Podcasts

Conversations about dbt and the data stack.

- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - One of the most popular data engineering podcasts covering great concepts and new products.
- [The Analytics Engineering Podcast](https://podcasts.apple.com/us/podcast/the-analytics-engineering-podcast/id1574755368) - Official podcast of dbt Labs.
- [Drill to Detail Podcast](https://www.rittmananalytics.com/drilltodetail) - Special guests discussing big data, business intelligence, modern data stack.

### Forums & Social

Places to ask questions and follow along.

- [dbt Labs TikTok](https://www.tiktok.com/@dbtlabs) - Official TikTok channel of dbt Labs.
- [Locally Optimistic](https://locallyoptimistic.com/about/) - A Slack community of aspiring analytics leaders discussing and sharing lessons learned and challenges from their experiences in using data.
- [DataTalks.Club](https://datatalks.club/) - Global online community of data enthusiasts. Podcasts and blogs, etc. are distributed with high frequency.
- [dbt Community Discussions](https://github.com/dbt-labs/docs.getdbt.com/discussions) - GitHub Discussions on the dbt docs repo, the successor of the dbt Discourse forum.
- [dbt Slack](https://www.getdbt.com/community) - Energy-filled hub of analytics engineers (Highly recommended).
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - Subreddit of data engineering topics.

## Contributors

Thanks for all the great resources! Can't see your avatar? Check the contribution guide on how you can submit your resources to the community!

<a href="https://github.com/Hiflylabs/awesome-dbt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Hiflylabs/awesome-dbt" />
</a>
