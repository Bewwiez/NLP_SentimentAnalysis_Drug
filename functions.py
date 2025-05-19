import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import seaborn as sns
import torch  
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from datasets import Dataset 
print('hi')
 
model_Path = 'dmis-lab/biobert-v1.1' 
tokenizer = AutoTokenizer.from_pretrained(model_Path)
num_unique_Labels = 3
labels = ['negative','neutral','positive']
id2label = {i: label for i, label in enumerate(labels)}
label2id = {label: i for i, label in enumerate(labels)}

def model_Metrics(pred_label):
    predictions, label_ids = pred_label

def fine_tune_BioBERT(tokenized_Data):

model = AutoModelForSequenceClassification.from_pretrained(
    model_Path,
    num_labels = num_unique_Labels,
    id2label = id2label,
    label2id =label2id
)

