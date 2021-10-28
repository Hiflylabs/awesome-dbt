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

### Resources

- [dbt + Materialize: Streaming to a dbt project near you](https://blog.getdbt.com/dbt-materialize-streaming-to-a-dbt-project-near-you/) - How to own your real-time transformation workflows like batch-based alternatives.
- [Who's really using dbt?](https://semistructured.substack.com/p/dbt-analytics-engineering-or-data-engineering)
- [dbt and the Analytics Engineer — what’s the hype about](https://medium.com/validio/dbt-and-the-analytics-engineer-whats-the-hype-about-907eb86c4938)
- [dbtvault](https://dbtvault.readthedocs.io/en/latest/) - Package for generating and executing ETL for Data Vault 2.0 on Snowflake

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
- [How to review an analytics pull request](https://blog.getdbt.com/how-to-review-an-analytics-pull-request/)

## Tools

- [vscode-dbt-power-user](https://github.com/innoverio/vscode-dbt-power-user)

### Testing

- [dbt-expectations](https://github.com/calogica/dbt-expectations) - Port between dbt and great_expectations to extend out-of-the-box tests.
- [re_data](https://www.getre.io/) - dbt package for montioring metrics and detect anomalies.
- [How do you test your data](https://discourse.getdbt.com/t/how-do-you-test-your-data/149) - Suggestions on testing your data powered by the community
- [How to unit test sql transforms in dbt](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/)

### Packages

- [dbt-coves](https://pypi.org/project/dbt-coves/) - CLI tool for generating a scaffold for your dbt project
- [dbt-profiler](https://hub.getdbt.com/data-mie/dbt_profiler/latest/) - data profiling and doc block generator 
- [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) - General macros library. A must have.
- [dbt-ml-preprocessing](https://github.com/omnata-labs/dbt-ml-preprocessing)
- 
### Visualization

- [lightdash](https://github.com/lightdash/lightdash) - Open source Looker alternative with deep dbt integration
- [superset](https://superset.apache.org/) - Open source visualization layer for your Modern Data Stack
