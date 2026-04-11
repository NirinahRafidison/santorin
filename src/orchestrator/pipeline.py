import os
from src.config import DATA_DIR, OUTPUT_DIR
from src.loaders.loader_factory import LoaderFactory
from src.processors.data_processor import DataProcessor
from src.translators.translator import Translator
from src.evaluators.evaluator import Evaluator


class Pipeline:
    def run(self):
        file_path = os.path.join(DATA_DIR, "sample02.json")

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

        loader = LoaderFactory.create(file_path)
        df = loader.to_dataframe()
        print(f"Loaded {len(df)} rows.")

        processor = DataProcessor(df)
        df = processor.clean()

        translator = Translator("Helsinki-NLP/opus-mt-fr-en")
        df = translator.translate(df, column="source", new_column="translation")

        if not os.path.isdir(OUTPUT_DIR):
            raise RuntimeError(f"Output directory does not exist: {OUTPUT_DIR}")

        output_path = os.path.join(OUTPUT_DIR, "translated.csv")

        df.to_csv(output_path, index=False)
        print(f"Saved translated file to: {output_path}")

        evaluator = Evaluator(df)
        scores = evaluator.evaluate()

        print("\n📊 Translation quality metrics:")
        for metric, value in scores.items():
            print(f"  {metric}: {value:.2f}")


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()