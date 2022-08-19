from ortools.sat.python import cp_model
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count
N = 4
A = 500
C = 1000
c = [10,12,15,10]
a = [4,2,7,5]
f = [5,6,4,8]
m = [10,12,6,4]
model = cp_model.CpModel()
x = {}
for i in range(N):
    x[i] = model.NewIntVar(1,N,'x[' + str(i) + ']') 
c1 = model.Add(C >= sum(c[i] * x[i] for i in range(N)))
c2 = model.Add(A >= sum(a[i] * x[i] for i in range(N)))
b = model.NewBoolVar('b')

#constraints

model.Add(x[i] < m[i] for i in range(N)).OnlyEnforceIf(b)
model.Add(x[i] >= m[i] for i in range(N)).OnlyEnforceIf(b.Not())

model.Add(x[i] == 0 for i in range(N)).OnlyEnforceIf(b)
solver = cp_model.CpSolver()
solver.parameters.search_branching = cp_model.FIXED_SEARCH

vars = [x[i] for i in range(5)]

	
solution_printer = VarArraySolutionPrinter(vars)
solver.SearchForAllSolutions(model,solution_printer)