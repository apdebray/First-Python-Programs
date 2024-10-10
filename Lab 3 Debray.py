# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 07:34:04 2024

@author: arman
"""
#importing re to clean keywords in txt file from dashes, counter is to count keywords in the feedback
import re
from collections import Counter

# Define the file paths, including new feedback_summary.txt file
feedback_file_path = "C:\\Users\\arman\\OneDrive\\Documents\\PURDUE\\Python Programming\\HWs\\customer_feedback.txt"
keywords_file_path = "C:\\Users\\arman\\OneDrive\\Documents\\PURDUE\\Python Programming\\HWs\\word_sentiment.txt"
summary_file_path = "C:\\Users\\arman\\OneDrive\\Documents\\PURDUE\\Python Programming\\HWs\\feedback_summary.txt"

# Step 1: Read Feedback Entries
with open(feedback_file_path, 'r') as f:
    feedback_lines = f.readlines()

total_feedback = len(feedback_lines) #returns total feedback

# Function to clean keywords, getting rid of uneeded dashes using "re"
def clean_keyword(keyword):
    return re.sub(r'[^a-zA-Z0-9]', '', keyword)

# Function to read keywords from files
def read_keywords(file_path, start_line, end_line):
    keywords = set() 
    with open(file_path, 'r') as file:
        for _ in range(start_line):
            file.readline()
        for _ in range(start_line, end_line):
            line = file.readline()
            if not line:
                break
            word = line.strip()
            cleaned_word = clean_keyword(word)
            if cleaned_word:
                keywords.add(cleaned_word)
    return keywords

# Read positive, negative, and neutral keywords specifically from keyword txt file 
positive_keywords = read_keywords(keywords_file_path, 0, 26)
negative_keywords = read_keywords(keywords_file_path, 27, 42)
neutral_keywords = read_keywords(keywords_file_path, 44, 52)

# Step 2: Analyze Feedback Entries
def classify_feedback(feedback_lines, pos_keywords, neg_keywords, neut_keywords):
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    keyword_occurrences = {'positive': Counter(), 'negative': Counter(), 'neutral': Counter()}
    
    for feedback in feedback_lines:
        words = re.findall(r'\b\w+\b', feedback.lower())
        pos_count = sum(word in pos_keywords for word in words)
        neg_count = sum(word in neg_keywords for word in words)
        neut_count = sum(word in neut_keywords for word in words)
        
        #compares in each feeback sentence the presence of neg, neut, and pos keywords, assigning a winning overall sentiment
        if pos_count > max(neg_count, neut_count):  
            sentiment_counts['positive'] += 1
            keyword_occurrences['positive'].update(word for word in words if word in pos_keywords)
        elif neg_count > max(pos_count, neut_count):
            sentiment_counts['negative'] += 1
            keyword_occurrences['negative'].update(word for word in words if word in neg_keywords)
        else:
            sentiment_counts['neutral'] += 1
            keyword_occurrences['neutral'].update(word for word in words if word in neut_keywords)
    
    return sentiment_counts, keyword_occurrences

# Classify each feedback entry
sentiment_counts, keyword_occurrences = classify_feedback(feedback_lines, positive_keywords, negative_keywords, neutral_keywords)

# Calculate average word count per feedback entry
def average_word_count(feedback_lines):
    total_words = sum(len(re.findall(r'\b\w+\b', feedback.lower())) for feedback in feedback_lines)
    return total_words / len(feedback_lines) if feedback_lines else 0

avg_word_count = average_word_count(feedback_lines)

# Calculate the overall sentiment distribution, simple percentage
def calculate_sentiment_distribution(sentiment_counts, total_feedback):
    return {sentiment: (count / total_feedback) * 100 for sentiment, count in sentiment_counts.items()}

sentiment_distribution = calculate_sentiment_distribution(sentiment_counts, total_feedback)

# Create a function to generate a text-based bar chart, googled how to do this one
def generate_bar_chart(distribution, max_width=50):
    max_value = max(distribution.values(), default=1)  # Avoid division by zero
    chart = ""
    for sentiment, percentage in distribution.items():
        bar_length = int((percentage / max_value) * max_width)
        bar = "█" * bar_length
        chart += f"{sentiment.capitalize()}: {percentage:.2f}% {bar}\n"
    return chart

# Output results to a text file
with open(summary_file_path, 'w') as f:
    f.write(f"Total number of feedback entries: {total_feedback}\n")
    f.write(f"Average word count per feedback entry: {avg_word_count:.2f}\n\n")
    
    f.write("Sentiment distribution (percentage):\n")
    for sentiment, percentage in sentiment_distribution.items():
        f.write(f"{sentiment.capitalize()}: {percentage:.2f}%\n")
    
    f.write("\nSentiment Distribution Bar Chart:\n")
    f.write(generate_bar_chart(sentiment_distribution))
    
    f.write("\nTop 3 positive keywords:\n")
    for keyword, count in Counter({word: keyword_occurrences['positive'][word] for word in positive_keywords}).most_common(3):
        f.write(f"{keyword}: {count}\n")
    
    f.write("\nTop 3 negative keywords:\n")
    for keyword, count in Counter({word: keyword_occurrences['negative'][word] for word in negative_keywords}).most_common(3):
        f.write(f"{keyword}: {count}\n")
    
    f.write("\nTop 3 neutral keywords:\n")
    for keyword, count in Counter({word: keyword_occurrences['neutral'][word] for word in neutral_keywords}).most_common(3):
        f.write(f"{keyword}: {count}\n")

print(f"Summary written to {summary_file_path}")




