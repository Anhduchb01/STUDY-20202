from __future__ import print_function
from ortools.linear_solver import pywraplp
N = 4
A = 150
C = 200
c = [10,12,15,10]
a = [4,2,7,5]
f = [5,6,4,8]
m = [10,12,6,4]
solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
x = {}
for j in range(N):
  x[j] = solver.IntVar(0, infinity, 'x[%i]' % j)
print('Number of variables =', solver.NumVariables())
solver.Add(sum([c[i]*x[i] for i in range(N)]) <= C)
solver.Add(sum([a[i] *x[i] for i in range(N)]) <= A)
solver.Add(x[i]>= m[i] for i in range(N))
solver.Maximize(sum([f[i] * x[i] for i in range(N)]))
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
  print('Objective value =', solver.Objective().Value())
  for j in range(N):
    print(x[j].name(), ' = ', x[j].solution_value())
  print()
  print('Problem solved in %f milliseconds' % solver.wall_time())
  print('Problem solved in %d iterations' % solver.iterations())
  print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
else:
  print('The problem does not have an optimal solution.')