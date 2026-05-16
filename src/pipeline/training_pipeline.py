



class TrainingPipeline:

    def __init__(self):
        pass

    def start_data_ingestion(self):
        from src.components.data_ingestion import DataIngestion
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        return train_data_path, test_data_path

    def start_data_transformation(self, train_data_path, test_data_path):
        from src.components.data_transformation import DataTransformation
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initialize_data_transformation(
            train_data_path,
            test_data_path
        )
        return train_arr, test_arr

    def start_model_training(self, train_arr, test_arr):
        from src.components.model_trainer import ModelTrainer
        model_trainer_obj = ModelTrainer()
        model_trainer_obj.initate_model_training(train_arr, test_arr)

    def start_model_evaluation(self, train_arr, test_arr):
        from src.components.model_evaluation import ModelEvaluation
        model_eval_obj = ModelEvaluation()
        model_eval_obj.initiate_model_evaluation(train_arr, test_arr)


if __name__ == "__main__":
    training_pipeline = TrainingPipeline()

    train_data_path, test_data_path = training_pipeline.start_data_ingestion()

    train_arr, test_arr = training_pipeline.start_data_transformation(
        train_data_path,
        test_data_path
    )

    training_pipeline.start_model_training(train_arr, test_arr)
    training_pipeline.start_model_evaluation(train_arr, test_arr)