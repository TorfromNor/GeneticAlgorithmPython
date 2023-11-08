import pygad
import random

num_generations = 100
sol_per_pop = 10
num_parents_mating = 5

def number_saved_solutions(keep_elitism=1, 
                           keep_parents=-1,
                           mutation_type="random",
                           mutation_percent_genes="default",
                           parent_selection_type='sss',
                           multi_objective=False,
                           fitness_batch_size=None,
                           save_solutions=False,
                           save_best_solutions=False):

    def fitness_func_no_batch_single(ga, solution, idx):
        return random.random()

    def fitness_func_no_batch_multi(ga_instance, solution, solution_idx):
        return [random.random(), random.random()]

    def fitness_func_batch_single(ga_instance, solution, solution_idx):
        f = []
        for sol in solution:
            f.append(random.random())
        return f

    def fitness_func_batch_multi(ga_instance, solution, solution_idx):
        f = []
        for sol in solution:
            f.append([random.random(), random.random()])
        return f

    if fitness_batch_size is None or (type(fitness_batch_size) in pygad.GA.supported_int_types and fitness_batch_size == 1):
        if multi_objective == True:
            fitness_func = fitness_func_no_batch_multi
        else:
            fitness_func = fitness_func_no_batch_single
    elif (type(fitness_batch_size) in pygad.GA.supported_int_types and fitness_batch_size > 1):
        if multi_objective == True:
            fitness_func = fitness_func_batch_multi
        else:
            fitness_func = fitness_func_batch_single

    ga_optimizer = pygad.GA(num_generations=num_generations,
                            sol_per_pop=sol_per_pop,
                            num_genes=6,
                            num_parents_mating=num_parents_mating,
                            fitness_func=fitness_func,
                            mutation_type=mutation_type,
                            parent_selection_type=parent_selection_type,
                            mutation_percent_genes=mutation_percent_genes,
                            keep_elitism=keep_elitism,
                            keep_parents=keep_parents,
                            suppress_warnings=True,
                            fitness_batch_size=fitness_batch_size,
                            save_best_solutions=save_best_solutions,
                            save_solutions=save_solutions)

    ga_optimizer.run()

    if save_solutions == True:
        expected_num_solutions = sol_per_pop + num_generations * sol_per_pop
    else:
        expected_num_solutions = 0

    if save_best_solutions == True:
        expected_num_best_solutions = 1 + num_generations
    else:
        expected_num_best_solutions = 0

    print(f"Expected number of solutions is {expected_num_solutions}.")
    print(f"Actual number of solutions is {len(ga_optimizer.solutions)}.")
    print(f"Expected number of best solutions is {expected_num_best_solutions}.")
    print(f"Actual number of best solutions is {len(ga_optimizer.best_solutions)}.")
    return expected_num_solutions, len(ga_optimizer.solutions), len(ga_optimizer.solutions_fitness), expected_num_best_solutions, len(ga_optimizer.best_solutions)

