<!--lint disable awesome-heading-->
# Awesome dbt [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme) <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Hiflylabs/awesome-dbt"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Hiflylabs/awesome-dbt">

[<img src="dbt-logo.png" align="right" width="200">](https://www.getdbt.com/)

Welcome to the awesome curated list of dbt resources!

Any kind of contribution is greatly encouraged and appreciated. For making a contribution, **please check the [contribution guidelines](https://github.com/Hiflylabs/awesome-dbt/blob/main/contributing.md) first!** **Add new entries on the top of sections** (LIFO) to keep fresh items more visible! Also, **feel free to add new sections**.

Happy contributing!

## Contents
- [Get Started](#get-started)
- [How To](#how-to)
- [Integrations](#integrations)
- [User Stories](#user-stories)
- [Data Quality](#data-quality)
- [CI/CD](#cicd)
- [Orchestration](#orchestration)
- [Utilities](#utilities)
- [Packages](#packages)
- [Community](#community)
- [Sample Projects](#sample-projects)
- [Contributors](#contributors)

## Get Started

Courses from where you can get started with Analytics Engineering.

- [The Ultimate Guide to dbt](https://count.co/canvas/JpkaYdqr9oN) - A comprehensive canvas guide to dbt, from the basics to advanced topics.
- [dbt in a real world scenario, A Beginner dbt tutorial](https://tipseason.com/dbt-tutorial-real-world-scenario-guide/) - A beginner tutorial to understand dbt with a real world example.
- [Mastering dbt: Beginner to Pro](https://www.udemy.com/course/mastering-dbt-data-build-tool-bootcamp/?referralCode=FFF494163B7B9E5E846F) - Paid Udemy course that covers theory, building a dbt project from scratch, and deploying to dbt Cloud.
- [Analytics Engineering Glossary](https://docs.getdbt.com/glossary) - Living collection of terms & concepts commonly used in the data industry by dbt Labs.
- [Zero to Hero dbt](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/) - Complete course covering both theory & practice through real-world Airbnb use-case.
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - Data engineering course on cutting edge tools including dbt.
- [Analytics Engineering with dbt](https://corise.com/course/analytics-engineering-with-dbt) - Paid course offered by co:rise covering the basics of dbt.
- [dbt Fundamentals](https://courses.getdbt.com/collections) - Official free course offered by dbt. Excellent for learning the basics of dbt Cloud.
- [Refactoring SQL for Modularity](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) - Another dbt labs offered free course on dbt refactoring and CTE supercharging.
- [Learn DBT from Scratch](https://www.udemy.com/course/learn-dbt-from-scratch/) - Guides you through a setup paired with Snowflake (decorated with extras).

## How To

Helping hand on setting up integrations and implementing best practices.

- [dbt Jinja Functions Cheat Sheet - Datacoves](https://datacoves.com/post/dbt-jinja-functions-cheat-sheet) - Jinja Functions Cheat Sheet that covers the Jinja additions in dbt Core.
- [Discovery API use-cases](https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-use-cases-and-examples) - Use-cases and examples for the dbt Cloud Discovery API.
- [dbt Docs as a Static Website](https://medium.com/hiflylabs/dbt-docs-as-a-static-website-c50a5b306514) - How to deploy dbt docs as a static website with App Engine and GitHub Actions.
- [dbt Monorepo Workflow](https://www.loom.com/share/3b4f2d1d209444f1bff75bf4aac2fe1c) - How to get started with the team dbt workflow.
- [Configuring Snowflake warehouse sizes in dbt](https://select.dev/posts/configuring-snowflake-warehouse-sizes-in-dbt) - How to use dbt with Snowflake to allow specific warehouses to be chosen down to the model level.
- [BigQuery Ingestion-Time Partitioning and Partition Copy With dbt](https://medium.com/teads-engineering/bigquery-ingestion-time-partitioning-and-partition-copy-with-dbt-cc8a00f373e3) - Combining ingestion-time partitioning and partition copy is a great way to achieve better performance for your models.
- [Power up your data quality with grouped checks](https://docs.getdbt.com/blog/grouping-data-tests) - How to use grouped checkes in dbt-utils to keep our data "on track".
- [Dry running our data warehouse using BigQuery and dbt](https://engineering.autotrader.co.uk/2022/04/06/dry-running-our-data-warehouse-using-bigquery-and-dbt.html) - Use dbt & BigQuery dry run jobs to validate our 1000+ models in under 30 seconds.
- [Automatically generate ERD](https://github.com/dbt-labs/docs.getdbt.com/discussions/1541) - Automatically generate ERDs and display in your docs site.
- [Business Intelligence Standards](https://github.com/flexanalytics/dbt-business-intelligence) - Best practices in Business Intelligence standards for integrating with dbt.
- [Jinja cheatsheet](https://github.com/zsombor-flds/dbt-jinja-cheatsheet) - Jinja cheatsheet for dbt development.
- [Test SQL Pipelines against Production Clones using DBT and Snowflake](https://medium.com/airtribe/test-sql-pipelines-against-production-clones-using-dbt-and-snowflake-2f8293722dd4) - Leverage Snowflake Zero-copy-clones to run slim ci checks.
- [How we structure our dbt projects](https://discourse.getdbt.com/t/how-we-used-to-structure-our-dbt-projects/355) - How the dbt team structures its dbt projects.
- [How we structure our dbt projects](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355) - How the dbt team structures its dbt projects.
- [dbt guide](https://about.gitlab.com/handbook/business-technology/data-team/platform/dbt-guide/) - Primer on how you should properly set up and configure your dbt workflow.
- [dbt for Data Transformation – Hands-on](https://www.kdnuggets.com/2021/07/dbt-data-transformation-tutorial.html) - Yet another tutorial for using dbt Cloud.
- [Start Modeling Data](https://dataschool.com/sql-optimization/start-modeling-data/) - Configuring Bigquery with your dbt project.
- [Accelerating Data Teams with dbt & Snowflake](https://quickstarts.snowflake.com/guide/data_teams_with_dbt_cloud/?index=..%2F..index) - A dbt & Snowflake workshop on financial data.
- [Creating a dev environment quickly on Snowflake](https://discourse.getdbt.com/t/creating-a-dev-environment-quickly-on-snowflake/1151) - Setting up teh integraton with Snowflake.
- [How to set up a dbt data-ops workflow, using dbt cloud and Snowflake](https://www.startdataengineering.com/post/cicd-dbt/) - Leverage GitHub Actions to set up CI/CD with dbt Core.
- [How to configure your dbt repository](https://discourse.getdbt.com/t/how-to-configure-your-dbt-repository-one-or-many/2121) - Mono-repo or not mono-repo?
- [Best Practices for Optimizing Your dbt and Snowflake Deployment](https://resources.snowflake.com/white-paper/best-practices-for-optimizing-your-dbt-and-snowflake-deployment) - Pocket guide on optimization best practices with Snowflake.
- [How to Deploy dbt to Production using GitHub Actions](https://towardsdatascience.com/how-to-deploy-dbt-to-production-using-github-action-778bf6a1dff6)
- [Doing More With Less: Using DBT to load data from AWS S3 to Snowflake via External Tables](https://medium.com/slateco-blog/doing-more-with-less-usingdbt-to-load-data-from-aws-s3-to-snowflake-via-external-tables-a699d290b93f) - An alternative guide to set up your dbt-external-tables workflow.
- [Best Practices for your dbt Style Guide](https://airbyte.com/content-hub/blog/best-practices-dbt-style-guide) - Standards for well organized base layer with Airbyte ingestion.
- [Tips and Tricks about working with dbt](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287) - Tips from community members.
- [Best Practices for your dbt Style Guide](https://airbyte.com/blog/best-practices-dbt-style-guide?utm_content=bufferd2cd7&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer) - Standards for well organized base layer with Airbyte ingestion.
- [Writing Unit Tests for dbt](https://www.equalexperts.com/blog/our-thinking/writing-unit-tests-for-dbt-with-tdd/) - An overview about the package dbt-unit-testing.
- [How to create Kimball dimensional models with dbt](https://docs.getdbt.com/blog/kimball-dimensional-model) - A step by step guide on how to build Kimball dimensional models with dbt. 

## Integrations

Collection of known data integrations with dbt

- [modal-dbt](https://github.com/trouze/modal-dbt) - This repo gives some code to run dbt jobs/actions using modal which is a serverless application framework.
- [Grai](https://docs.grai.io/integrations/dbt) - Expose warehouse dbt tests in CI to upstream data consumers so production changes never break the warehouse.
- [Datafold](https://docs.datafold.com/os_diff/dbt_integration/) - Gives a quick print out summary of changes so you can move fast and (not) break stuff!
- [Raycast dbt Metadata](https://github.com/b-per/raycast-dbt-cloud-metadata) - Queries the dbt Cloud API to return some useful information about your models (number of tests, time they took to run etc…).
- [Cube](https://cube.dev/blog/dbt-metrics-meet-cube?ref=awesome-dbt) - APIs, Caching, and Access Control on top of dbt Metrics.
- [FlexIt Analytics](https://learn.flexitanalytics.com/docs/dbt/) - Business Intelligence platform with deep dbt Cloud and CLI integration.
- [Raycast dbt Jobs](https://www.raycast.com/zsombor-flds/dbtcloud) - Raycast integration to monitor dbt Cloud Jobs.
- [Metaplane](https://www.metaplane.dev/) - Data Observaibility layer on top of your dbt + BI project.
- [Dbt + Machine Learning: What makes a great baton pass?](https://docs.getdbt.com/blog/maching-learning-dbt-baton-pass) - Landscape of ML utilities around dbt.
- [Soda](https://docs.soda.io/soda/integrate-dbt.html) - Integration of Soda's data observability platform and dbt.
- [Supported Adapters](https://docs.getdbt.com/docs/supported-data-platforms) - Offically supported database adapters.
- [Lightdash](https://github.com/lightdash/lightdash) - Open source Looker alternative with deep dbt integration.
- [Superset](https://superset.apache.org/) - Open source visualization layer for your Modern Data Stack.
- [Dagster and dbt: Better Together](https://dagster.io/blog/dagster-dbt) - Getting started with the dagster-dbt library.
- [fal](https://github.com/fal-ai/fal) - Add multi-language support (Python) to your dbt project.
- [Privacy Dynamics](https://www.privacydynamics.io) - Anonymize data in your dbt project.
- [prefect-dbt](https://github.com/PrefectHQ/prefect-dbt) - Collection of Prefect integrations for working with dbt with your Prefect flows.

## User Stories

Use-cases and user stories implemented by the community members using components of the MDS with dbt.

- [Speeding up the dbt™ docs by 20x with React Server Components](https://dagster.io/blog/dbt-docs-on-react) - A rewrite of dbt docs using Next.js with React Server Components and SSG.
- [How HomeToGo connected dbt and Superset to make metadata more accessible and reduce analytical overhead](https://medium.com/m/global-identity-2?redirectUrl=https%3A%2F%2Fengineering.hometogo.com%2Fhow-hometogo-connected-dbt-and-superset-to-make-metadata-more-accessible-and-reduce-analytical-2223af539cc6) - A dbt<>Superset connector that leverages Superset's API capabilities and dbt's manifest.
- [Self-service Business Intelligence](https://medium.com/modern-business-intelligence/self-service-business-intelligence-powered-by-dbt-3b7e24a92e27) - Eliminate the need for a data modeling semantic layer in BI.
- ["Semantic-free" is the future of Business Intelligence](https://towardsdatascience.com/semantic-free-is-the-future-of-business-intelligence-27aae1d11563) - How to leverage dbt as a data catalog and semantic layer (joins, synonyms, etc.) that BI tools can just plug into.
- [Building an extension framework for dbt](https://medium.com/data-monzo/building-an-extension-framework-for-dbt-654ca99495da) - How Monzo built an extension framework for dbt.
- [Why I moved my dbt workloads to GitHub and saved over $65,000](https://medium.com/@datajuls/why-i-moved-my-dbt-workloads-to-github-and-saved-over-65-000-759b37486001) - Save by replacing dbt Cloud with GitHub Actions.
- [“Is This You?” Entity Matching in the Modern Data Stack with Large Language models](https://towardsdatascience.com/is-this-you-entity-matching-in-the-modern-data-stack-with-large-language-models-19a730373b26) - An experiment in productionizing LLMs.
- [How HomeToGo connected dbt and Superset to make metadata more accessible and reduce analytical overhead](https://engineering.hometogo.com/how-hometogo-connected-dbt-and-superset-to-make-metadata-more-accessible-and-reduce-analytical-2223af539cc6) - A dbt<>Superset connector that leverages Superset's API capabilities and dbt's manifest.
- [Self-service Business Intelligence](https://medium.com/p/3b7e24a92e27) - Eliminate the need for a data modeling semantic layer in BI.
- [Leveraging DBT as a Data Modeling tool](https://medium.com/analytics-and-data/leveraging-dbt-as-a-data-modeling-tool-b3caf78f4a3a) - Reflection on one-year usage of dbt.
- [dbt + Materialize: Streaming to a dbt project near you](https://www.getdbt.com/blog/dbt-materialize-streaming-to-a-dbt-project-near-you) - How to own your real-time transformation workflows like batch-based alternatives.
- [Who's really using dbt?](https://semistructured.substack.com/p/dbt-analytics-engineering-or-data-engineering) - Behind the community of analytics engineers.
- [dbt and the Analytics Engineer — what's the hype about](https://medium.com/validio/dbt-and-the-analytics-engineer-whats-the-hype-about-907eb86c4938) - Behind the upheaval of the analytics engineer profession.
- [Analyzing Fishtown's dbt project performance with artifacts](https://discourse.getdbt.com/t/analyzing-fishtowns-dbt-project-performance-with-artifacts/2214) - Using project artifacts to identify anomalies and room for refactoring.
- [Deploying and Running dbt on Azure Container Instances](https://medium.com/hashmapinc/deploying-and-running-dbt-on-azure-container-instances-f6136f8ea74c) - Demonstration of integration with Azure.
- [Beware of DBT Incremental Updates Against Snowflake External Tables](https://dm03514.medium.com/beware-of-dbt-incremental-updates-against-snowflake-external-tables-beeda513e748) - Things you should be aware of when using external tables with dbt.
- [dbt development at Vimeo](https://medium.com/vimeo-engineering-blog/dbt-development-at-vimeo-fe1ad9eb212) - Best practises from the Vimeo Data team.

## Data Quality

Best-practices and extensions of the testing framework.

- [dq-tools](https://github.com/infinitelambda/dq-tools) - Make simple storing test results and visualisation of these in a BI dashboard leveraging 6 Data Quality KPIs.
- [BigQuery Stale data detection](https://eponkratova.medium.com/stale-data-detection-with-dbt-and-bigquery-dataset-metadata-662196cf9370) - Stale data detection with dbt and BigQuery dataset metadata.
- [PipeRider](https://github.com/InfuseAI/piperider) - PipeRider allows you to define the shape of your data once, and then use the data checking functionality to alert you to changes in your data quality.
- [Elementary](https://github.com/elementary-data/elementary) - A dbt package that provides data anomaly detection as dbt tests.
- [Environment-dependent Unit Testing in dbt](https://medium.com/hiflylabs/environment-dependent-unit-testing-in-dbt-c081a0a5ff1e) - Guide on how to run unit tests in dbt dynamically.
- [dbt-expectations](https://github.com/calogica/dbt-expectations) - Port between dbt and great_expectations to extend out-of-the-box tests.
- [re_data](https://www.getre.io/) - A dbt package for montioring metrics and detect anomalies.
- [How do you test your data](https://discourse.getdbt.com/t/how-do-you-test-your-data/149) - Suggestions on testing your data powered by the community.
- [How to unit test sql transforms in dbt](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/) - Unit test using source defer and generic custom tests.

## CI/CD

Make the best out of your product quality and seamless delivery.

- [How to Create CI/CD Pipelines for dbt Core](https://paulfry999.medium.com/v0-4-pre-chatgpt-how-to-create-ci-cd-pipelines-for-dbt-core-88e68ab506dd) - This post dives into the use of CI/CD for dbt Core, providing insights on dbt Cloud's Slim CI CICD job pattern and how to implement this using dbt Core.
- [Slim CI/CD with Bitbucket Pipelines](https://docs.getdbt.com/blog/slim-ci-cd-with-bitbucket-pipelines) - How to setup slim CI on Bitbucket.
- [dbt-docs-to-notion](https://github.com/marketplace/actions/dbt-docs-to-notion) - A GitHub action for exporting dbt model docs to a Notion database.
- [How to review an analytics pull request]( https://www.getdbt.com/blog/how-to-review-an-analytics-pull-request) - Checkpoints to consider when reviewing an analytics engineer PR.
- [Continuous Integration and Automated Build Testing with dbtCloud](https://blog.rittmananalytics.com/continuous-integration-and-automated-analytics-test-pipelines-using-dbt-and-dbtcloud-c4517f40b874) - Great and detailed blogpost on setting up Slim CI in dbt Cloud.
- [How to review an analytics pull request](https://blog.getdbt.com/how-to-review-an-analytics-pull-request/) - Checkpoints to consider when reviewing an analytics engineer PR.
- [Performing a blue/green deploy of your dbt project on Snowflake](https://discourse.getdbt.com/t/performing-a-blue-green-deploy-of-your-dbt-project-on-snowflake/1349) - A very tidy and fail-safe way to run dbt in production by using two parallel production enviromnents.
- [How we speed up our CI runs by 10x using Slim CI](https://discourse.getdbt.com/t/how-we-sped-up-our-ci-runs-by-10x-using-slim-ci/2603) - Limit data in long-running CI checks to improve developing experience.

## Orchestration

Resources to manage and maintain dependencies in modern data pipelines.

- [Orchestrate dbt Core jobs with Airflow and Cosmos](https://docs.astronomer.io/learn/airflow-dbt) - Run your dbt Core projects as Apache Airflow DAGs and Task Groups.
- [Building a Scalable Analytics Architecture with Airflow and dbt](https://www.astronomer.io/blog/airflow-dbt-1/) - Leveraging the dbt manifest in Airflow.
- [Auto-generating an Airflow DAG using the dbt manifest](https://engineering.autotrader.co.uk/2021/09/15/auto-generated-airflow-dag-for-dbt.html) - Yet another article on extracting value from the manifest file.
- [Building a robust data pipeline with the dAG stack: dbt, Airflow, Great Expectations](https://airflowsummit.org/sessions/2021/building-a-robust-data-pipeline-with-the-dag-stack/) - Demonstration of a data orchestration project with Airflow.
- [Run dbt in Azure Data Factory](https://medium.com/@guangx/run-dbt-in-azure-data-factory-a-clean-solution-for-azure-cloud-edddf0c85849) - Primer about dbt on Azure Data Stack.

## Utilities

Useful tools and extensions to bump up your analytics engineer worklow.

- [dlt(data load tool)](https://dlthub.com/) - The open-source Python library for data loading. 
- [Turntable VSCode extension](https://www.turntable.so/extension) - A handy docs composer and column-level lineage.
- [dbt-loom](https://github.com/nicholasyager/dbt-loom) - A dbt-core plugin to weave together multi-project dbt-core deployments.
- [dbt-meshify](https://github.com/dbt-labs/dbt-meshify) - A dbt-core plugin that automates the management and creation of dbt groups, contracts, access, and versions.
- [dbot](https://github.com/dbt-labs/dbot) - An LLM-powered chatbot with the added context of the dbt knowledge base.
- [dbt-lineagex](https://github.com/sfu-db/dbt-lineagex) - A Column Level Lineage Graph for dbt.
- [Jinjat](https://jinjat.com/) - Low-code application framework that turns your dbt projects into web apps.
- [fst: flow state tool](https://github.com/sungchun12/fst) - A tool to help you stay in flow state while developing dbt models.
- [dbt_tld](https://github.com/GJMcClintock/dbt_tld) - A self-updating dbt library that will maintain a list of current IANA/ICANN recognized top level domains.
- [dbt-model-finder](https://dbt-model-finder.streamlit.app/) - A Streamlit web app to find currently running dbt models.
- [dbtc Explorer](https://dpguthrie-dbtc-streamlit-home-yy7c0b.streamlit.app/Admin_API) - A Streamlit web app to explore the dbt Cloud API.
- [dbt-feature-flags](https://github.com/z3z1ma/dbt-feature-flags) - Feature Flags in dbt models.
- [dbtpal](https://github.com/PedramNavid/dbtpal) - A Neovim plugin for dbt model editing.
- [cookiecutter-dbt](https://github.com/datacoves/cookiecutter-dbt) - Cookiecutter template for dbt projects.
- [turbovault4dbt](https://github.com/ScalefreeCOM/turbovault4dbt) - TurboVault4dbt is an open source tool that automatically generates dbt models according to datavault4dbt-templates.
- [dbtvault-generator](https://github.com/Oracen/dbtvault-generator) - Generate DBT Vault files from yml metadata (supporting `dbtvault` package).
- [dbt-container-skeleton](https://github.com/gnilrets/dbt-container-skeleton) - All the basics to get a nice containerized dbt development environment.
- [oliver-twist](https://github.com/autotraderuk/oliver-twist) - DAG auditing tool that audits the DBT DAG and generates a summary report.
- [dbt-sql-formatter](https://github.com/dbt-labs/dbt-sql-formatter) - Makes your sql less bad.
- [dbterd](https://github.com/datnguye/dbterd) - CLI to generate DBML file from dbt manifest.json.
- [dbt-cue](https://github.com/gilcrest/dbt-cue) - Generate dbt yml files using the CUE language.
- [VSC - Wizard for dbt Core](https://marketplace.visualstudio.com/items?itemName=Fivetran.dbt-language-server) - This extension accelerates your first-time environment setup with dbt Core, and optimizes your continual development of transformation pipelines.
- [dbt-artifacts-parser](https://github.com/yu-iskw/dbt-artifacts-parser) -  It enables us to deal with catalog.json, manifest.json, run-results.json and sources.json as python objects.
- [GitHub Action: Cancel Running CI Job](https://github.com/Stevedow99/dbt-cloud-cancel-running-ci-job-action) -  This allows to always have the newest code commit running in the CI job without having to wait for the stale job runs to finish.
- [dbtc](https://github.com/dpguthrie/dbtc) - Unaffiliated python interface to various dbt Cloud API endpoints.
- [dbt-osmosis](https://github.com/z3z1ma/dbt-osmosis) - Enhance the developer experience significantly with workbench, output diffs, and YAML management.
- [pytest-dbt-core](https://github.com/godatadriven/pytest-dbt-core) - Pytest dbt core is a pytest plugin for testing your dbt projects.
- [looker-gen](https://github.com/aaronbannin/looker-gen) - Generate lookml from dbt.
- [dbtenv](https://github.com/brooklyn-data/dbtenv) - A version manager for dbt.
- [sqlfmt](https://github.com/tconbeer/sqlfmt) - This tool formats your dbt SQL code so you don't have to.
- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - SQL linter that supports dbt and Jinja templating.
- [Build Data Access Layer on dbt](https://github.com/coterahq/dal) - Package to build GraphQL API on top of your dbt project.
- [Run changed models based on Git status](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287/2) - Handy bash function to run changed models since last commit.
- [How we set up our computers for working on dbt projects](https://discourse.getdbt.com/t/how-we-set-up-our-computers-for-working-on-dbt-projects/243) - Things I wish I would have known when started working with dbt. Tools and hacks to improve developing experience.
- [fzf-dbt](https://github.com/Infused-Insight/fzf-dbt) - Search dbt models interactively from terminal.
- [vscode-dbt-power-user](https://github.com/innoverio/vscode-dbt-power-user) - VSCode extension to give more clarity on model dependencies.
- [Your Essential dbt Project Checklist](https://discourse.getdbt.com/t/your-dbt-project-checklist/1377) - Checklist on items necessary for a successful dbt project.
- [dbt Style Guide](https://github.com/dbt-labs/corp/blob/main/dbt_style_guide.md) - Developing styleguide often referred in PR templates.
- [Clean your warehouse of old and deprecated models](https://discourse.getdbt.com/t/clean-your-warehouse-of-old-and-deprecated-models/1547) - Clean out warehouse models which are not existent in the project.
- [dbt-tips](https://github.com/erika-e/dbt-tips) - Excellent companion to your dbt practice with rich collection of tips.
- [dbt-tags](https://yu-ishikawa.medium.com/understanding-the-scopes-of-dbt-tags-691d0286f3aa) - Understanding the scopes of dbt tags.
- [Pre-commit hooks](https://github.com/dbt-checkpoint/dbt-checkpoint) - Pre-commit hooks for checking data integity before schema change commit.

## Packages

Community-developed packages to extend default macros and toolset.

- [dbt-fake](https://github.com/leogodin217/dbt-fake) - Daily updated fake data for dbt learning and projects.
- [dbt_cloud_run_cost](https://github.com/danthelion/dbt_cloud_run_cost) - Package to calculate dbt Cloud usage-based cost.
- [dbt-reconfigured](https://github.com/TheGrowthEngineeringCompany/dbt-reconfigured) - A dbt package containing reconfigured macros.
- [dbt-census-utils](https://github.com/sutrolabs/dbt_census_utils) - A collection of dbt macros for working with Census data.
- [dbt-fabric](https://github.com/datarootsio/dbt-fabric) - A dbt adapter for working with Microsoft Fabric Data Warehouses.
- [dq-vault](https://github.com/infinitelambda/dq-vault) - Data Quality Observation of Data Vault layer.
- [dbt-translate](https://github.com/datnguye/dbt-translate) - Translate numbers into words.
- [dbt-excel](https://dbt-excel.com/) - A dbt adapter for working with Excel.
- [dbt_linreg](https://github.com/dwreeves/dbt_linreg) - Linear regression in SQL using dbt.
- [dbt-snowflake-query-tags](https://github.com/get-select/dbt-snowflake-query-tags) - Automatically tag dbt-issued queries with informative metadata.
- [snowflake-resource-monitoring](https://github.com/dbt-labs/snowflake-resource-monitoring) - Yet another package to monitor Snowflake usage.
- [usagedata](https://github.com/anjane-tech/usagedata) - Provides insights on the database/table level usage informations from Snowflake.
- [dbt_ml](https://github.com/kristeligt-dagblad/dbt_ml) - Package for dbt that allows users to train, audit and use BigQuery ML models.
- [ddbt](https://github.com/monzo/ddbt) - This repo represents my attempt to build a fast version of DBT which gets very slow on large projects (3000+ data models). This project attempts to be a direct drop in replacement for DBT at the command line.
- [dbt-snowflake-monitoring](https://github.com/get-select/dbt-snowflake-monitoring) - A dbt package to help you monitor Snowflake performance and costs.
- [datavault4dbt](https://github.com/ScalefreeCOM/datavault4dbt) - Macros for staging and creation of all DataVault-Entities you need, to build your own DataVault2.0 solution.
- [DDO](https://github.com/marco-roy/DDO) - Perform DataOps & administrative CI/CD on your data warehouse.
- [dbt-yaml-check](https://github.com/aranke-archive/dbt-yaml-check) - Checks that columns defined in YAML also exist in SQL.
- [data-diff](https://github.com/datafold/data-diff) - A command-line tool and Python library to efficiently diff rows across two different databases.
- [dbt-project-evaluator](https://github.com/dbt-labs/dbt-project-evaluator) - This package highlights areas of a dbt project that are misaligned with dbt Labs' best practices.
- [dbt_constraints](https://github.com/Snowflake-Labs/dbt_constraints) - Generate database constraints based on the tests in a dbt project.
- [dbt-date](https://github.com/calogica/dbt-date) - Date logic and calendar functionality.
- [dbt-privacy](https://github.com/pvcy/dbt-privacy) - Macros to make it easier to protect your customers' data.
- [dbt-fivetran-utils](https://github.com/fivetran/dbt_fivetran_utils) - General macros and helpers.
- [dbt_metrics](https://github.com/dbt-labs/dbt_metrics) - Macros to support secondary calculations and generate business metrics.
- [dbt-metabase](https://github.com/gouline/dbt-metabase) - Model synchronization from dbt to Metabase.
- [dbt-coves](https://pypi.org/project/dbt-coves/) - CLI tool for generating a scaffold for your dbt project.
- [dbt-profiler](https://hub.getdbt.com/data-mie/dbt_profiler/latest/) - Data profiling and doc block generator.
- [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) - General macros library. A must have.
- [dbt_audit_helper](https://github.com/dbt-labs/dbt-audit-helper/) - Macros for data audits that compare columns values and schemas between tables.
- [dbt-ml-preprocessing](https://github.com/omnata-labs/dbt-ml-preprocessing) - A SQL port of python's scikit-learn preprocessing module, provided as cross-database dbt macros.
- [dbt-external-tables](https://github.com/dbt-labs/dbt-external-tables) - Macros to stage your external sources.
- [dbt-feature-store](https://github.com/fal-ai/dbt_feature_store) - Macros to build a feature store right within your dbt project.
- [dbt-codegen](https://github.com/dbt-labs/dbt-codegen) - Macros that generate dbt code, and log it to the command line.
- [dbt-init](https://github.com/dbt-labs/dbt-init) - Create a project and populate as much of the dbt project as possible.
- [dbt-artifacts](https://github.com/brooklyn-data/dbt_artifacts ) - This package builds a mart of tables from dbt artifacts loaded into a table.
- [dbt-erdiagram-generator](https://github.com/intellishore/dbt-erdiagram-generator) - This packages generate ERD diagrams from a dbt project.
- [Terraform-dbt Cloud Module](https://github.com/GtheSheep/terraform-provider-dbt-cloud) - IAC in dbt Cloud via Terraform.
- [dbt2looker](https://github.com/lightdash/dbt2looker) - Generate Looker views for dbt models.
- [dbt-coverage](https://github.com/slidoapp/dbt-coverage) - Checks dbt docs and tests coverage.
- [dbt-meta-testing](https://github.com/tnightengale/dbt-meta-testing) - Yet another coverage testing.
- [dbt-superset-lineage](https://github.com/slidoapp/dbt-superset-lineage) - Push and pull metadata between dbt to Superset.
- [dbtvault](https://dbtvault.readthedocs.io/en/latest/) - Package for generating and executing ETL for Data Vault 2.0.
- [dbt-invoke](https://github.com/Dashlane/dbt-invoke) - CLI for creating, updating, and deleting dbt property files.
- [dbt-unit-testing](https://github.com/EqualExperts/dbt-unit-testing) -  Package which contains macros to support unit testing.


## Community

Conferences, meetups, dicussions, newsletters, podcasts, etc. led by fellow analytics engineers and forums of contact.

- [Data Council Austin 2023](https://www.youtube.com/playlist?list=PLAesBe-zAQmF-GpvZ3ba5YpVzoVbgzl8M) - A conference for data teams.
- [State of Analytics Engineering 2023](https://www.getdbt.com/state-of-analytics-engineering-2023?mn=gWlJaysu_LpdqLTox0JXl6LHyaPHE5lKxcKh.yF0aSpyD38bsL9D9) - A survey of pains, gains, and areas of investment for global data teams.
- [dbt Labs Tiktok](https://www.tiktok.com/@dbtlabs) - Official TikTok channel of dbt Labs.
- [Locally Optimistic](https://locallyoptimistic.com/about/) - A Slack community of aspiring analytics leaders discussing and sharing lessons learned and challenges from their experiences in using data.
- [DataTalks.Club](https://datatalks.club/) - Global online community of data enthusiasts. Podcasts and blogs, etc. are distributed with high frequency.
- [Metadata Weekly](https://metadataweekly.substack.com) - Weekly substack about metadata, the metrics layer and MDS.
- [Data & Analytics Events in 2022](https://atlanhq.notion.site/atlanhq/Data-Analytics-Events-in-2022-7abf9f3daf8d42358234c6a00b43f1a6) - Great curated list of upcoming data analytics conferences.
- [Data Council Austin 2022](https://www.youtube.com/playlist?list=PLAesBe-zAQmEod2ARZjjAHmGFoGcjaXK6) - Worldwide community driven analytics conference with a handful of talks fitting to the dbt stack.
- [Discourse v2](https://github.com/dbt-labs/docs.getdbt.com/discussions) - Revamped and ported hub of main discussions for the community.
- [Coalesce 2021](https://www.youtube.com/playlist?list=PL0QYlrC86xQnNXXXL7WPRTULbMgh_Sry3) - Second iteration of the analytics engineer conference.
- [Coalesce 2020](https://www.youtube.com/playlist?list=PL0QYlrC86xQmPf9QUceFdOarYcv3ETSsz) - Annual dbt conference full of fascinating use-cases.
- [dbt meetups](https://www.meetup.com/en-AU/pro/dbt/) - List of community led dbt meetups.
- [Analytics Engineer Roundup](https://roundup.getdbt.com/) - Official dbt Labs newsletter on topics of the MDS.
- [Benn Stacil's Newsletter](https://benn.substack.com/) - Tought-provoking reads from founder of Mode.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Weekly newsletter of recent trends in Data Engineering.
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - One of the most popular data engineering podcasts covering great concepts and new products.
- [Analyitics Engineer Podcast](https://podcasts.apple.com/us/podcast/the-analytics-engineering-podcast/id1574755368) - Official podcast of dbt Labs.
- [dbt Slack](https://www.getdbt.com/community) - Energy-filled hub of analytics engineers (Highly recommended).
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - Subreddit of data engineering topics.
- [Drill to Detail Podcast](https://www.rittmananalytics.com/drilltodetail) - Special guests discussing big data, business intelligence, modern data stack.

## Sample Projects

Sample projects which work out-of-the box. Reflect use-cases publicly available.

- [awesome-public-dbt-projects](https://github.com/InfuseAI/awesome-public-dbt-projects) - A curated list of awesome public dbt projects.
- [mdsinabox](https://github.com/matsonj/mdsinabox) - MDS in a box deployed anywhere.
- [gee_production_gatekeepers](https://github.com/nszoni/gee_production_gatekeepers) - A demonstration of production gatekeepers in Snowflake and BigQuery.
- [dbt-beyond-the-basics](https://github.com/pgoslatara/dbt-beyond-the-basics) - A repository demonstrating advanced use cases of dbt in multiple areas.
- [mdsfest-opensource-mds](https://github.com/dagster-io/mdsfest-opensource-mds) - Demo project for open source MDS.
- [f1-data-pipeline](https://github.com/InosRahul/f1-data-pipeline) - F1 Data Pipeline.
- [transfermarkt-datasets](https://github.com/dcaribou/transfermarkt-datasets) - E2E dbt project for scraping and transforming football data from Transfermarkt.
- [dbt_github_archive_bigquery](https://github.com/preset-io/dbt_github_archive_bigquery) - A dbt project for GitHub Archive data on BigQuery.
- [dbt_workspace](https://github.com/randypitcherii/dbt_workspace) - A workspace template for dbt demos.
- [Cloud Cost Monitoring](https://github.com/randypitcherii/cloud_cost_monitoring) - A dbt project to monitor cloud costs.
- [Analytics Engineer Survey 2023](https://github.com/dbt-labs/analytics-engineering-survey/tree/main) - Repo containing data and dbt template of the survey.
- [Tracking the Fake GitHub Star Black Market with Dagster, dbt and BigQuery](https://dagster.io/blog/fake-stars) - Explore the topic of fake GitHub stars.
- [Data-aware orchestration](https://github.com/jonathanneo/data-aware-orchestration) - Dagster's ability to create a global dependency graph between different dbt projects.
- [GitLab Data Team](https://gitlab.com/gitlab-data/analytics/-/tree/master/transform/snowflake-dbt) - Gitlab's open source dbt project.
- [attribution-playbook](https://github.com/dbt-labs/attribution-playbook) - A worked example to demonstrate how to model customer attribution.
- [mrr-playbook](https://github.com/dbt-labs/mrr-playbook) - A worked example to demonstrate how to model subscription revenue.
- [Use dbt inside Visual Studio Code development containers](https://github.com/davidgasquez/dbt-devcontainer) - Set up your dbt environment with pre-installed extensions.
- [dag-stack](https://github.com/spbail/dag-stack) - Dbt-Airflow-GreatExpectations Stack.
- [Jaffle Shop](https://github.com/dbt-labs/jaffle_shop) - A self-contained dbt project for testing purposes.
- [Spotify User Analytics](https://github.com/ftupas/dbt-spotify-analytics) - Sample dbt project with Spotify user data.
- [dbt-github-workflow](https://github.com/slve/dbt-github-workflow) - Deploy BigQuery + Airflow.
- [airflow-dbt-demo](https://github.com/astronomer/airflow-dbt-demo) - Demonstration of Airflow integration.
- [aws athena x dbt](https://kiwamizamurai.github.io/posts/2022-08-25/) - How to build a small and modern data infrastructure.
- dbt on AWS ![image](https://user-images.githubusercontent.com/1023748/206618801-52fb35ab-bcb3-4ba5-9986-23498f03f70c.png) - Data Build Tool (dbt) for Effective Data Transformation on AWS
  - [Part 1 – Redshift](https://jaehyeon.me/blog/2022-09-28-dbt-on-aws-part-1-redshift/)
  - [Part 2 – Glue](https://jaehyeon.me/blog/2022-10-09-dbt-on-aws-part-2-glue/)
  - [Part 3 – EMR on EC2](https://jaehyeon.me/blog/2022-10-19-dbt-on-aws-part-3-emr-ec2/)
  - [Part 4 – EMR on EKS](https://jaehyeon.me/blog/2022-11-01-dbt-on-aws-part-4-emr-eks/)
  - [Part 5 – Athena](https://jaehyeon.me/blog/2022-12-06-dbt-on-aws-part-5-athena/)

## Contributors

Thanks for all the great resources! Can't see your avatar? Check the contribution guide on how you can submit your resources to the community!

<a href="https://github.com/Hiflylabs/awesome-dbt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Hiflylabs/awesome-dbt" />
</a>
