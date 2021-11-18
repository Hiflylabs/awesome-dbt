# Awesome dbt [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome dbt resources 

### Learning

- [Leveraging DBT as a Data Modeling tool](https://medium.com/analytics-and-data/leveraging-dbt-as-a-data-modeling-tool-b3caf78f4a3a) - Reflection on one-year usage of dbt.
- [dbt guide](https://about.gitlab.com/handbook/business-technology/data-team/platform/dbt-guide/) - Primer on how you should properly set up and configure your dbt workflow
- [dbt Fundamentals](https://courses.getdbt.com/collections) - Official free course offered by dbt. Excellent for learning the basics of dbt Cloud.
- [Learn DBT from Scratch](https://www.udemy.com/course/learn-dbt-from-scratch/) - Guides you through a setup paired with Snowflake (decorated with extras)
- [Your Essential dbt Project Checklist](https://discourse.getdbt.com/t/your-essential-dbt-project-checklist/1377)
- [dbt for Data Transformation – Hands-on ](https://www.kdnuggets.com/2021/07/dbt-data-transformation-tutorial.html) Yet another tutorial for using dbt Cloud
- [Start Modeling Data](https://dataschool.com/sql-optimization/start-modeling-data/) - Configuring Bigquery with your dbt project
- [Accelerating Data Teams with dbt & Snowflake](https://quickstarts.snowflake.com/guide/data_engineering_with_dbt/index.html?index=..%2F..index#0) - dbt & Snowflake workshop on financial data
- [Refactoring SQL for Modularity](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) - Another dbt labs offered free course on dbt refactoring and CTE supercharging

### Resources

- [dbt + Materialize: Streaming to a dbt project near you](https://blog.getdbt.com/dbt-materialize-streaming-to-a-dbt-project-near-you/) - How to own your real-time transformation workflows like batch-based alternatives.
- [Who's really using dbt?](https://semistructured.substack.com/p/dbt-analytics-engineering-or-data-engineering)
- [dbt and the Analytics Engineer — what’s the hype about](https://medium.com/validio/dbt-and-the-analytics-engineer-whats-the-hype-about-907eb86c4938)
- [dbtvault](https://dbtvault.readthedocs.io/en/latest/) - Package for generating and executing ETL for Data Vault 2.0 on Snowflake
- [dbt-tips](https://github.com/erika-e/dbt-tips) - Excellent companion to your dbt practice with rich collection of tips


### Orchestration

- [Building a Scalable Analytics Architecture with Airflow and dbt](https://www.astronomer.io/blog/airflow-dbt-1) - Leveraging the dbt manifest in Airflow
- [Auto-generating an Airflow DAG using the dbt manifest](https://engineering.autotrader.co.uk/2021/09/15/auto-generated-airflow-dag-for-dbt.html)
- [Dagster and dbt: Better Together](https://dagster.io/blog/dagster-dbt) - Getting started with the dagster-dbt library
- [Building a robust data pipeline with the dAG stack: dbt, Airflow, Great Expectations](https://airflowsummit.org/sessions/2021/building-a-robust-data-pipeline-with-the-dag-stack/)

### Deployment

- [How to set up a dbt data-ops workflow, using dbt cloud and Snowflake](https://www.startdataengineering.com/post/cicd-dbt/)
- [How to configure your dbt repository](https://discourse.getdbt.com/t/how-to-configure-your-dbt-repository-one-or-many/2121) - Mono-repo or not mono-repo?
- [Anatomy of A Pipeline: CI/CD For a dbt Data Warehouse on Google Big Query Using Azure Pipelines](https://analysis.backhand.tech/Data-Ops/ci-cd-for-dbt-big-query-on-azure)
- [How to Deploy dbt to Production using GitHub Actions](https://towardsdatascience.com/how-to-deploy-dbt-to-production-using-github-action-778bf6a1dff6)
- [Deploying and Running dbt on Azure Container Instances](https://medium.com/hashmapinc/deploying-and-running-dbt-on-azure-container-instances-f6136f8ea74c)
- [Continuous Integration and Automated Build Testing with dbtCloud](https://rittmananalytics.com/blog/2019/6/11/continuous-integration-feature-branches-and-automated-build-tests-using-dbtcloud)
- [Best Practices for Optimizing Your dbt and Snowflake Deployment](https://resources.snowflake.com/white-paper/best-practices-for-optimizing-your-dbt-and-snowflake-deployment)
- [How to review an analytics pull request](https://blog.getdbt.com/how-to-review-an-analytics-pull-request/)
- [Best Practices for Optimizing Your dbt and Snowflake Deployment](https://resources.snowflake.com/white-paper/best-practices-for-optimizing-your-dbt-and-snowflake-deployment)
- [Performing a blue/green deploy of your dbt project on Snowflake](https://discourse.getdbt.com/t/performing-a-blue-green-deploy-of-your-dbt-project-on-snowflake/1349) - A very tidy way to run dbt in production
- [How we sped up our CI runs by 10x using Slim CI](https://discourse.getdbt.com/t/how-we-sped-up-our-ci-runs-by-10x-using-slim-ci/2603)
- [Beware of DBT Incremental Updates Against Snowflake External Tables](https://dm03514.medium.com/beware-of-dbt-incremental-updates-against-snowflake-external-tables-beeda513e748) - Things you should be aware of when using external tables with dbt
- [Doing More With Less: Using DBT to load data from AWS S3 to Snowflake via External Tables](https://medium.com/slateco-blog/doing-more-with-less-usingdbt-to-load-data-from-aws-s3-to-snowflake-via-external-tables-a699d290b93f) - An alternative guide to set up your dbt-external-tables workflow

## Tools

- [vscode-dbt-power-user](https://github.com/innoverio/vscode-dbt-power-user)
- [How we set up our computers for working on dbt projects](https://discourse.getdbt.com/t/how-we-set-up-our-computers-for-working-on-dbt-projects/243)

### Testing

- [dbt-expectations](https://github.com/calogica/dbt-expectations) - Port between dbt and great_expectations to extend out-of-the-box tests.
- [re_data](https://www.getre.io/) - dbt package for montioring metrics and detect anomalies.
- [How do you test your data](https://discourse.getdbt.com/t/how-do-you-test-your-data/149) - Suggestions on testing your data powered by the community
- [How to unit test sql transforms in dbt](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/)

### Packages

- [dbt-coves](https://pypi.org/project/dbt-coves/) - CLI tool for generating a scaffold for your dbt project
- [dbt-profiler](https://hub.getdbt.com/data-mie/dbt_profiler/latest/) - data profiling and doc block generator 
- [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) - General macros library. A must have.
- [dbt_audit_helper](https://github.com/dbt-labs/dbt-audit-helper/) - Macros for data audits that compare columns values and schemas between tables
- [dbt-ml-preprocessing](https://github.com/omnata-labs/dbt-ml-preprocessing)
- [dbt-external-tables](https://github.com/dbt-labs/dbt-external-tables)

### Visualization

- [lightdash](https://github.com/lightdash/lightdash) - Open source Looker alternative with deep dbt integration
- [superset](https://superset.apache.org/) - Open source visualization layer for your Modern Data Stack
