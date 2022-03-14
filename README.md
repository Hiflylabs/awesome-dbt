<!--lint disable awesome-heading-->
# Awesome dbt [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Hiflylabs/awesome-dbt"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Hiflylabs/awesome-dbt">

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

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - Data engineering course on cutting edge tools including dbt.
- [Analytics Engineering with dbt](https://corise.com/course/analytics-engineering-with-dbt) - Paid course offered by co:rise covering the basics of dbt.
- [dbt Fundamentals](https://courses.getdbt.com/collections) - Official free course offered by dbt. Excellent for learning the basics of dbt Cloud.
- [Refactoring SQL for Modularity](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) - Another dbt labs offered free course on dbt refactoring and CTE supercharging.
- [Learn DBT from Scratch](https://www.udemy.com/course/learn-dbt-from-scratch/) - Guides you through a setup paired with Snowflake (decorated with extras).

## How To

Helping hand on setting up integrations and implementing best practices.

- [How we structure our dbt projects](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355) - How the dbt team structures its dbt projects. 
- [dbt guide](https://about.gitlab.com/handbook/business-technology/data-team/platform/dbt-guide/) - Primer on how you should properly set up and configure your dbt workflow.
- [dbt for Data Transformation – Hands-on](https://www.kdnuggets.com/2021/07/dbt-data-transformation-tutorial.html) - Yet another tutorial for using dbt Cloud.
- [Start Modeling Data](https://dataschool.com/sql-optimization/start-modeling-data/) - Configuring Bigquery with your dbt project.
- [Accelerating Data Teams with dbt & Snowflake](https://quickstarts.snowflake.com/guide/data_engineering_with_dbt/index.html?index=..%2F..index#0) - A dbt & Snowflake workshop on financial data.
- [Creating a dev environment quickly on Snowflake](https://discourse.getdbt.com/t/creating-a-dev-environment-quickly-on-snowflake/1151) - Setting up teh integraton with Snowflake.
- [How to set up a dbt data-ops workflow, using dbt cloud and Snowflake](https://www.startdataengineering.com/post/cicd-dbt/) - Leverage GitHub Actions to set up CI/CD with dbt Core.
- [How to configure your dbt repository](https://discourse.getdbt.com/t/how-to-configure-your-dbt-repository-one-or-many/2121) - Mono-repo or not mono-repo?
- [Best Practices for Optimizing Your dbt and Snowflake Deployment](https://resources.snowflake.com/white-paper/best-practices-for-optimizing-your-dbt-and-snowflake-deployment) - Pocket guide on optimization best practices with Snowflake.
- [How to Deploy dbt to Production using GitHub Actions](https://towardsdatascience.com/how-to-deploy-dbt-to-production-using-github-action-778bf6a1dff6)
- [Doing More With Less: Using DBT to load data from AWS S3 to Snowflake via External Tables](https://medium.com/slateco-blog/doing-more-with-less-usingdbt-to-load-data-from-aws-s3-to-snowflake-via-external-tables-a699d290b93f) - An alternative guide to set up your dbt-external-tables workflow.
- [Best Practices for your dbt Style Guide](https://airbyte.com/blog/best-practices-dbt-style-guide?utm_content=bufferd2cd7&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer) - Standards for well organized base layer with Airbyte ingestion.
- [Tips and Tricks about working with dbt](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287) - Tips from community members. 
- [Writing Unit Tests for dbt](https://www.equalexperts.com/blog/our-thinking/writing-unit-tests-for-dbt-with-tdd/) - An overview about the package dbt-unit-testing.
## Integrations

Collection of known data integrations with dbt

- [Model synchronization from dbt to Metabase.](https://github.com/gouline/dbt-metabase)
- [Soda](https://docs.soda.io/soda/integrate-dbt.html) - Integration of Soda's data observability platform and dbt.
- [Supported Adapters](https://docs.getdbt.com/docs/available-adapters) - Offically supported database adapters.
- [Lightdash](https://github.com/lightdash/lightdash) - Open source Looker alternative with deep dbt integration.
- [Superset](https://superset.apache.org/) - Open source visualization layer for your Modern Data Stack.
- [Dagster and dbt: Better Together](https://dagster.io/blog/dagster-dbt) - Getting started with the dagster-dbt library.
- [fal](https://github.com/fal-ai/fal) - Add multi-language support (Python) to your dbt project.

## User Stories

Use-cases and user stories implemented by the community members using components of the MDS with dbt.

- [Leveraging DBT as a Data Modeling tool](https://medium.com/analytics-and-data/leveraging-dbt-as-a-data-modeling-tool-b3caf78f4a3a) - Reflection on one-year usage of dbt.
- [dbt + Materialize: Streaming to a dbt project near you](https://blog.getdbt.com/dbt-materialize-streaming-to-a-dbt-project-near-you/) - How to own your real-time transformation workflows like batch-based alternatives.
- [Who's really using dbt?](https://semistructured.substack.com/p/dbt-analytics-engineering-or-data-engineering) - Behind the community of analytics engineers.
- [dbt and the Analytics Engineer — what's the hype about](https://medium.com/validio/dbt-and-the-analytics-engineer-whats-the-hype-about-907eb86c4938) - Behind the upheaval of the analytics engineer profession.
- [Analyzing Fishtown's dbt project performance with artifacts](https://discourse.getdbt.com/t/analyzing-fishtowns-dbt-project-performance-with-artifacts/2214) - Using project artifacts to identify anomalies and room for refactoring.
- [Deploying and Running dbt on Azure Container Instances](https://medium.com/hashmapinc/deploying-and-running-dbt-on-azure-container-instances-f6136f8ea74c) - Demonstration of integration with Azure.
- [Beware of DBT Incremental Updates Against Snowflake External Tables](https://dm03514.medium.com/beware-of-dbt-incremental-updates-against-snowflake-external-tables-beeda513e748) - Things you should be aware of when using external tables with dbt.
- [dbt development at Vimeo](https://medium.com/vimeo-engineering-blog/dbt-development-at-vimeo-fe1ad9eb212) - Best practises from the Vimeo Data team.
## Data Quality

Best-practices and extensions of the testing framework.

- [Environment-dependent Unit Testing in dbt](https://medium.com/codex/environment-dependent-unit-testing-in-dbt-c081a0a5ff1e) - Guide on how to run unit tests in dbt dynamically.
- [dbt-expectations](https://github.com/calogica/dbt-expectations) - Port between dbt and great_expectations to extend out-of-the-box tests.
- [re_data](https://www.getre.io/) - A dbt package for montioring metrics and detect anomalies.
- [How do you test your data](https://discourse.getdbt.com/t/how-do-you-test-your-data/149) - Suggestions on testing your data powered by the community.
- [How to unit test sql transforms in dbt](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/) - Unit test using source defer and generic custom tests.

## CI/CD

Make the best out of your product quality and seamless delivery.

- [Anatomy of A Pipeline: CI/CD For a dbt Data Warehouse on Google Big Query Using Azure Pipelines](https://analysis.backhand.tech/Data-Ops/ci-cd-for-dbt-big-query-on-azure) - Setting up CI/CD for a Big Query Stack using Azure Pipelines.
- [Continuous Integration and Automated Build Testing with dbtCloud](https://rittmananalytics.com/blog/2019/6/11/continuous-integration-feature-branches-and-automated-build-tests-using-dbtcloud) - Great and detailed blogpost on setting up Slim CI in dbt Cloud.
- [How to review an analytics pull request](https://blog.getdbt.com/how-to-review-an-analytics-pull-request/) - Checkpoints to consider when reviewing an analytics engineer PR.
- [Performing a blue/green deploy of your dbt project on Snowflake](https://discourse.getdbt.com/t/performing-a-blue-green-deploy-of-your-dbt-project-on-snowflake/1349) - A very tidy and fail-safe way to run dbt in production by using two parallel production enviromnents.
- [How we speed up our CI runs by 10x using Slim CI](https://discourse.getdbt.com/t/how-we-sped-up-our-ci-runs-by-10x-using-slim-ci/2603) - Limit data in long-running CI checks to improve developing experience.

## Orchestration

Resources to manage and maintain dependencies in modern data pipelines.

- [Building a Scalable Analytics Architecture with Airflow and dbt](https://www.astronomer.io/blog/airflow-dbt-1) - Leveraging the dbt manifest in Airflow.
- [Auto-generating an Airflow DAG using the dbt manifest](https://engineering.autotrader.co.uk/2021/09/15/auto-generated-airflow-dag-for-dbt.html) - Yet another article on extracting value from the manifest file.
- [Building a robust data pipeline with the dAG stack: dbt, Airflow, Great Expectations](https://airflowsummit.org/sessions/2021/building-a-robust-data-pipeline-with-the-dag-stack/) - Demonstration of a data orchestration project with Airflow.
- [Run dbt in Azure Data Factory](https://medium.com/@guangx/run-dbt-in-azure-data-factory-a-clean-solution-for-azure-cloud-edddf0c85849) - Primer about dbt on Azure Data Stack.
## Utilities

Useful tools and extensions to bump up your analytics engineer worklow.

- [Run changed models based on Git status](https://discourse.getdbt.com/t/tips-and-tricks-about-working-with-dbt/287/2) - Handy bash function to run changed models since last commit.
- [How we set up our computers for working on dbt projects](https://discourse.getdbt.com/t/how-we-set-up-our-computers-for-working-on-dbt-projects/243) - Things I wish I would have known when started working with dbt. Tools and hacks to improve developing experience.
- [fzf-dbt](https://github.com/Infused-Insight/fzf-dbt) - Search dbt models interactively from terminal.
- [vscode-dbt-power-user](https://github.com/innoverio/vscode-dbt-power-user) - VSCode extension to give more clarity on model dependencies.
- [Your Essential dbt Project Checklist](https://discourse.getdbt.com/t/your-essential-dbt-project-checklist/1377) - Checklist on items necessary for a successful dbt project.
- [dbt Style Guide](https://github.com/dbt-labs/corp/blob/master/dbt_style_guide.md) - Developing styleguide often referred in PR templates.
- [Clean your warehouse of old and deprecated models](https://discourse.getdbt.com/t/clean-your-warehouse-of-old-and-deprecated-models-snowflake/1547) - Clean out warehouse models which are not existent in the project.
- [dbt-tips](https://github.com/erika-e/dbt-tips) - Excellent companion to your dbt practice with rich collection of tips.
- [dbt-tags](https://link.medium.com/l33DGL9sFlb) - Understanding the scopes of dbt tags.
- [Pre-commit hooks](https://github.com/offbi/pre-commit-dbt) - Pre-commit hooks for checking data integity before schema change commit.

## Packages

Community-developed packages to extend default macros and toolset.

- [dbt-coves](https://pypi.org/project/dbt-coves/) - CLI tool for generating a scaffold for your dbt project.
- [dbt-profiler](https://hub.getdbt.com/data-mie/dbt_profiler/latest/) - Data profiling and doc block generator.
- [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) - General macros library. A must have.
- [dbt_audit_helper](https://github.com/dbt-labs/dbt-audit-helper/) - Macros for data audits that compare columns values and schemas between tables.
- [dbt-ml-preprocessing](https://github.com/omnata-labs/dbt-ml-preprocessing) - A SQL port of python's scikit-learn preprocessing module, provided as cross-database dbt macros.
- [dbt-external-tables](https://github.com/dbt-labs/dbt-external-tables) - Macros to stage your external sources.
- [dbt-feature-store](https://github.com/fal-ai/dbt_feature_store) - Macros to build a feature store right within your dbt project.
- [dbt-codegen](https://github.com/dbt-labs/dbt-codegen) - Macros that generate dbt code, and log it to the command line.
- [dbt-init](https://github.com/dbt-labs/dbt-init) - Create a project and populate as much of the dbt project as possible.
- [dbt-artifacts](https://github.com/tailsdotcom/dbt_artifacts) - This package builds a mart of tables from dbt artifacts loaded into a table.
- [dbt-erdiagram-generator](https://github.com/intellishore/dbt-erdiagram-generator) - This packages generate ERD diagrams from a dbt project.
- [Terraform-dbt Cloud Module](https://github.com/GtheSheep/terraform-provider-dbt-cloud) - IAC in dbt Cloud via Terraform.
- [dbt2looker](https://github.com/lightdash/dbt2looker) - Generate Looker views for dbt models.
- [dbt-coverage](https://github.com/slidoapp/dbt-coverage) - Checks dbt docs and tests coverage.
- [dbt-meta-testing](https://github.com/tnightengale/dbt-meta-testing) - Yet another coverage testing.
- [dbt-superset-lineage](https://github.com/slidoapp/dbt-superset-lineage) - Push and pull metadata between dbt to Superset.
- [dbtvault](https://dbtvault.readthedocs.io/en/latest/) - Package for generating and executing ETL for Data Vault 2.0 on Snowflake.
- [dbt-invoke](https://github.com/Dashlane/dbt-invoke) - CLI for creating, updating, and deleting dbt property files.
- [dbt-unit-testing](https://github.com/EqualExperts/dbt-unit-testing) -  Package which contains macros to support unit testing.

## Community

Conferences, meetups, dicussions, newsletters, podcasts, etc. led by fellow analytics engineers and forums of contact.

- [Coalesce 2021](https://youtube.com/playlist?list=PL0QYlrC86xQnNXXXL7WPRTULbMgh_Sry3) - Second iteration of the analytics engineer conference.
- [Coalesce 2020](https://youtube.com/playlist?list=PL0QYlrC86xQmPf9QUceFdOarYcv3ETSsz) - Annual dbt conference full of fascinating use-cases.
- [dbt meetups](https://www.meetup.com/en-AU/pro/dbt/) - List of community led dbt meetups.
- [Analytics Engineer Roundup](https://roundup.getdbt.com/) - Official dbt Labs newsletter on topics of the MDS.
- [Benn Stacil's Newsletter](https://benn.substack.com/) - Tought-provoking reads from founder of Mode.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Weekly newsletter of recent trends in Data Engineering.
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - One of the most popular data engineering podcasts covering great concepts and new products.
- [Analyitics Engineer Podcast](https://podcasts.apple.com/us/podcast/the-analytics-engineering-podcast/id1574755368) - Official podcast of dbt Labs.
- [dbt Slack](https://www.getdbt.com/community/) - Energy-filled hub of analytics engineers (Highly recommended).
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - Subreddit of data engineering topics.
- [Drill to Detail Podcast](https://rittmananalytics.com/drilltodetail) - Special guests discussing big data, business intelligence, modern data stack.

## Sample Projects

Sample projects which work out-of-the box. Reflect use-cases publicly available.

- [dag-stack](https://github.com/spbail/dag-stack) - Dbt-Airflow-GreatExpectations Stack.
- [Jaffle Shop](https://github.com/dbt-labs/jaffle_shop) - A self-contained dbt project for testing purposes.
- [Spotify User Analytics](https://github.com/ftupas/dbt-spotify-analytics) - Sample dbt project with Spotify user data.
- [dbt-github-workflow](https://github.com/slve/dbt-github-workflow) - Deploy BigQuery + Airflow.
- [airflow-dbt-demo](https://github.com/astronomer/airflow-dbt-demo) - Demonstration of Airflow integration.

## Contributors

Thanks for all the great resources! Can't see your avatar? Check the contribution guide on how you can submit your resources to the community!

<a href="https://github.com/Hiflylabs/awesome-dbt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Hiflylabs/awesome-dbt" />
</a>

