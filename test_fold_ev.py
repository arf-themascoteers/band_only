from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    c = FoldEvaluator(prefix="no_es2", folds=10, algorithms=["mlr","svr","ann","ann_es"])
    c.process()