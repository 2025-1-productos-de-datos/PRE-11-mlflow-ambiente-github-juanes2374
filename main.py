import mlflow

if __name__ == "__main__":
    with mlflow.start_run():
        mlflow.log_param("param1", 5)
        mlflow.log_metric("metric1", 0.85)
    print("MLflow experiment logged!")
