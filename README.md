## End to End Machine Learning Project

# Building a model to predict house prices

The model should learn from this data and be able to predict the median housing price in any districts given the metrics

## Things to Consider 
 
 1. What is the bussiness objective: This involves  how the company expect to use and benefit from the model

 2. If its worth investing in a certain paramater or not 

  The Seqence of data processing components is called Data pipeline
    ``` Pipelines are common since there is alot of data to manipulate ```

## Bussiness Goal 
`` Predictions to be feed into in investment decision system``  
``The decision will be feed into another system along with manymore other signals``

 ## Framing the problem :
  Boss explains how its costly using a team of experts to estimate the price of a house and still is 20% off

  ``The  problem is a Supervised Theory  and it is a Regression problem``

  Multiple Regression: Multiple features used to make prediction
  Univatiate Regression: only  try to predict  a single value in a statistical data
  linear Regression: output is continous 

  ## PERFOMANCE MEASURES :

  Root Mean Square Error (RMSE). It gives an idea of how
  much error the system typically makes in its predictions, with a higher weight for
  large errors. Equation 2-1 shows the mathematical formula to compute the RMSE.
  Root Mean Square Error (RMSE):
  RMSE(X, h) = √[ (1/n) * ∑ (h(xᵢ) - yᵢ)² ]

  Even though the RMSE is generally the preferred performance measure for regression
tasks, in some contexts you may prefer to use another function. For example, suppose
that there are many outlier districts. In that case, you may consider using the Mean
Absolute Error

  MAE(X, h) = (1/n) * ∑ |h(xᵢ) - yᵢ|
  

 ## Getting the Data Ready

Before training any model, you need to prepare your data. First, you separate the information you want to predict (the target) from the rest of the data. This keeps things organised.  

## Handling Missing Information
Real-world data often has gaps. You have a few ways to deal with missing values:

You can remove the entire row with missing data.

You can remove the whole column if it has too many gaps.

You can fill the gaps with a typical value, like the most common or middle value.

The most important rule: if you compute a fill value (like the middle value), you must compute it using only your training data and save it. You will need to use the exact same value later when filling gaps in new data or test data.


## Dealing with Text Categories

Machine learning algorithms prefer numbers, so text categories must be converted. There are two common ways:

Numbering categories: Turn each category into a number (like 0, 1, 2). But this can mislead the algorithm into thinking the numbers have an order.

One-hot encoding: Create a separate "yes/no" column for each category. This avoids the order problem but can create many columns if there are many categories.

## Creating New Features


## Scaling the Numbers
Features often have very different ranges. Most algorithms work better when all features are on a similar scale. There are two main approaches:

Normalization: Squeezing values into a fixed range, like between zero and one.

Standardization: Centring values around zero and adjusting for spread. This is less affected by extreme values.


## Building a Smooth Workflow
Instead of doing each preparation step manually, you chain them together. This creates a single, repeatable process that:

Cleans missing values.

Adds custom features.

Scales the data.

Handles text categories separately from numbers.

This pipeline ensures that the same transformations are applied consistently to your training data, your test data, and any new data in the future. It also prevents accidental "leakage" of information from the test set into the training process.

## Choosing and Training Models
Now that your data is clean and prepared, you can start training models. It is wise to try several different types.

A simple linear model might underfit (it can't capture complex patterns).

A more complex model, like a decision tree, might overfit (it learns the training data too perfectly and fails on new data).

An ensemble model, which combines many simpler models, often gives the best balance.

## Checking Performance Properly

Instead of testing a model only on the data it was trained on, you use cross-validation. This means you split your training data into several parts, train on some parts and test on the others, rotating through them. This gives you a more honest estimate of how the model will perform on unseen data, along with a sense of how stable that performance is.

## Fine-Tuning the Best Models

Once you have a shortlist of promising models, you need to find the best settings for them (these are called hyperparameters).

A grid search tries every combination of a set of values you choose. This is thorough but can be slow.

A random search tries random combinations. This is faster and often finds good results when the number of settings is large.

You can also combine your best models into an ensemble, which usually improves overall performance.

## Learning from the Best Model

After finding the best model, you look at which features it found most important. This gives you valuable insight into the problem—for example, you might discover that income matters more than location. You can use this knowledge to simplify your system by dropping unimportant features.

## Final Evaluation and Launch

Only after all your tuning is complete do you test your final model on the test set that you set aside at the beginning. This gives you the final, honest estimate of its real-world performance. You can also calculate a range (confidence interval) to understand how precise your estimate is.

At this stage, you present your findings, document what worked and what didn't, and list any limitations.

## After Launching
The work doesn't stop at launch. You need to:

Monitor performance in the live system and set up alerts for when it drops.

Check the input data quality regularly, as bad data can slowly degrade your model.

Retrain the model regularly with fresh data to prevent it from becoming outdated.

Automate the entire process as much as possible, including saving backups so you can easily revert to a working version if something goes wrong.

