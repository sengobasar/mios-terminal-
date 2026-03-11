import sys
import os
import time
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from mios.core.executor import run_action
from mios.core.planner import plan_from_error
from mios.core.system import get_system_info
from mios.ai.intent_classifier import IntentClassifier

def main():
    # Load the model
    model  = IntentClassifier.load_model()

    # Get the system information
    system_info  = get_system_info()

    # Print the system information
    print(system_info)

    # Get the command
    command  = input("Enter the command: ")

    # Classify the intent
    intent  = classify_intent(command)

    # Print the intent
    print(f"The intent is: 
    {intent}")

    # Run the action
    run_action(system_info, command, intent)

def classify_intent(text):
    """
    Detects the intent of the command
    """
    # Vectorize the text
    vectorizer  = CountVectorizer()
    X  = vectorizer.fit_transform(text)

    # Predict the intent
    y_pred  = model.predict(X)

    # Return the intent
    return y_pred[0]

if 
