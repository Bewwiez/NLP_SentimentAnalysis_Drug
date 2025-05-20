# Sentiment Analysis on Drug Benefit Reviews with BioBERT

## Dependencies

The project relies on the following Python Libraries:
PyTorch,pandas, datasets, transformers, numpy, seaborn, and sklearn

Installing PyTorch with GPU support on their official website: 
https://pytorch.org/get-started/locally/

The rest of the packages can be installed like so:

pip install transformers[torch] datasets scikit-learn pandas numpy seaborn

## Code Explanation

The only important file to look at is the Modeling.ipynb. The EDA file is where I initially played with my data and the tokenizers.

Following the notebook one can just run each block to initialize functions and variables until the cross validation section.

### Data set up 

The data is read in as a pandas data frame in cell 2. Cell 3 fills in all the n/a with blanks. 
Cell 4 and 5 allow the consumer ratings to be turned into sentiments with 0 representing negative and 2 representing positive. 

### Functions and Training Arguments
After running the tokenizer and get_model functions one can change the training parameters to fit their needs.

The notable parameters are :<br>

epoch_Numb : changing this will change the number of iterations for each training split<br>

batch_size: changing this will change the number of samples processed at once<br>

These two hyperparameters should be adjusted based on your specs


### Cross Validation 
Right before the for loop : drug_train_benefits_df = drug_train_df[['benefitsReview','sentiment_label']].copy() <br>
By changing benefitsReview to other review columns in the data base will change the type of review the model will be trained on. Make sure to update the column names of earlier dataframe manipulations as well!

## Notebook Workflow

Load in Data<br>
Run data cleaning lines such as replacing n/a's and the creation of sentiment column <br>
Run the functions and training argument cells <br>
Run the cross validation for loop <br>
It will generate metrics for each epoch and split <br>
Load the trained model and use it on the test data set<br>

Similar results can be achieved if nothing is changed from the notebook (the hyperparameters are unchanged)

