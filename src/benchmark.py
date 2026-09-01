import pandas as pd

def build_benchmark():
    tasks = [
        ("elasticity_01","quantitative","Price rises 10% and quantity falls 15%. Approximate price elasticity?","-1.5"),
        ("abtest_01","experimentation","Treatment conversion is 12% and control is 10%. Absolute effect in percentage points?","2"),
        ("causal_01","causal","Sales are higher among firms that buy ads. Does this alone identify advertising's causal effect?","no"),
        ("profit_01","business","Revenue rises $120,000 and incremental cost is $80,000. Incremental profit?","40000"),
        ("did_01","causal","What key identifying assumption is commonly required for difference-in-differences?","parallel trends"),
        ("srm_01","experimentation","Why check for sample ratio mismatch in an experiment?","randomization"),
    ]
    return pd.DataFrame(tasks, columns=["task_id","category","prompt","reference_answer"])
