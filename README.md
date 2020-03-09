# svdExamples.py

# Intro
Just a simple example of SVD(Singualr Value Decomposition) algorithm using two orthogonal functions;
a*sin(t) and b*cos(t) 

# Idea
Every matrix is just a composition of Rotation, Stretching, Rotation

# How it works
Exact reverse of ICA(Independent Component Analysis) without whitening 
1. Multiply matrix(MAT) to column matrix of two orthogonal functions
2. Calculate covariance to determine direction
3. Scaling
4. Use secret 'Algorithm'
5. UsV^t = MAT

# ALGORITHM for phase detection
