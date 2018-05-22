---
title: "EDA and XGB Avito"
author: "Bukun"
output:
  html_document:
    number_sections: true
    toc: true
    fig_width: 10
    code_folding: hide
    fig_height: 4.5
    theme: cosmo
    highlight: tango
---


# Preparation{.tabset .tabset-fade .tabset-pills}

       
## Load Libraries

```{r,message=FALSE,warning=FALSE}

library(tidyverse)
library(tidytext)
library(stringr)
library(knitr)
library(lubridate)
library(caret)

library(tidytext)
library(wordcloud)

library(text2vec)
library(stopwords)
library(Matrix)

```

## Read the data

```{r,message=FALSE,warning=FALSE}

rm(list=ls())

fillColor = "#FFA07A"
fillColor2 = "#F1C40F"

train = read_csv("../input/train.csv",locale = locale(encoding = stringi::stri_enc_get()))
test = read_csv("../input/test.csv",locale = locale(encoding = stringi::stri_enc_get()))
periods_train <- read_csv("../input/periods_train.csv")

TotalNumberOfRows = nrow(train)

train <-train %>%
  mutate(title_len = str_count(title)) %>%
  mutate(description_len = str_count(description))

test <-test %>%
  mutate(title_len = str_count(title)) %>%
  mutate(description_len = str_count(description))

```
