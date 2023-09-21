from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    c = FoldEvaluator(prefix="t2", folds=10, algorithms=["mlr","svr"])
    c.process()