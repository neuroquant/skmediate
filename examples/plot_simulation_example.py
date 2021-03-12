"""
Simulation Example
===============================

We are just putting this here for now, so that doc builds run

"""

outcomes, exposures, mediators, true_alpha, true_beta, true_gam = make_null_mediation(dag_type='null-dag1')
print(true_alpha)
print(np.round(np.transpose(true_beta),1))
print(np.round(np.transpose(true_gam)),1)

outcomes, exposures, mediators, true_alpha, true_beta, true_gam = make_null_mediation(dag_type='null-dag2')
print(true_alpha)
print(np.round(np.transpose(true_beta),1))
print(np.round(np.transpose(true_gam)),1)

outcomes, exposures, mediators, true_alpha, true_beta, true_gam = make_null_mediation(dag_type='null-dag3')
print(true_alpha)
print(np.round(np.transpose(true_beta),1))
print(np.round(np.transpose(true_gam)),1)
