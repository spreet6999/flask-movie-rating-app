# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
from random import random
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
import plotly.express as px
from apps import template_obj, chart_template, page_template
from app import app, context  # other objects such as "indicator" can be imported and used it
from collections import Counter

preprocessed_text = context.catalog.load('preprocessed_text')
# texts = context.catalog.load('gensim_lda_texts')
corpus = context.catalog.load('gensim_lda_corpus')
# dictionary = context.catalog.load('gensim_lda_dictionary')
gensim_lda_model = context.catalog.load('gensim_lda_model')

# Load clean text
preprocessed_text = pd.Series(preprocessed_text, name="text")

# Load clean text
preprocessed_text = pd.Series(preprocessed_text, name="text")

word_count = preprocessed_text.apply(lambda x: len(x.split()))
word_count.name = "word_count"

preprocessed_text_df = pd.concat([preprocessed_text, word_count], axis=1)

for topic_id in range(gensim_lda_model.num_topics):
    topk = gensim_lda_model.show_topic(topic_id, 10)
    topk_words = [w for w, _ in topk]
    print('{}: {}'.format(topic_id, ' '.join(topk_words)))


# Visualize the topics
# pyLDAvis.enable_notebook()
# vis = pyLDAvis.gensim.prepare(gensim_lda_model, corpus, dictionary)
# pyLDAvis.save_html(vis,  str(proj_path / 'data/08_reporting/gensim_pylda.html'))

def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row[0], key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num),
                                                                  round(prop_topic, 4)]),
                                                       ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic'
        , 'Perc_Contribution'
                              ]

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return sent_topics_df


df_topic_sents_keywords = format_topics_sentences(ldamodel=gensim_lda_model,
                                                  corpus=corpus,
                                                  texts=preprocessed_text)

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Text']

df_dominant_topic['document_length'] = df_dominant_topic['Text'].apply(lambda x: len(x))

fig = go.Figure()

for topic_id in range(gensim_lda_model.num_topics):
    df_dominant_topic_sub = df_dominant_topic.loc[df_dominant_topic.Dominant_Topic == topic_id, :]
    fig.add_trace(go.Histogram(x=df_dominant_topic_sub['document_length'], name='Topic ' + str(topic_id)))

# Overlay both histograms
fig.update_layout(
    title="Frequency Distribution of Word Counts by Topic",
    xaxis_title="Document Length",
    yaxis_title="Count",
    barmode='overlay')

# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)

test = dcc.Markdown('''
Topic word distribution is helpful to understand the inherent difference in the topics based on the size of the documents.
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Topic Distribution:",
                                          left_panel_content=template_obj.graph_content(
                                              figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
