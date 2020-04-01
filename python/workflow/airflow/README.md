# Apache Airflow
>Learn from [Apache Airflow Documentation](https://airflow.apache.org/docs/stable/). 

![feature-image](https://user-images.githubusercontent.com/44774033/71560206-07175d00-2aaa-11ea-9841-bf39854c2716.png)

## Getting Started
```bash
# install apache airflow
pip install apache-airflow

# initialize the database
airflow initdb

# set airflow home
export AIRFLOW_HOME=...
```

Refer to [here](https://airflow.apache.org/docs/stable/installation.html#extra-packages) if you want to install extra packages. 

## Metadata Validation
```bash
# make sure the pipeline is parsed successfully 
python dags/tutorial.py

# print the list of active DAGs
airflow list_dags

# prints the list of tasks the "tutorial" dag_id
airflow list_tasks tutorial

# prints the hierarchy of tasks in the tutorial DAG
airflow list_tasks tutorial --tree
```

## Testing
```bash
# command layout: command subcommand dag_id task_id date

# testing print_date
airflow test tutorial print_date 2015-06-01

# testing sleep
airflow test tutorial sleep 2015-06-01
```

## Monitoring
```bash
# start the web server
airflow webserver -p 8080

# start the scheduler
airflow scheduler
```

## DAG Runs
```bash
# optional, start a web server in debug mode in the background
# airflow webserver --debug &

# start your backfill on a date range
airflow backfill tutorial -s 2015-06-01 -e 2015-06-07
```

## Life Cycle
<img width="875" alt="スクリーンショット 2019-12-30 11 18 33" src="https://user-images.githubusercontent.com/44774033/71565882-3eabf680-2af6-11ea-8067-71bfedd01406.png">

## Notes
- [簡易メモ](https://esa-pages.io/p/sharing/13096/posts/113/aedcba7a6a71337ef733.html)