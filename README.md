# Stock Prediction Algorithim

A set of two algorithims, one using a lighter trained model,
and one using heavy GPU based tensorflow model training + prediction.

Each EPOCH takes 0.59ms on the tensor model. The lite model takes almost no time but proves to be less accurate and only provides info 
on wether it will go up or down, not the exact trade patterns or price.