def test_save_solutions_default_keep():
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions()
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_no_keep(multi_objective=False,
                                parent_selection_type='sss',
                                fitness_batch_size=None,
                                save_solutions=False,
                                save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=0, 
                                                                                                                                            keep_parents=0,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_keep_elitism(multi_objective=False,
                                     parent_selection_type='sss',
                                     fitness_batch_size=None,
                                     save_solutions=False,
                                     save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=3, 
                                                                                                                                            keep_parents=0,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_keep_parents(multi_objective=False,
                                     parent_selection_type='sss',
                                     fitness_batch_size=None,
                                     save_solutions=False,
                                     save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=0, 
                                                                                                                                            keep_parents=4,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_both_keep(multi_objective=False,
                                  parent_selection_type='sss',
                                  fitness_batch_size=None,
                                  save_solutions=False,
                                  save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=3, 
                                                                                                                                            keep_parents=4,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_no_keep_adaptive_mutation(multi_objective=False,
                                                  parent_selection_type='sss',
                                                  fitness_batch_size=None,
                                                  save_solutions=False,
                                                  save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=0, 
                                                                                                                                            keep_parents=0,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            mutation_type="adaptive",
                                                                                                                                            mutation_percent_genes=[10, 5],
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_default_adaptive_mutation(multi_objective=False,
                                                  parent_selection_type='sss',
                                                  fitness_batch_size=None,
                                                  save_solutions=False,
                                                  save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(mutation_type="adaptive",
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            mutation_percent_genes=[10, 5],
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

def test_save_solutions_both_keep_adaptive_mutation(multi_objective=False,
                                                    parent_selection_type='sss',
                                                    fitness_batch_size=None,
                                                    save_solutions=False,
                                                    save_best_solutions=False):
    expected_solutions, actual_solutions, actual_solutions_fitness, expected_best_solutions, actual_best_solutions = number_saved_solutions(keep_elitism=3, 
                                                                                                                                            keep_parents=4,
                                                                                                                                            parent_selection_type=parent_selection_type,
                                                                                                                                            mutation_type="adaptive",
                                                                                                                                            mutation_percent_genes=[10, 5],
                                                                                                                                            multi_objective=multi_objective,
                                                                                                                                            fitness_batch_size=fitness_batch_size,
                                                                                                                                            save_solutions=save_solutions,
                                                                                                                                            save_best_solutions=save_best_solutions)
    assert expected_solutions == actual_solutions
    assert expected_solutions == actual_solutions_fitness
    assert expected_best_solutions == actual_best_solutions

if __name__ == "__main__":
    #### Single-objective
    print()
    test_save_solutions_default_keep()
    print()
    test_save_solutions_no_keep(save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(save_solutions=True,
                                                    save_best_solutions=True)
    print()

    #### Multi-Objective
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(multi_objective=True,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(multi_objective=True,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(multi_objective=True,
                                  save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(multi_objective=True,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(multi_objective=True,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(multi_objective=True,
                                                    save_solutions=True,
                                                    save_best_solutions=True)
    print()

    #### Multi-Objective NSGA-II Parent Selection
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                parent_selection_type='nsga2',
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(multi_objective=True,
                                     parent_selection_type='nsga2',
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(multi_objective=True,
                                     parent_selection_type='nsga2',
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(multi_objective=True,
                                  parent_selection_type='nsga2',
                                  save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(multi_objective=True,
                                                  parent_selection_type='nsga2',
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(multi_objective=True,
                                                  parent_selection_type='nsga2',
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(multi_objective=True,
                                                    parent_selection_type='nsga2',
                                                    save_solutions=True,
                                                    save_best_solutions=True)
    print()


    #### Single-objective
    print()
    test_save_solutions_no_keep(fitness_batch_size=1,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=2,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=3,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=4,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=5,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=6,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=7,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=8,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=9,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(fitness_batch_size=10,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(fitness_batch_size=4,
                                  save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(fitness_batch_size=4,
                                                    save_solutions=True,
                                                    save_best_solutions=True)
    print()

    #### Multi-Objective
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                fitness_batch_size=1,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                fitness_batch_size=4,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                fitness_batch_size=9,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                fitness_batch_size=10,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(multi_objective=True,
                                     fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(multi_objective=True,
                                     fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(multi_objective=True,
                                  fitness_batch_size=4,
                                  save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(multi_objective=True,
                                                  fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(multi_objective=True,
                                                  fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(multi_objective=True,
                                                    fitness_batch_size=4,
                                                    save_solutions=True,
                                                    save_best_solutions=True)
    print()

    #### Multi-Objective NSGA-II Parent Selection
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                parent_selection_type='nsga2',
                                fitness_batch_size=1,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                parent_selection_type='nsga2',
                                fitness_batch_size=4,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                parent_selection_type='nsga2',
                                fitness_batch_size=9,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_no_keep(multi_objective=True,
                                parent_selection_type='nsga2',
                                fitness_batch_size=10,
                                save_solutions=True,
                                save_best_solutions=True)
    print()
    test_save_solutions_keep_elitism(multi_objective=True,
                                     parent_selection_type='nsga2',
                                     fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_keep_parents(multi_objective=True,
                                     parent_selection_type='nsga2',
                                     fitness_batch_size=4,
                                     save_solutions=True,
                                     save_best_solutions=True)
    print()
    test_save_solutions_both_keep(multi_objective=True,
                                  parent_selection_type='nsga2',
                                  fitness_batch_size=4,
                                  save_solutions=True,
                                  save_best_solutions=True)
    print()
    test_save_solutions_no_keep_adaptive_mutation(multi_objective=True,
                                                  parent_selection_type='nsga2',
                                                  fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_default_adaptive_mutation(multi_objective=True,
                                                  parent_selection_type='nsga2',
                                                  fitness_batch_size=4,
                                                  save_solutions=True,
                                                  save_best_solutions=True)
    print()
    test_save_solutions_both_keep_adaptive_mutation(multi_objective=True,
                                                    parent_selection_type='nsga2',
                                                    fitness_batch_size=4,
                                                    save_solutions=True,
                                                    save_best_solutions=True)
    print()

